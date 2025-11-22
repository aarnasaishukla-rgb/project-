

 UML Diagrams

This section outlines the UML representations of system behavior.

 **1. Use Case Diagram**

```
       +---------------------+
       |      User           |
       +---------------------+
                 |
   -------------------------------------------
   |                System                    |
   |  - Upload image                          |
   |  - Predict sign                          |
   |  - Play speech output                    |
   |  - View analytics                        |
   -------------------------------------------
```

 **2. Class Diagram (Text-Based)**

```
+-------------------+
|  FlaskApp         |
+-------------------+
| +upload_image()   |
| +predict()        |
| +analytics()      |
+-------------------+

+-------------------+
|  MLModel          |
+-------------------+
| +extract()        |
| +train()          |
| +predict()        |
+-------------------+

+-------------------+
|  Database         |
+-------------------+
| +insertUser()     |
| +validateUser()   |
| +logPrediction()  |
+-------------------+
```

 **3. Sequence Diagram**

```
User → Browser → Flask → ML Model → Database → Flask → User
```

---