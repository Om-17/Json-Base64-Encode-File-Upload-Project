import base64
import binascii
from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import Base64FileField,Base64ImageField
from django.core.files.uploadedfile import SimpleUploadedFile

import filetype
from django.core.exceptions import ValidationError
class CustomBase64FileField(Base64FileField):
    ALL_MIME_TYPES = {
    'image/jpeg': 'jpg',
    'text/plain': 'txt',
    'image/png': 'png',
    'application/pdf': 'pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
    'application/msword': 'doc',
    'application/vnd.ms-excel': 'xls',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'xlsx',
    'application/vnd.ms-powerpoint': 'ppt',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'pptx',
    'text/csv': 'csv',
    'image/gif': 'gif',
    'image/webp': 'webp',
    'audio/mpeg': 'mp3',
    'video/mp4': 'mp4',
    'application/zip': 'zip',
    'application/x-7z-compressed': '7z',
  
}
    
    ALLOWED_TYPES = ['pdf','txt', 'docx', 'jpg', 'jpeg', 'png']

    def __init__(self, *args, **kwargs):
       
        self.allow_type = kwargs.pop('allow_type', self.ALLOWED_TYPES)
         
        super().__init__(*args, **kwargs) 
    def get_file_extension(self, filename, decoded_file):
       return filename.split('.')[-1].lower()
   
    def to_internal_value(self, base64_data):
        if base64_data in self.EMPTY_VALUES:
            return None

        if isinstance(base64_data, str):
            file_mime_type = None
            file_name=None
            # Strip base64 header, get mime_type from base64 header.
            if ";base64," in base64_data:
                header, base64_data = base64_data.split(";base64,")
                typedata,name=header.split(",")
                if name:
                    file_name=name.replace("name:","")
                file_mime_type = typedata.replace("data:", "")
            try:
                decoded_file = base64.b64decode(base64_data)
                # print("decoded_file",decoded_file)
            except (TypeError, binascii.Error, ValueError):
                raise ValidationError(self.INVALID_FILE_MESSAGE)
              # Generate file name:
            if file_name is None:
                file_name = self.get_file_name(decoded_file)
            # Use filetype to guess the MIME type and extension
          
            file_extension = self.get_file_extension(file_name, decoded_file)
            self.INVALID_TYPE_MESSAGE=f"Files of type {file_extension} are not allowed."
            if self.trust_provided_content_type:
                if file_mime_type not in self.ALL_MIME_TYPES:
                    raise ValidationError(self.INVALID_TYPE_MESSAGE)
            if file_extension not in self.ALLOWED_TYPES:
                raise ValidationError(self.INVALID_TYPE_MESSAGE)
           
          
            complete_file_name = file_name 
            
            data = SimpleUploadedFile(
                name=complete_file_name,
                content=decoded_file,
                content_type=file_mime_type
            )
          
         
        return data
class ImageBase64FileField(Base64FileField):
    ALL_MIME_TYPES = {
    'image/jpeg': 'jpg',
   
    'image/png': 'png',
  
    'image/gif': 'gif',
    'image/webp': 'webp',
   
  
}
    
    ALLOWED_TYPES = [ 'gif','jpg', 'jpeg', 'png','webp']

    def __init__(self, *args, **kwargs):
       
        self.allow_type = kwargs.pop('allow_type', self.ALLOWED_TYPES)
        self.trust_provided_content_type=True
        self.file_mime_type = None
        
        super().__init__(*args, **kwargs) 
    def get_file_extension(self, filename, decoded_file):
       extension=filename.split('.')[-1].lower()
       return  "jpg" if extension == "jpeg"  else  extension
   
    def to_internal_value(self, base64_data):
        if base64_data in self.EMPTY_VALUES:
            return None

        if isinstance(base64_data, str):
            file_mime_type = None
            file_name=None
            # Strip base64 header, get mime_type from base64 header.
            if ";base64," in base64_data:
                header, base64_data = base64_data.split(";base64,")
                typedata,name=header.split(",")
                if name:
                    file_name=name.replace("name:","")
                file_mime_type = typedata.replace("data:", "")
            try:
                decoded_file = base64.b64decode(base64_data)
                # print("decoded_file",decoded_file)
            except (TypeError, binascii.Error, ValueError):
                raise ValidationError(self.INVALID_FILE_MESSAGE)
              # Generate file name:
            if file_name is None:
                file_name = self.get_file_name(decoded_file)
            # Use filetype to guess the MIME type and extension
        
            file_extension = self.get_file_extension(file_name, decoded_file)
            self.INVALID_TYPE_MESSAGE=f"Files of type {file_extension} are not allowed."
            if self.trust_provided_content_type:
                if file_mime_type not in self.ALL_MIME_TYPES:
                    raise ValidationError(self.INVALID_TYPE_MESSAGE)
            if file_extension not in self.ALLOWED_TYPES:
                raise ValidationError(self.INVALID_TYPE_MESSAGE)
           
            complete_file_name = file_name 
            
            data = SimpleUploadedFile(
                name=complete_file_name,
                content=decoded_file,
                content_type=file_mime_type
            )
          
         
        return data

    
class FileSerializer(serializers.ModelSerializer):
    file_upload = CustomBase64FileField(allow_type=['txt', 'docx', 'jpg', 'jpeg', 'png'],allow_null=True)
    image=ImageBase64FileField(required=False)
    class Meta:
        model = Fileupload
        fields = ('name', 'file_upload', 'image')
    def create(self, validated_data):
        # print(validated_data.get('file_upload').size)
        return super().create(validated_data)
   
    

