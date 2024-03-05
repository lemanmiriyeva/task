from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    father_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    send_type=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    email=models.EmailField()
    message=models.TextField()
    file=models.FileField(upload_to="files/")

    def __str__(self):
        return self.name