## Hotel service
The idea of the project is a hotel system. Users can login and see rooms, their categories and bookings. Also there is a possibility to 
book some room for yourself. Admin can edit users information and see the list of existing hotels in the system.

## How to start
Download the source code and install all requirements as following:
``` 
pip install -r requirements.txt 
```
Migrate changes to the database:
```
python manage.py makemigrations
python manage.py migrate
```
Start the server using the command below:
``` 
python manage.py runserver 
```
Now you can see the application on your localhost.

## How to use
To access to application create superuser using the folloing command (since all user endpoint is not available except admin user):
```
python manage.py createsuperuser
```
After login as admin with credentials provided by you in the previous command, you can create a ordinary user sending POST request
to `users/` (since registration endpoint wasn't required). (Note: hotel is not specified for superuser, so, please, check the api 
using an ordinary user. For admin user it returns all objects from database)

Endpoint for usual login is `api-auth/login/` and for logout `api-auth/logout/`.

The full version of API is available at `/docs/` (all endpoints are complete).
