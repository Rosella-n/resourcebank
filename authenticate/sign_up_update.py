import email
from authenticate.models import(User_Info,User,)
from django.utils import timezone



now = timezone.now()
def update_new_user_details(request,id_numb):
    user_details=User_Info.objects.all().filter(id_numb=id_numb)
    for u in User_Info.objects.all().filter(id_numb=id_numb):
        user_id=u.id_numb
        first_name=u.first_name
        middle_name=u.middle_name
        last_name=u.last_name
        useremail=u.email
       
        full_name='{} {}'.format(first_name,last_name)       
       
        User.objects.filter(pk=id_numb).update(
        first_name=first_name,last_name=last_name,middle_name=middle_name,display_name=\
        full_name,email=useremail,)
        
