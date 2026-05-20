# Secure Concert Booking System

## 1. Project Description
A secure, web-based concert booking application built with Django. This platform allows users to view upcoming events, register for accounts, and book tickets while enforcing strict security protocols and Role-Based Access Control (RBAC).

## 2. Installation Steps
1. Clone the repository: `git clone https://github.com/arffimrxn/concert_booking.git`
2. Navigate into the directory: `cd concert_booking`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Create a local `.env` file based on `.env.example` and add your secret key.
6. Apply database migrations: `python manage.py migrate`

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
- Django 6.0.5 (or your specific version)
- SQLite3 (Default local database)

## 6. System Screenshots
<img width="1246" height="1123" alt="image" src="https://github.com/user-attachments/assets/0ac25401-8518-4da2-a20a-d29609bc92c7" />
