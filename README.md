Django Blog Project
===================

Overview:
---------
This is a full-featured Django-based blog web application with the following core features:
- User Registration, Login, Logout
- Create, Read, Update, Delete (CRUD) blog posts
- Upload and display images with posts
- Categorize posts using a dynamic category model
- User Profile page with personal posts
- Responsive UI using Bootstrap 5
- CSRF protection and secure form handling

Technology Stack:
-----------------
- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap 5
- Database: SQLite (default Django DB)
- Version Control: Git
- Hosting-ready (can be deployed on platforms like Heroku, Vercel, or AWS)

'''Folder Structure:
-----------------
project/
├── blog/                  # Main Django app
│   ├── models.py          # Post and Category models
│   ├── views.py           # All view logic
│   ├── forms.py           # PostForm and SignupForm
│   ├── urls.py            # App-specific URL patterns
│   ├── templates/blog/    # All HTML templates
│   └── static/            # Static files (optional)
├── media/                 # Uploaded post images
├── project_name/          # Django project settings
├── db.sqlite3             # Default database
└── manage.py              # Django project manager'''

How to Run:
------------
1. Clone the repository:
   git clone https://github.com/your-username/django-blog-project.git

2. Navigate into the project:
   cd django-blog-project

3. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  (Linux/macOS)
   venv\Scripts\activate     (Windows)

4. Install dependencies:
   pip install -r requirements.txt

5. Apply migrations:
   python manage.py migrate

6. Run the development server:
   python manage.py runserver

7. Visit http://127.0.0.1:8000 in your browser to use the blog.

Admin Access (Optional):
------------------------
1. Create a superuser:
   python manage.py createsuperuser

2. Log in to the admin panel at:
   http://127.0.0.1:8000/admin

Features Summary:
-----------------
- Clean, user-friendly Bootstrap layout
- Fully working user authentication system
- Dynamic post creation with category and image
- Profile view showing posts by user
- Validation for empty fields and proper error messages
- Secure login/logout and CSRF tokens on forms

Deployment:
-----------
This app can be deployed to any platform that supports Django. Use tools like Docker, Gunicorn, and Nginx for production deployment.

Credits:
--------
Developed using Django by Gaurav Takalkar.
Feel free to fork and customize.

License:
--------
Open-source for learning purposes.
