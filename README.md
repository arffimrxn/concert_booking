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

### ⚙️ Environment Configuration (Crucial Step)

*Because this project follows strict security best practices, the `.env` file containing sensitive credentials is intentionally excluded from version control. You must create a local version to run the application:*

6. **Create a new file named exactly `.env` in the root directory.**
7. **Open the file and add your own Secret Key and Debug setting:**
   ```env
   SECRET_KEY='your-random-secret-key-goes-here'
   DEBUG=True

### 🔒 Database Initialization
*Note: For security and data privacy, the `db.sqlite3` database is excluded from version control. You must initialize your own local database.*

8. **Apply database migrations (builds the database tables):**
   `python manage.py migrate`
9. **Create a local admin account:**
   `python manage.py createsuperuser`
   *(Follow the prompts to set your admin username, email, and password)*

### 🚀 Running the Application

10. **Start the development server:**
   `python manage.py runserver`
11. **Access the application:** 
   Open your browser and navigate to `http://127.0.0.1:8000`. You can log into the admin dashboard at `http://127.0.0.1:8000/admin` to begin adding concert data.

### 🎟️ Managing Concert Data (Admin Panel)

Since the database is newly initialized, the homepage will show "No concerts available" until you add them. To populate your database:

1. Ensure your development server is running (`python manage.py runserver`).
2. Navigate to the admin dashboard at `http://127.0.0.1:8000/admin`.
3. Log in using the superuser credentials.
4. Under the **Concerts** section, click **+ Add**.
5. Fill in the event details:
   * **Concert Title**
   * **Date and Time**
   * **Price (RM)**
   * **Total Tickets Available**
   * **Poster Image** (Upload a custom image)
6. Click **Save**. 

Navigate back to the main homepage (`http://127.0.0.1:8000`) and the newly added concerts will now be displayed

### 🛠️ Development & Troubleshooting (DEBUG Mode)

By default, this application is configured with strict security settings for production. If you clone this repository and find that CSS styles, images, or detailed error pages are missing, it is because the app is running in secure mode.

To enable local development mode:
1. Open your `.env` file.
2. Locate the line: `DEBUG=False`
3. Change it to: `DEBUG=True`
4. Restart your local server (`Ctrl + C`, then `python manage.py runserver`).

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
