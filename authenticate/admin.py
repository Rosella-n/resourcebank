from django.contrib import admin
from authenticate.models import *

class User_InfoAdmin(admin.ModelAdmin):
    list_display = ('id_numb','first_name','last_name','phone','email',)
    list_per_page = 30
admin.site.register(User_Info,User_InfoAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk','first_name','last_name','phone','email',)
    list_per_page = 30
admin.site.register(User,UserAdmin)