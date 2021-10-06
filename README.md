# To_Do_Backend
## Project overview
This a ToDo mobile application backend, built using 
Flask as backend framework and Postgresql as DBMS.
It is deployed on Heroku.


## Database migration
These are the commands that will need in case if you
want to add new tables to the database.
- flask db init
- flask migrate -m "migration message"
- flask db upgrade
