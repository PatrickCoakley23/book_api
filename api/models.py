from django.db import models

# Create your models here.

class Book(models.Model):

  BOOK_STATUS_CHOICES = (
    ('Unread', ('Unread')),
    ('In Progress', ('In Progress')),
    ('Finished', ('Finished')),
  )

  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  isbn = models.CharField(max_length=200)
  status = models.CharField(
    max_length=30, choices=BOOK_STATUS_CHOICES, default="Unread")
  
  class Meta:
    verbose_name_plural = 'Books'
      
  def __str__(self):
    return self.title