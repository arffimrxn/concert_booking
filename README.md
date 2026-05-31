# Secure Concert Booking System

## 1. Project Description
A secure, web-based concert booking application built with Django. This platform allows users to view upcoming events, register for accounts, and book tickets while enforcing strict security protocols and Role-Based Access Control (RBAC).

## 2. Installation Steps

To set up this project locally, follow these steps:

1. **Clone the repository:** 
   `git clone https://github.com/arffimrxn/concert_booking.git`
2. **Navigate into the directory:** 
   `cd concert_booking`
3. **Create a virtual environment:** 
   `python -m venv venv`
4. **Activate the virtual environment:**
   * Windows: `venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`
5. **Install dependencies:**
   `pip install -r requirements.txt`

### 🔒 Database Initialization
*Note: For security and data privacy, the `db.sqlite3` database is excluded from version control. You must initialize your own local database.*

6. **Apply database migrations (builds the database tables):**
   `python manage.py migrate`
7. **Create a local admin account:**
   `python manage.py createsuperuser`
   *(Follow the prompts to set your admin username, email, and password)*

### 🚀 Running the Application

8. **Start the development server:**
   `python manage.py runserver`
9. **Access the application:** 
   Open your browser and navigate to `http://127.0.0.1:8000`. You can log into the admin dashboard at `http://127.0.0.1:8000/admin` to begin adding concert data.


## 3. Security Features Summary
- **Environment Isolation:** Sensitive credentials stored in `.env` and excluded via `.gitignore`.
- **Authentication & RBAC:** Enforced user sessions and `@login_required` decorators for booking and profiles.
- **Input Validation:** Server-side integer casting and boundary checks for ticket quantities.
- **CSRF Protection:** Anti-CSRF tokens applied to all state-changing POST requests (Booking, Logout).
- **Error Handling:** Production mode (`DEBUG=False`) activated to suppress sensitive stack traces.

## 4. How to Run the App
Run the local development server using the following command:
`python manage.py runserver`
Then, open a web browser and navigate to `http://127.0.0.1:8000`.

## 5. Dependencies
- Python 3.14.5
- Django 6.0.5 
- SQLite3 (Default local database)

## 6. System Screenshots
<img width="1246" height="1123" alt="image" src="https://github.com/user-attachments/assets/0ac25401-8518-4da2-a20a-d29609bc92c7" />
<img width="1229" height="1122" alt="image" src="https://github.com/user-attachments/assets/75a53655-4393-4ffc-9dd6-99e849424e01" />
<img width="1192" height="714" alt="image" src="https://github.com/user-attachments/assets/ed41debb-57f5-48cb-868e-f0c15c559a57" />
