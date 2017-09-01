from django.db import models
from django.contrib.auth.models import User

def company_logo_locations(instance, filename):
    return "company_logo/%s" % (filename)

class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_at = models.DateTimeField(null=True, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    
    active = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated 	= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
 
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class TeamSubscriber(models.Model):
    team 	= models.ForeignKey(Team, related_name='TeamSubscriber')
    subscriber 	= models.ForeignKey(Subscriber, related_name='TeamSubscriber')
    job_title = models.CharField(max_length=200, null=True, blank=True)
    manager =  models.BooleanField(default=False)

    active = models.BooleanField(default=True)
    timestamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated 	= models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        ordering = ["-team", "-subscriber"]
        unique_together = (("team", "subscriber"),)

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo_image = models.ImageField(
        upload_to=company_logo_locations,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    width_field = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name

    def TeamNamesValidation(self):
      pass

    def SubscriberNamesValidation(self):
      pass

class TeamTree(models.Model):
    parent 	= models.ForeignKey(Team, related_name='ParentTeam')
    child 	= models.ForeignKey(Team, related_name='ChildTeam')

    active = models.BooleanField(default=True)
    timestamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated 	= models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ["-parent"]
        unique_together = (("parent", "child"),)

class CompanySubscriber(models.Model):
    company = models.ForeignKey(Company, related_name='CompanySubscriber')
    subscriber = models.ForeignKey(Subscriber, related_name='CompanySubscriber')

    active = models.BooleanField(default=True)
    timestamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated 	= models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ["-company"]
        unique_together = (("company", "subscriber"),)

class CompanyTeam(models.Model):
    company = models.ForeignKey(Company, related_name='CompanyTeam')
    team = models.ForeignKey(Team, related_name='CompanyTeam')

    active = models.BooleanField(default=True)
    timestamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated 	= models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        ordering = ["-company"]
        unique_together = (("company", "team"),)