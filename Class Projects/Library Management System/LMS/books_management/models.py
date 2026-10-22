from django.db import models

# Create your models here.
class BooksModel(models.Model):
    bname = models.CharField(max_length=30)
    author = models.CharField(max_length=15)
    genre = models.CharField(max_length=15)
    avail = models.BooleanField(default=False)

    def __str__(self):
        return self.bname


    