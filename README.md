# Code Institute Hello Django Lessons

## Gettign Set Up
1. Use the CI Gitpod Template to create new repo.
2. Launch the Gitpod Workspace for new repo.
3. Install Django from CLI: `pip3 install django`
4. Create new project with Django from CLI: `django-admin startproject <project_name> .`
5. Run the prject from CLI: `python3 manage.py runserver`

    End of unit

## URLs
1. Create apps on the project from CLI: `python3 manage.py startapp <app_name>`
2. On your app directory, under views.py, create the http view.
3. Make views.py functions available to the browser on urls.py using path function.

### Templates
1. Create the directory "templates", then "<app_name>" to hold your HTML templates within the app directory.
2. Update the views to get the template with render(request, '<template_name>').
3. On settings.py, include the created app as installed app.

### Migrations and admin
1. Run on the CLI: `python manage.py migrate`. Do this initially for default database setup.
2. Create admin user from CLI: `python3 manage.py createsuperuser`
3. Enter username, email (optional) and password.
4. To login in, run the app and navigate to url /admin.