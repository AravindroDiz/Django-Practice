from django.db import models

class Employers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone_no = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
