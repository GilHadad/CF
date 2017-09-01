from django.db import models


vv_priority = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
    )
vv_status =(
    ('1','Defined'),
    ('2','In progress'),
    ('3','Done'),
    ('4','Accepted'),
    ('5','Blocking')
    )


class Project(models.Model):
    """docstring for ClassName"""

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    status=models.CharField(max_length=1, choices=vv_status)
    # Owner=
    prioirity= models.CharField(max_length=1, choices=vv_priority)
    men_hours= models.FloatField (default=0)
    income= models.FloatField(default=0)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ["-id"]






class Task(models.Model):
    """docstring for ClassName"""


    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    status=models.CharField(max_length=1, choices=vv_status)
    # Owner=
    # Project=
    prioirity= models.CharField(max_length=1, choices=vv_priority)
    men_hours= models.FloatField (default=0)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ["-id"]








    # slug = models.CharField(max_length=30)
    # imageSrc = models.ImageField(
    #     upload_to=products_image_locations,
    #     null=True,
    #     blank=True,
    #     width_field="width_field",
    #     height_field="height_field")
    # width_field = models.IntegerField(default=0)
    # height_field = models.IntegerField(default=0)


    # button_text = models.CharField(max_length=30)

    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)
    # active = models.BooleanField(default=True)

    # class Meta:
    #     ordering = ["id"]

# Create your models here.
