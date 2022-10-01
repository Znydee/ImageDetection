from django.db import models

class Image(models.Model):
    main_img = models.ImageField()