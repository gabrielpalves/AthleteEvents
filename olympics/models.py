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
    event_key = models.IntegerField(validators=[isPositive]) # event key
    name = models.CharField(max_length=250)
    sex = models.CharField(max_length=1, validators=[validate_sex]) # M, F
    age = models.IntegerField(validators=[isPositive])
    height = models.IntegerField(validators=[isPositive])
    weight = models.IntegerField(validators=[isPositive])
    team = models.CharField(max_length=250)
    noc = models.CharField(max_length=3)
    games = models.CharField(max_length=250)
    year = models.IntegerField(validators=[validate_year])
    season = models.CharField(max_length=6) # summer, winter, spring, fall
    city = models.CharField(max_length=250)
    sport = models.CharField(max_length=250)
    event = models.CharField(max_length=250)
    medal = models.CharField(max_length=6) # bronze, silver, gold

    def __str__(self):
        return self.name + ' ' + self.games + ' ' + self.event