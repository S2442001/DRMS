# Disaster Resource Management System (DRMS)

A Flask-based web application for coordinating SOS requests, managing shelters and resources, and providing admin oversight during disaster situations.

## Features

### User (Victim)
- Register and login
- Submit SOS requests with location and description
- Track status (Pending / Resolved / Rejected)

### Admin
- Login as administrator
- View and manage all SOS requests
- Add and manage resources (medical kits, food, etc.)
- Add and manage shelters (capacity, available beds)

---

## Technologies Used

- Flask
- Flask-WTF
- Flask-Login
- SQLAlchemy
- SQLite (can be switched to PostgreSQL/MySQL)
- Bootstrap 5 (for UI)

---

##  Getting Started

1. Clone the repo:
   git clone https://github.com/yourusername/drms.git
   cd drms

2. Create & activate virtuaenv
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate   # On Linux/Mac

3. Install Dependencies
   pip install -r requirements.txt

4.  Run the app
   python run.py

#### Future Enhancements for DRMS:
1. Volunteer Management System
   Add a new user role for volunteers who can view, accept, and resolve SOS requests in their area.

2. Real-Time Notifications & Mapping
  Integrate Google Maps for tracking SOS locations and implement SMS/email alerts.

3. REST API & Microservices Architecture
   Expose core functionalities via RESTful APIs and scale the app by modularizing it into independent Flask microservices.


