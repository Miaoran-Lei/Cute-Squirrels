from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class chart(models.Model):
    x_axis = models.FloatField(
        help_text = ('Latitude of the squirrel'), null = True,
        )

    y_axis = models.FloatField(
        help_text = ('Longtitude of the squirrel'), null = True,
        )

    Unique_Squirrel_ID = models.CharField(
        max_length = 100, help_text = ('Unique Squirrel ID'), 
        unique = True, primary_key=True,
        )

    PM, AM = 'PM', 'AM'
    shift_types = ((PM,'PM'), (AM,'AM'))
    shift = models.CharField(
        max_length = 100, help_text = ('Shift in time'), default = '',
        choices = shift_types, null = True,
        )

    date = models.DateField(
        help_text = ('Date'), default='2000-01-01', null = True,
        )

    # The Age of Squirrel
    ADU, JUV = 'Adult', 'Juvenile'
    age_types = ((ADU,'Adult Squirrel'),(JUV,'Juvenile Squirrel'))
    age = models.CharField(
        max_length = 100, help_text = ('Age'), 
        choices = age_types, null = True,
        )

    # The fur color
    GR, CI, BL = 'Gray', 'Cinnamon', 'Black'
    fur_types = ((GR,'Gray'),(CI,'Cinnamon'),(BL,'Black'))
    primary_fur_color = models.CharField(
        max_length = 100, help_text = ('Primary Fur Color'), 
        choices = fur_types, null = True,
        )
    highlight_fur_color = models.CharField(
        max_length = 100, help_text = ('Primary Fur Color'), null = True,
        )

    GP, AG = 'Ground Plane', 'Above Ground'
    location_types = ((GP, 'Ground Plane'), (AG,'Above Ground'))
    location = models.CharField(
        max_length = 100, help_text = ('Location'), 
        choices = location_types, null = True,
        )
    specific_location = models.CharField(
        max_length = 100, help_text = ('Specific location of the squirrel'),
        null = True,
        )

    # Activities of the squirrel
    running = models.BooleanField(
        help_text = ('Is the squirrel running?'), default = False
        )
    chasing = models.BooleanField(
        help_text = ('Is the squirrel chasing?'), default = False
        )
    climbing = models.BooleanField(
        help_text = ('Is the squirrel climbing?'), default = False
        )
    eating = models.BooleanField(
        help_text = ('Is the squirrel eating?'), default = False
        )
    foraging = models.BooleanField(
        help_text = ('Is the squirrel foraging?'), default = False
        )
    other_activities = models.CharField(
        max_length = 100, default = '', null = True, help_text = ('Other Activities'),
        )

    # Other Features
    kuks = models.BooleanField(
        help_text = ('Kuks'), default = False,
        )
    quaas = models.BooleanField(
        help_text = ('Quaas'), default = False,
        )
    tail_flags = models.BooleanField(
        help_text = ('Tail Flags'), default = False,
        )
    tail_twitches = models.BooleanField(
        help_text = ('Tail Twitches'), default = False,
        )

    approaches = models.BooleanField(
        help_text = ('Approaches'), default = False,
        )
    indifferent = models.BooleanField(
        help_text = ('Indifferent'), default = False,
        )
    runs_from = models.BooleanField(
        help_text = ('Runs From?'), default = False,
        ) 
    moans = models.BooleanField(
        help_text= ('Moans'), default = False,
        )

    # Image existence
    profile_image = models.ImageField(
        help_text= ('Profile Image'), upload_to = "img/", null = True,
        )
    have_image = models.BooleanField(
        help_text=('Does this squirrel have an image?'), default = False,
        )   
    

    def __str__(self):

        return self.Unique_Squirrel_ID