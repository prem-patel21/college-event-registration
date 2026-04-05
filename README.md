# Cloud-Based College Event Registration System
### Google Cloud Digital Leader — Semester 2 Capstone Project

## Project Overview
A cloud-native web application that allows students to register 
for college events such as Tech Fest, Cultural Events, and Workshops.

## Local Prototype Tech Stack
| Component  | Technology        |
|------------|-------------------|
| Frontend   | HTML + CSS + JS   |
| Backend    | Python + Flask    |
| Database   | SQLite            |

## How to Run Locally
1. Install Flask: pip install flask
2. Run the app: py app.py
3. Open browser: http://127.0.0.1:5000

## Application URLs
| URL | Description |
|-----|-------------|
| http://127.0.0.1:5000/ | Student Registration Form |
| http://127.0.0.1:5000/registrations | View All Registrations |

## GCP Cloud Architecture
| Local | Google Cloud Equivalent |
|-------|------------------------|
| Flask on localhost | Cloud Run |
| SQLite database | Firestore |
| Direct DB write | Pub/Sub + Cloud Functions |

## GCP Services Used
- **Cloud Run** — Hosts the web app serverlessly
- **Pub/Sub** — Message queue for loose coupling
- **Cloud Functions** — Processes registration data
- **Firestore** — NoSQL cloud database

## Project Structure
```
college-event-registration/
├── app.py
├── database.db
└── templates/
    ├── index.html
    ├── success.html
    └── registrations.html
```
## Screenshots

![Preview 1](assets/screenshots/ss-1.png)
![Preview 2](assets/screenshots/ss-2.png)
