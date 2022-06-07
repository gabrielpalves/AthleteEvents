from wsgiref import validate
from django.db import models
from django.core.exceptions import ValidationError
import datetime

# event_key > 0 (also, age > 0, height > 0, weight > 0)
def isPositive(value):
    if value > 0:
        return value
    else:
        raise ValidationError("This field accepts only integers bigger than zero")

# sex = 'M' or 'F'
def validate_sex(value):
    value = value.upper()
    if value == 'M' or value == 'F':
        return value
    else:
        return ValidationError("Please, type only M (for male) or F (for female)")

# year can't be bigger than this year
def validate_year(value):
    now = datetime.datetime.now()
    thisYear = now.year
    if value > thisYear:
        return ValidationError("You can't predict the future")
    else:
        return value

class Event(models.Model):
    event_key = models.IntegerField(validators=[isPositive]) # unique number for each athlete
    Name = models.CharField(max_length=250)
    Sex = models.CharField(max_length=1, validators=[validate_sex]) # M, F
    Age = models.IntegerField(validators=[isPositive])
    Height = models.IntegerField(validators=[isPositive]) # cm
    Weight = models.IntegerField(validators=[isPositive]) # kg
    Team = models.CharField(max_length=250)
    NOC = models.CharField(max_length=3) # national olympic committee (3-letter code)
    Games = models.CharField(max_length=250) # year and season
    Year = models.IntegerField(validators=[validate_year]) # integer
    Season = models.CharField(max_length=6) # summer or winter
    City = models.CharField(max_length=250)
    Sport = models.CharField(max_length=250)
    Event = models.CharField(max_length=250)
    Medal = models.CharField(max_length=6) # bronze, silver, gold or NA

    def __str__(self):
        return self.Name + ' ' + self.Games + ' ' + self.Event + f'({self.Medal})'*(self.Medal != 'NA')