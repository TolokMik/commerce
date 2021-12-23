from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.html import format_html


def custom_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return filename

class User(AbstractUser):
    users_photo = models.ImageField()

def custom_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return filename    

#----------------------------------------
class Staff(models.Model):
    staffname = models.CharField(max_length = 64)
    image_one = models.ImageField(upload_to='staff/', default='F-208_H.png', blank=True,null=True)
    staff_descript = models.TextField()
    startprice = models.FloatField(null = True, blank=True)
    staff_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    def __str__(self):
        return f"{self.staffname} | {self.startprice} | {self.staff_owner}"

    def image_data(self):
        return format_html(
            '<img src="media/{}" width="100%"/>',
           self.image_one,
        )
    
#--------------------------------------
class Propositions(models.Model):
    person_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name="person")
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="staff")
    price = models.FloatField()



