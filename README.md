# Squirrel Tracker Readme

### Background & Introduction: 
Eccentric billionaire Joffrey Hosencratz would like to start keeping track of all the known squirrels and plans to start with Central Park in order to avoid running in to squirrels. Therefore, this app is used to track and maintain relevant information about squirrels in Central Park, where you can import the 2018 Central Park Squirrel Census data and allow to add, update, and view squirrel data.   
 
### Dataset
The Squirrel Census dataset contains squirrel data for each of the 3,023 sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans. 

### Implementation
The application is based on Django.
 
### Import and export data
Management commands:  
Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.   
$ python manage.py import_squirrel_data /path/to/file.csv  
	The squirrel census file can be downloaded here:   
https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv  

Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.   
$ python manage.py export_squirrel_data /path/to/file.csv.  

### Squirrel Map
This is a view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.  
Located at: /map  
Methods Supported: GET  
Uses the https://leafletjs.com/ library for plotting  
Please note: Your browser will start to freeze if you plot more than 100 points at once. The app will only show the first 100 squirrels in the listing.  

### Squirrel Sightings List
This is the page that lists all squirrel sightings with links to view and edit each sighting as well as the link to view stats of squirrels and the link to add squirrels  	
Located at: /sightings  
Methods Supported: GET  
Fields to show:  
- Unique Squirrel ID  
- Date  
- Link to unique squirrel sighting to edit the squirrel  
- Link to the “add” sighting view  
- Link to show the stats of the squirrels  

### A view to update a particular sighting
The url is Located at: /sightings/<unique-squirrel-id>  
Methods Supported: GET & POST  
It allows you to update Latitude, Longitude, Unique Squirrel ID, Shift, Date and Age.  

### A view to create a new sighting
Located at: /sightings/add  
Methods Supported: GET & POST  
It allows you to add new sighting with all fields listed in the form.  

### A view with general stats about the sightings
It shows the 
Located at: /sightings/stats
Method: GET
Stats to show:  
- Count of all squirrels  
- Average of lattitude  
- Average of longitude  
- Ratio of squirrels (AM vs PM)  
- Percentage % of squirrels (Running)  

### Contributors
Group Name: Team Q&L  

Section: 001  

Contributors: Xintong Qiang, Minyue Liu  

UNIs: [xq2212, ml4368]  













