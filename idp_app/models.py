from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

# Create your models here.

#Country
class Country(models.Model) :
    name = models.CharField(max_length=128)


    def get_absolute_url(self):
        return reverse('country_detail', args=[str(self.id)])

    def __str__(self) :
        return self.name

#SituationType
class SituationType(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


#Year
class Year(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


#Focal Point
class FocalPoint(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


#Aid Provider -- want to make aid provider many to many
class AidProvider(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name



#Situation
class Situation(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population_estimate = models.IntegerField(null=True)
    focal_point = models.ForeignKey(FocalPoint, on_delete=models.CASCADE)
    situation_type = models.ForeignKey(SituationType, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    aid_provider = models.ManyToManyField(AidProvider)
    description = models.CharField(max_length=2000)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name='comments_owned')

    def __str__(self) :
        return self.name


#Comment
class Comment(models.Model) :
    text = models.TextField(validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")])
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + ' ...'
