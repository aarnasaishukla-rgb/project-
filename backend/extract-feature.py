import mediapipe as mp
import cv2
import numpy as np
import os
import glob
import pandas as pd

mp_hands = mp.solutions.hands

def image_to_landmark_vector(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    with mp_hands.Hands(static_image_mode=True,
                        max_num_hands=1,
                        min_detection_confidence=0.5) as hands:
        result = hands.process(img_rgb)
        if not result.multi_hand_landmarks:
            return None

        lm = result.multi_hand_landmarks[0].landmark
        arr = np.array([[p.x, p.y, p.z] for p in lm]).flatten()
        return arr

def main():
    data_dir = "data"
    out_csv = "features/landmarks.csv"
    os.makedirs("features", exist_ok=True)

    rows = []
    for label in os.listdir(data_dir):
        folder = os.path.join(data_dir, label)
        if not os.path.isdir(folder):
            continue

        for img_path in glob.glob(os.path.join(folder, "*")):
            v = image_to_landmark_vector(img_path)
            if v is None:
                print("No hand detected in", img_path)
                continue

            row = list(v) + [label, os.path.basename(img_path)]
            rows.append(row)

    if not rows:
        print("No features extracted. Check your images.")
        return

    cols = [f"f{i}" for i in range(63)] + ["label", "file"]
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv(out_csv, index=False)

    print("Saved features to", out_csv)

if __name__ == "__main__":
    main()
