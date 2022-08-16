To be able to run the app:

1. In terminal run:
  sqlite3 db/travel_manager.db < db/travel_manager.sql
  
  then:
  python3 console.py

2. In terminal again: to access on local host:
  -flask run

Reminder: 
- to exit pdb: q
- to exit flask ctrl c


Brief:

Travel Bucket List
Build an app to track someone's travel adventures.

MVP:
The app should allow the user to track countries and cities they want to visit and those they have visited.
The user should be able to create and edit countries
Each country should have one or more cities to visit
The user should be able to create and delete entries for cities
The app should allow the user to mark destinations as visited or still to see

extensions completed:

added sights to the cities
able to add/update/delete sights

Technologies used:
Python
Flask
Sqlite3
HTML
CSS



