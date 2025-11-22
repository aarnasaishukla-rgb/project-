

Project Workflow

The workflow describes how the entire Sign2Speech system operates from start to finish.
 **Step 1: Dataset Preparation**

* User places images in `data/<label>/` folders
* Each folder represents one sign

 **Step 2: Feature Extraction**

* `extract_features.py` reads all images
* MediaPipe extracts 21 hand landmarks (x, y, z)
* Landmark vectors saved into `features/landmarks.csv`

 **Step 3: Model Training**

* `train_model.py` loads CSV
* Splits data into training/testing sets
* Trains Random Forest classifier
* Saves model as `models/rf_signs.pkl`

 **Step 4: Web App Execution**

* Flask loads the trained model
* User uploads image
* Backend predicts sign
* gTTS speaks prediction
* SQLite logs activity

 **Step 5: Analytics**

* Flask counts frequency of predictions
* Chart.js visualizes sign usage trends


