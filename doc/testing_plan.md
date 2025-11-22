

 Testing Plan

This document describes how each part of the system should be tested.

 **1. Unit Testing**

 Feature Extraction

* Test if MediaPipe detects hands correctly
* Test if CSV is generated

Model Training

* Validate number of features
* Test model accuracy

 **2. Integration Testing**

 Flask + Model

* Upload image → Check prediction returned
* Test speech generation
* Validate that result is saved in database

 **3. UI Testing**

* Verify upload button works
* Result page displays correct label
* Analytics page loads charts properly

 **4. Database Testing**

* User registration/login works
* Predictions stored correctly

 **5. End-to-End Testing**

* Upload image → Get prediction → Hear audio → View analytics
* Ensure no crashes

---

