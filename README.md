# To_Do_Backend

## Project overview

This a ToDo mobile application backend, built using Flask as backend framework and Postgresql as DBMS. You can create,
edit, delete and get todo items. To run this project, you must have installed Postgresql client + server on your
machine. I won't explain here how to install it, you will be fine after watching a YouTube tutorial. The files wsgi.py,
Procfile are necessary to deploy your app on Heroku for example, if you are working locally, you can remove them.
 
## Database migration

These are the commands that you will need in case you want to add new tables or any changes to the database.

- flask db init
- flask migrate -m "migration message"
- flask db upgrade
