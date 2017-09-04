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


