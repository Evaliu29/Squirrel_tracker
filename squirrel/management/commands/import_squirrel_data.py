from django.core.management.base import BaseCommand
from squirrel.models import Squirrel
import csv
import datetime

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path',type=str,help='csv file')    


    def handle(self,path,**options):
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dt = row['Date']
                d = datetime.date(int(dt[4:]),int(dt[:2]),int(dt[2:4]))
                s = Squirrel(Latitude=row['X'],
                    Longitude=row['Y'],
                    Unique_Squirrel_ID=row['Unique Squirrel ID'],
                    Shift=row['Shift'],
                    Date=d,Age=row['Age'],
                    Primary_Fur_Color=row['Primary Fur Color'],
                    Location=row['Location'],
                    Specific_Location=row['Specific Location'],
                    Running=True if row['Running'].upper()=='TRUE' else False,
                    Chasing=True if row['Chasing'].upper()=='TRUE' else False,
                    Climbing=True if row['Climbing'].upper()=='TRUE' else False,
                    Eating=True if row['Eating'].upper()=='TRUE' else False,
                    Foraging=True if row['Foraging'].upper()=='TRUE' else False,
                    Other_Activities=row['Other Activities'],
                    Kuks=True if row['Kuks'].upper()=='TRUE' else False,
                    Quaas=True if row['Quaas'].upper()=='TRUE' else False,
                    Moans=True if row['Moans'].upper()=='TRUE' else False,
                    Tail_flags=True if row['Tail flags'].upper()=='TRUE' else False,
                    Tail_twitches=True if row['Tail twitches'].upper()=='TRUE' else False,
                    Approaches=True if row['Approaches'].upper()=='TRUE' else False,
                    Indifferent=True if row['Indifferent'].upper()=='TRUE' else False,
                    Runs_from=True if row['Runs from'].upper()=='TRUE' else False)
                s.save()
