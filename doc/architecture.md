

 architecture.md

 System Architecture

The Sign2Speech system follows a modular architecture divided into three major components:

 **1. Frontend (Flask Web App)**

* Renders the user interface using HTML/CSS (Jinja templates)
* Accepts image uploads
* Displays predictions and audio playback
* Shows analytics via Chart.js



* Handles image preprocessing
* Uses MediaPipe to extract hand landmarks
* Loads the trained Random Forest model for prediction
* Stores prediction logs and user account information
 **3. Database Layer (SQLite)**

* Stores user records
* Saves prediction history
* Supports authentication

 Architecture Diagram (Text Representation)

```
User → Browser UI → Flask App → ML Backend → SQLite DB
                        ↓
                 Prediction Result → Audio Output
```

---

 
 

 

