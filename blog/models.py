from django.db import models

# Create your models here.
class Contact(models.Model):
    serialno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=600)
    message = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email

class Post(models.Model):
    title = models.CharField(max_length=600)
    author = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    category = models.CharField(max_length=200)
    slug = models.CharField(max_length=800)
    body = models.TextField()
    dt = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title + ' by ' + self.author