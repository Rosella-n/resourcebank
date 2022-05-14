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
   no_view=models.PositiveSmallIntegerField(default=0)
   rating=models.SmallIntegerField(default=0)
   class Meta:
        verbose_name = _('Questions')
        verbose_name_plural = _('Questions')
        ordering = ['pk']

   def __str__(self):
        return self.description

class Answers(models.Model):
   answer = models.TextField(blank=False, null=False)
   created_on = models.DateTimeField(auto_now_add=True)
   updated_on= models.DateTimeField(auto_now=True)
   question=models.ForeignKey(Questions,on_delete=models.CASCADE,null=False,blank=False)
   author= models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False)
   no_view=models.PositiveSmallIntegerField(default=0)
   rating=models.SmallIntegerField(default=0)
   class Meta:
        verbose_name = _('Answers')
        verbose_name_plural = _('Answers')
        ordering = ['pk']

   def __str__(self):
        return self.answer
