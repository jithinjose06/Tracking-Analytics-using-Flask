# Tracking Analytics using Flask

This project was done to get familiar with Flask, SQLAlchemy and PostgreSQL.

Tracking Analytics for Music App:

The website contains 3 pages: 
Home - Provides brief description
Download - Contains download button for app
Analytics - Displays number of downloads

Flask is used to render the pages and make app available for download.

SQLAlchemy is used to store a count of downloads in the database.

This data is retrieved from the database and displayed on the Analytics page of the website using jinja.

Note: I'm trying to find a way to store some unique id for each visitor so that the number of visitors can also be tracked.

Instructions to run:

Download the files.

Assumptions: Flask, SQLAlchemy and other dependencies are installed.

1) Open Terminal
2) Type FLASK_RUN=app.py FLASK_DEBUG=true flask run
3) Open browser and enter the port you are using as url. Eg: in this code it is 'localhost:5000'

Note: The webpage layout needs to be improved.

