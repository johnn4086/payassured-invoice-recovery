# PayAssured – Invoice Recovery Case Tracker

This project is a mini internal CRM built as part of the **PayAssured Full Stack Internship Assignment**.  
It simulates how unpaid invoice recovery cases are tracked and managed within a B2B credit and recovery workflow.

The application provides a clean dashboard to manage clients, track unpaid invoices, monitor recovery status, and record follow-up actions.

---

## Tech Stack

### Frontend
- React
- Axios for API communication
- React Router DOM for routing
- CSS for clean, B2B-style UI design

### Backend
- Python
- Flask
- Flask-SQLAlchemy (ORM)
- Flask-CORS

### Database
- MySQL (Relational Database)

---

## Setup Steps

### step 1: Clone the Repository

git clone <your-github-repo-link>
cd PayAssured-CRM


Step 2: Database Creation

Login to MySQL and create the database:
CREATE DATABASE payassured_db;
This database is used to store client details and invoice recovery cases with proper relational constraints.

Step 3: Backend Setup & Run

Navigate to the backend folder and install dependencies:
cd backend
pip install -r requirements.txt
Create a .env file in the backend directory using the .env.example file as reference.

Step 4: Start the backend server:
python app.py
The backend API will run at:
http://127.0.0.1:5000
All required APIs for client and case management are exposed from this server.

Step 5: Frontend Setup & Run
Navigate to the frontend folder and install dependencies:
cd frontend
npm install


-Start the React development server:
npm start
The frontend application will be available at:
http://localhost:3000

The frontend consumes backend APIs to dynamically display and manage invoice recovery cases.