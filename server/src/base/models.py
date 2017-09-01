from django.db import models


def products_image_locations(instance, filename):
    return "products/%s" % (filename)


class Product(models.Model):
    """
    all the products info
    """
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    slug = models.CharField(max_length=30)
    imageSrc = models.ImageField(
        upload_to=products_image_locations,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)


    button_text = models.CharField(max_length=30)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]


# ========================================

# class Person(models.Model):
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name

# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')

#     def __str__(self):
#         return self.name

# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)