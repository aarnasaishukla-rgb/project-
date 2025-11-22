 Project Statement – Sign2Speech  
 Image-Based Sign Language to Speech Converter

 1. Problem Statement  
Millions of hearing-impaired individuals rely on sign language for communication.  
However, most people cannot understand sign language, which creates daily communication barriers in:

- Hospitals
- Schools
- Transport
- Shops
- Workplaces

There is a need for a simple, low-cost system that converts sign language into speech **without requiring hardware**, making it accessible to everyone.



 2. Objective  
- To develop a system that converts static sign images to speech.  
- To extract hand landmarks using MediaPipe.  
- To train a machine learning model to classify hand gestures.  
- To design a user-friendly web app for recognition & speech.  
- To store user data, predictions, and analytics.  



3. Scope  
The scope includes:

- Accepting uploaded hand-sign images  
- Extracting 21 MediaPipe hand landmarks  
- Converting them into a feature vector  
- ML-based classification (Random Forest)  
- Speech output using gTTS  
- User login & management  
- SQLite database for predictions  
- Analytics dashboard  
- Dataset folder for multi-class signs  



 4. Existing System  
Existing systems require:
- Expensive hardware  
- Real-time gloves and sensors  
- Complex machine learning pipelines  
- High processing power  
- Trained datasets  

These systems are not beginner-friendly or low-cost.



 5. Proposed System  
The proposed system:

- Works **only with images**  
- No hardware required  
- Uses MediaPipe for easy landmark extraction  
- Uses Random Forest for classification  
- Outputs speech using TTS  
- Simple UI for everyday use  
- Fully modular & scalable structure  



6. Target Users  
- Hearing-impaired community  
- Healthcare staff  
- Students & teachers  
- Beginners in machine learning  
- Developers building assistive tools  



 7. Constraints  
- Works only for static signs  
- Lighting must be adequate  
- Needs at least 20–50 images per class



 8. Deliverables  
- Source Code  
- Working Web App  
- Trained Model  
- Documentation  
- Screenshots  
- GitHub Repository  
