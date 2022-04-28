from django.contrib import admin
from resourcebank.models import *
# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('description','created_on','updated_on','author',)
    list_per_page = 30
admin.site.register(Questions,QuestionsAdmin)
