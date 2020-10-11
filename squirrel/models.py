from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Squirrel(models.Model):
    Latitude = models.FloatField(
            help_text=_('Latitude')
            )

    Longitude = models.FloatField(
            help_text=_('Longitude')
            )

    Unique_Squirrel_ID = models.CharField(
            max_length=255,
            help_text=_('Unique Squirrel ID'),
            primary_key=True
            )

    Shift = models.CharField(
            max_length=100,
            help_text=_('Shift')
            )

    Date = models.DateField(
            help_text=_('Date')
            )

    Age = models.CharField(
             max_length = 255,
             help_text=_('Age')
             )

    
    Primary_Fur_Color = models.CharField(
             max_length = 255,
             help_text=_('Primary Fur Color')
             )

    Location = models.CharField(
             max_length = 255,
             help_text=_('Location')
             )

    Specific_Location = models.CharField(
             max_length = 255,
             help_text=_('Specific Location')
             )
     
    Running = models.BooleanField(
            help_text=_("Running")
            )

    Chasing = models.BooleanField(
            help_text=_("Chasing")
            )

    Climbing = models.BooleanField(
            help_text=_("Climbing")
            )

    Eating = models.BooleanField(
            help_text=_("Eating")
            )

    Foraging = models.BooleanField(
            help_text=_("Foraging")
            )

    Other_Activities = models.CharField(
            max_length=255,
            help_text=_("Other Activities")
            )

    Kuks = models.BooleanField(
            help_text=_("Kuks")
            )

    Quaas = models.BooleanField(
            help_text=_("Quaas")
            )

    Moans = models.BooleanField(
            help_text=_("Moans")
            )

    Tail_flags = models.BooleanField(
            help_text=_("Tail flags")
            )
    
    Tail_twitches = models.BooleanField(
            help_text=_("Tail twitches")
            )

    Approaches = models.BooleanField(
            help_text=_("Approaches")
            )
    
    Indifferent = models.BooleanField(
            help_text=_("Indifferent")
            )


    Runs_from = models.BooleanField(
            help_text=_("Runs from")
            )


    def __str__(self):
        return self.Unique_Squirrel_ID


