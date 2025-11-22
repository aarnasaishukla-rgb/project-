from flask import Flask, request, render_template, redirect, url_for, flash, session, send_from_directory
import os
import joblib
import numpy as np
import cv2
import mediapipe as mp
from gtts import gTTS
from werkzeug.utils import secure_filename

from backend.utils import init_db, get_db_connection, create_user, verify_user

UPLOAD_FOLDER = "uploads"
ALLOWED_EXT = {"png", "jpg", "jpeg"}
MODEL_PATH = "models/rf_signs.pkl"

app = Flask(__name__, template_folder="template")
app.secret_key = "your_secret_key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

init_db()

clf = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
mp_hands = mp.solutions.hands

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT

def extract_features(img_path):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    with mp_hands.Hands(static_image_mode=True, max_num_hands=1) as hands:
        result = hands.process(img_rgb)

        if not result.multi_hand_landmarks:
            return None

        lm = result.multi_hand_landmarks[0].landmark
        arr = np.array([[p.x, p.y, p.z] for p in lm]).flatten()
        return arr

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file uploaded")
            return redirect(request.url)

        f = request.files["file"]
        if f.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if allowed_file(f.filename):
            filename = secure_filename(f.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            f.save(path)

            vector = extract_features(path)
            if vector is None:
                return render_template("results.html", error="No hand detected.")

            prediction = clf.predict([vector])[0]

            tts = gTTS(prediction)
            audio_path = path + ".mp3"
            tts.save(audio_path)

            return render_template("results.html",
                                   label=prediction,
                                   audio=url_for("uploaded_file",
                                                 filename=os.path.basename(audio_path)))

    return render_template("index.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if verify_user(request.form["username"], request.form["password"]):
            session["username"] = request.form["username"]
            return redirect("/")
        else:
            flash("Login failed")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if create_user(request.form["username"], request.form["password"]):
            return redirect("/login")
        else:
            flash("Username exists")

    return render_template("register.html")

@app.route("/analytics")
def analytics():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT predicted_label, COUNT(*) FROM predictions GROUP BY predicted_label")
    rows = cur.fetchall()
    conn.close()

    labels = [r[0] for r in rows]
    counts = [r[1] for r in rows]

    return render_template("analytics.html", labels=labels, counts=counts)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
