import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Sight

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        
        def str_to_boolean(str_):
            text1 = str_.upper()
            if text1 == 'FALSE': 
                str_ = False
            elif text1 == 'TRUE':
                str_ = True
            else:
                str_ = None
            return str_

        for item in data:
            s = Sight(
                    Longitude = item['X'],
                    Latitude = item['Y'],
                    Unique_Squirrel_Id = item['Unique Squirrel ID'],
                    Shift = item['Shift'],
                    Date = datetime.datetime.strptime(item['Date'],'%m%d%Y'),
                    Age = item['Age'],
                    Primary_Fur_Color = item['Primary Fur Color'],
                    Location = item['Location'],
                    Specific_Location = item['Specific Location'],
                    Running = str_to_boolean(item['Running']),
                    Chasing = str_to_boolean(item['Chasing']),
                    Climbing = str_to_boolean(item['Climbing']),
                    Eating = str_to_boolean(item['Eating']),
                    Foraging = str_to_boolean(item['Foraging']),
                    Other_Activities = item['Other Activities'],
                    Kuks = str_to_boolean(item['Kuks']),
                    Quaas = str_to_boolean(item['Quaas']),
                    Moans = str_to_boolean(item['Moans']),
                    Tail_Flags = str_to_boolean(item['Tail flags']),
                    Tail_Twitches = str_to_boolean(item['Tail twitches']),
                    Approaches = str_to_boolean(item['Approaches']),
                    Indifferent = str_to_boolean(item['Indifferent']),
                    Runs_From = str_to_boolean(item['Runs from']),
                    )
            s.save()