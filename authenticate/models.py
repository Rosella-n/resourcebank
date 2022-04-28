import os
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db.models.deletion import DO_NOTHING
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.dispatch import receiver
now = timezone.now()
from storage import OverwriteStorage
from django.conf import settings
from django.db.models.signals import post_save,post_delete


from rest_framework.authtoken.models import Token

import shortuuid
from django.core.validators import MinValueValidator
from validators import (pdfvalidator,imagevalidator)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created=False,  **kwargs):
    
    if created:
        Token.objects.create(user=instance)
# @receiver(post_delete, sender='authenticate.Staff_Academic_Qualifications')
# def auto_delete_degree_file_on_delete(sender, instance, **kwargs):

#         """
#         Deletes file from filesystem
#         when corresponding `MediaFile` object is deleted.
#         """
#         if instance.scanned_doc:
#             if os.path.isfile(instance.scanned_doc.path):
#                 (instance.scanned_doc.close())
#                 os.remove(instance.scanned_doc.path)   

# # @receiver(post_delete, sender='authenticate.Scanned_Documents')
# # def auto_delete_file_on_delete(sender, instance, **kwargs):

# #         """
# #         Deletes file from filesystem
# #         when corresponding `MediaFile` object is deleted.
# #         """
# #         if instance.pdf_file:
# #             if os.path.isfile(instance.pdf_file.path):
# #                 (instance.pdf_file.close())
# #                 os.remove(instance.pdf_file.path) 


class Faculty(models.Model):
    name = models.CharField(max_length=50,)

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')
        ordering = ['pk']

    def __str__(self):
        return self.name





class Department (models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,null=False, blank=False)

    class Meta:

        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['pk']

    def __str__(self):
        return self.short_name


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def create_user(self, id_numb, password):
        id_numb=User_Info.objects.get(id_numb=id_numb)
        user = self.model(id_numb=id_numb, password=password)
        user.set_password(password)
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False
        user.last_login = now
        user.save(using=self._db)
        return user

    def create_superuser(self, email, id_numb, password):
            user = self.create_user(
                 id_numb=id_numb, password=password)
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.email=email
            user.last_login = now
            user.save(using=self._db)
            return user
# def user_profile_pics_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/profile_pictures/user_<id>/<filename>
#     return 'profile_pictures/user_{0}/{1}'.format(instance.staff_id, filename)

class User(AbstractUser):
    """User model."""
    
    id_numb = models.ForeignKey('User_Info', models.CASCADE,null=True,blank=True, related_name='idnumber')
    
    
    display_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=15, blank=True,
                             null=True, unique=False)
    # profile_pic = models.ImageField(storage=OverwriteStorage(
    # ), upload_to=user_profile_pics_path, blank=True, null=True)
    my_last_login = models.DateTimeField(blank=True, null=True,)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id_numb', ]

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['pk']

    def __str__(self):
        # return self.display_name
        return('%s %s' % (self.first_name, self.last_name)).strip()
        
        # return user.display_name

    def get_staff_id(self):
        '''
        Returns the staff_id
        '''
        return self.staff_id

    # def get_full_name(self):
    #     '''
    #     Returns the first_name plus the last_name, with a space in between.
    #     '''
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     '''
    #     Returns the short name for the user.
    #     '''
    #     return self.first_name
    
    # def get_profile_picture(self):
    #     if self.nominal_roll.profile_pic:
    #         return self.nominal_roll.profile_pic.url
    #     else:
    #         return '/static/images/black_avatar.jpg'    

class User_Info(models.Model):
    id_numb = models.CharField(unique=True,primary_key=True, max_length=50)
    state = models.ForeignKey('State',on_delete=models.DO_NOTHING,null=True, blank=True)
    local_government = models.ForeignKey('Local_Government',on_delete=models.DO_NOTHING,null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_student = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True,
                             null=True, unique=False)   
    email= models.EmailField(unique=True,null=True,blank=True)

    class Meta:
        verbose_name = _('User Info')
        verbose_name_plural = _('User Info')
        ordering = ['pk']

    def __str__(self):
        return('%s %s' % (self.first_name, self.last_name)).strip()

class Country(models.Model):
    name = models.CharField(max_length=100, blank=True,
                            null=True, unique=False)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ['pk']

    def __str__(self):
        return self.name
class GPZ(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Geopolitical Zone')
        verbose_name_plural = _('Geopolitical Zones')
        ordering = ['pk']

    def __str__(self):
        return self.name   

class State(models.Model):
    code = models.PositiveIntegerField(primary_key=True)
    country = models.ForeignKey(
        Country, on_delete=models.DO_NOTHING, blank=False, null=False, unique=False)
    name = models.CharField(max_length=100, blank=True,
                            null=True, unique=False)

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        ordering = ['pk']

    def __str__(self):
        return self.name


class Local_Government(models.Model):
    state = models.ForeignKey(
        State, on_delete=models.SET_NULL, blank=True, null=True, unique=False)
    name = models.CharField(max_length=100, blank=True,
                            null=True, unique=False)

    class Meta:
        verbose_name = _('Local Government')
        verbose_name_plural = _('Local Governments')
        ordering = ['pk']

    def __str__(self):
        return self.name


# class Questions(models.Model):
#    description = models.TextField(blank=False, null=False)
#    created_on = models.DateTimeField(auto_now_add=True)
#    updated_on= models.DateField(auto_now=True)

#    class Meta:
#         verbose_name = _('Questions')
#         verbose_name_plural = _('Questions')
#         ordering = ['pk']

#    def __str__(self):
#         return self.description
