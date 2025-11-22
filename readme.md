 Sign2Speech – Image-Based Sign Language to Speech Converter

 Overview
Sign2Speech is a beginner-friendly project that converts **static sign language images** into **spoken audio output** using a combination of:

- Image Upload
- MediaPipe Hand Landmark Extraction
- Machine Learning (Random Forest Classifier)
- Flask Web Application
- Text-to-Speech (gTTS)






 Features
- Upload any static image of a hand sign
- Automatic hand-landmark extraction using MediaPipe
- Machine-Learning-based classification
- Text-to-Speech output
- User Authentication (Register/Login)
- Prediction History storage in SQLite database
- Analytics Dashboard using Chart.js
- Organized dataset with CRUD structure
- Fully modular folder structure for maximum clarity



Technologies Used
- **Flask**
- **python**
- **MediaPipe**
- **OpenCV**
- **pandas / numpy**
- **scikit-learn**
- **gTTS**
- **SQLite3**
- **Chart.js**

---

## 📁 Project Structure
sign2speech/
│ README.md
│ statement.md
│ requirements.txt
│
├── app/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── result.html
│   │   ├── analytics.html
│   │   ├── login.html
│   │   └── register.html
│   └── static/
│       └── style.css
│
├── backend/
│   ├── extract_features.py
│   ├── train_model.py
│   └── utils.py
│
├── data/
│   ├── no/
│   ├── yes/
│   
│
├── features/
│   └── landmarks.csv
│
├── models/
│   └── rf_signs.pkl
│
├── db/
│   └── sign2speech.db
│
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── uml_diagrams.md
│   ├── er_diagram.md
│   └── testing_plan.md
│
└── tests/
    └── test_extract.py

Testing Instructions

Upload clear images with visible hand

Confirm prediction accuracy

Test TTS audio playback

Test login and register functionality

Check analytics dashboard graph

Verify SQLite database entries

⭐ Future Enhancements

Real-time webcam detection

Dynamic gesture recognition

Larger & more diverse dataset

Multilingual speech output

Mobile app version


name - AARNA SAI SHUKLA
Registration no. - 25BEC10061