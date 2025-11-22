

ER Diagram (Entity-Relationship)

This diagram describes how data is stored inside the SQLite database.

 **Entities:**

 **1. Users**

* id (PK)
* username
* password
* created_at

 **2. Predictions**

* id (PK)
* user_id (FK → Users.id)
* label
* timestamp
* image_path

 **ER Diagram (Text Representation)**

```
 Users (1) -------- (∞) Predictions
```

Meaning: One user can have many predictions.

---