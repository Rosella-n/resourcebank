from django.conf import settings
import datetime
import magic
import os,os.path
from django.core.exceptions import ValidationError
import sweetify

def pdfvalidator(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_mime_types = ['application/pdf']
    file_mime_type = magic.from_buffer(value.read(1024), mime=True)
    valid_file_extensions = ['.pdf']
    ext = os.path.splitext(value.name)[1]
    filesize = value.size
    print (filesize)
    megabyte_limit = 0.25
    

    if file_mime_type not in valid_mime_types:
        
        er_msg1='Unsupported File Type'
        er_msg2='Sorry, The File You Selected Is Not A PDF File'
        print(er_msg2)
        raise ValidationError(er_msg2)
                    
    
    elif ext.lower() not in valid_file_extensions:
        
        er_msg3='Wrong File Extension'
        er_msg4='Sorry, you must provide a file with PDF Extension'   
        print(er_msg2)
        raise ValidationError(er_msg4)
    
    elif filesize > megabyte_limit*1024*1024:
            print("please check file size")
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

def imagevalidator(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_mime_types = ['image/png','image/jpeg']
    file_mime_type = magic.from_buffer(value.read(1024), mime=True)
    valid_file_extensions = ['.png','.jpeg', '.jpg']
    ext = os.path.splitext(value.name)[1]
    filesize = value.size
    megabyte_limit = 0.5
    

    if file_mime_type not in valid_mime_types:
        
        er_msg1='Unsupported File Type'
        er_msg2='Sorry, The File You Selected Is Not A Valid Image File'
        
        raise ValidationError(er_msg2)
                    
    
    elif ext.lower() not in valid_file_extensions:
        
        er_msg3='Wrong File Extension'
        er_msg4='Sorry, you must provide a file with Image Extension'   
        raise ValidationError(er_msg4)
    
    elif filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))