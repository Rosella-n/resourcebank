from logging.handlers import RotatingFileHandler
from re import T
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
   rating = models.ForeignKey("QuestionRating",on_delete=models.DO_NOTHING, null=True, blank=True)
   
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
   rating = models.ForeignKey("AnswerRating",on_delete=models.DO_NOTHING, null=True, blank=True)
   file=models.FileField(upload_to='answer_attachment',null=True,blank=True)
  
   class Meta:
        verbose_name = _('Answers')
        verbose_name_plural = _('Answers')
        ordering = ['pk']

   def __str__(self):
        return self.answer


class QuestionRating(models.Model):
     question =models.ForeignKey(Questions,on_delete=models.CASCADE,null=False,blank=False)
     user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
     rated_on= models.DateTimeField(auto_now=True)
     rating=models.PositiveSmallIntegerField(default=0)
     no_of_views= models.PositiveSmallIntegerField(default=0)
     
     class Meta:
        verbose_name = _('Question_Rating')
        verbose_name_plural = _('Question_Ratings')
        ordering = ['pk']

     def __str__(self):
        return self.question


class AnswerRating(models.Model):
     answer =models.ForeignKey(Answers,on_delete=models.CASCADE,null=False,blank=False)
     user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
     rated_on= models.DateTimeField(auto_now=True)
     rating=models.PositiveSmallIntegerField(default=0)
     no_of_views= models.PositiveSmallIntegerField(default=0)
     
     class Meta:
        verbose_name = _('Answer_Rating')
        verbose_name_plural = _('Answer_Ratings')
        ordering = ['pk']

     def __str__(self):
        return self.answer.author.first_name


class Testsave(models.Model):
   suggestion=models.TextField(blank=True, null=True)
   add_file=models.FileField(upload_to='answer_attachment/',null=True,blank=True)
   class Meta:
        verbose_name = _('Testsave')
        verbose_name_plural = _('Testsave')
        ordering = ['pk']

   def __str__(self):
        return self.suggestion



