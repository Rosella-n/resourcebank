from tkinter import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.db import models
from authenticate.models import User
# Create your models here.

class Questions(models.Model):
   description = models.TextField(blank=False, null=False)
   created_on = models.DateTimeField(auto_now_add=True)
   updated_on= models.DateTimeField(auto_now=True)
   author= models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False)
   class Meta:
        verbose_name = _('Questions')
        verbose_name_plural = _('Questions')
        ordering = ['pk']

   def __str__(self):
        return self.description
