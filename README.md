# Squirrel Tracker Readme

### Background & Introduction: 
Eccentric billionaire Joffrey Hosencratz would like to start keeping track of all the known squirrels and plans to start with Central Park in order to avoid running in to squirrels. Therefore, this app is used to track and maintain relevant information about squirrels in Central Park, where you can import the 2018 Central Park Squirrel Census data and allow to add, update, and view squirrel data. 
 
 ### Dataset
 The Squirrel Census dataset contains squirrel data for each of the 3,023 sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans.
 
 ### Import and export data
 Management commands:
Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 
$ python manage.py import_squirrel_data /path/to/file.csv
	The squirrel census file can be downloaded here: 
https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv

Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 
$ python manage.py export_squirrel_data /path/to/file.csv.





