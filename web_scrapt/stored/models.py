from django.db import models

# Create your models here.
class Web_data(models.Model):
    business_name = models.CharField(max_length=355)
    web_url = models.URLField()
    category = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        db_table = "grayquest_web_data"

