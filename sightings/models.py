from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Squirrel(models.Model):
    Latitude = models.FloatField(
            help_text=_('Latitude'),
            null = False,
            blank = False
            )

    Longitude = models.FloatField(
            help_text=_('Longitude'),
            null = False,
            blank = False
            )

    Unique_Squirrel_ID = models.CharField(
            max_length=255,
            help_text=_('Unique Squirrel ID'),
            primary_key=True,
            null = False,
            blank = False
            )

    Shift = models.CharField(
            max_length=100,
            help_text=_('Shift'),
            null = True,
            blank = True
            )

    Date = models.DateField(
            help_text=_('Date'),
            null = True,
            blank = True
            )

    Age = models.CharField(
             max_length = 255,
             help_text=_('Age'),
             null = True,
             blank = True
             )

    
    Primary_Fur_Color = models.CharField(
             max_length = 255,
             help_text=_('Primary Fur Color'),
             null = True,
             blank = True
             )

    Location = models.CharField(
             max_length = 255,
             help_text=_('Location'),
             null = True,
             blank = True
             )

    Specific_Location = models.CharField(
             max_length = 255,
             help_text=_('Specific Location'),
             null = True,
             blank = True
             )
     
    Running = models.BooleanField(
            help_text=_("Running"),
            null = True,
            blank = True
            )

    Chasing = models.BooleanField(
            help_text=_("Chasing"),
            null = True,
            blank = True
            )

    Climbing = models.BooleanField(
            help_text=_("Climbing"),
            null = True,
            blank = True
            )

    Eating = models.BooleanField(
            help_text=_("Eating"),
            null = True,
            blank = True
            )

    Foraging = models.BooleanField(
            help_text=_("Foraging"),
            null = True,
            blank = True
            )

    Other_Activities = models.CharField(
            max_length=255,
            help_text=_("Other Activities"),
            null = True,
            blank = True
            )

    Kuks = models.BooleanField(
            help_text=_("Kuks"),
            null = True,
            blank = True
            )

    Quaas = models.BooleanField(
            help_text=_("Quaas"),
            null = True,
            blank = True
            )

    Moans = models.BooleanField(
            help_text=_("Moans"),
            null = True,
            blank = True
            )

    Tail_flags = models.BooleanField(
            help_text=_("Tail flags"),
            null = True,
            blank = True
            )
    
    Tail_twitches = models.BooleanField(
            help_text=_("Tail twitches"),
            null = True,
            blank = True
            )

    Approaches = models.BooleanField(
            help_text=_("Approaches"),
            null = True,
            blank = True
            )
    
    Indifferent = models.BooleanField(
            help_text=_("Indifferent"),
            null = True,
            blank = True
            )


    Runs_from = models.BooleanField(
            help_text=_("Runs from"),
            null = True,
            blank = True
            )


    def __str__(self):
        return self.Unique_Squirrel_ID


