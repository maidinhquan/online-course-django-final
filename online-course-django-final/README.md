# OnlineCourse – Django Assessment Final Project

This is a standalone demonstration of the IBM Online Course assessment lab, including `Question`, `Choice`, and `Submission`; Django Admin customization; Bootstrap course and exam templates; exam submission and scoring routes. It is **not a copy of the original IBM starter repository**.

## Windows PowerShell

```powershell
cd online-course-django-final
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations onlinecourse
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/` and sign in as the superuser. Take a real screenshot showing Authentication and Authorization and OnlineCourse, saved as `03-admin-site.png`.

Open `http://127.0.0.1:8000/` and select Introduction to Python. The exam requires login; log in via `/admin/` first using your superuser, then return to the course. Submit the correct answers `def`, `int`, `==`. The result page should show `Congratulations!`, `Score: 100%`, and individual answers; take a screenshot saved `07-final.png`.

## Publishing

Create a **public** GitHub repository `online-course-django-final`, then from this folder run:

```powershell
git init
git add .
git commit -m "Implement Django OnlineCourse assessments"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/online-course-django-final.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. Keep files at repository root. Task URLs:

- `https://github.com/YOUR_USERNAME/online-course-django-final/blob/main/onlinecourse/models.py`
- `https://github.com/YOUR_USERNAME/online-course-django-final/blob/main/onlinecourse/admin.py`
- `https://github.com/YOUR_USERNAME/online-course-django-final/blob/main/onlinecourse/templates/onlinecourse/course_details_bootstrap.html`
- `https://github.com/YOUR_USERNAME/online-course-django-final/blob/main/onlinecourse/views.py`
- `https://github.com/YOUR_USERNAME/online-course-django-final/blob/main/onlinecourse/urls.py`

If the assignment uses IBM's existing starter project, integrate these changes there instead of presenting this independent example as an IBM fork.
