from django.db import models
def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/file/<name>/<filename>
    return f'file/{instance.name}_{filename}'

# Create your models here.
class Fileupload(models.Model):
    name=models.CharField(max_length=60)
    file_upload=models.FileField(upload_to=user_directory_path,null=True)
    image = models.ImageField(upload_to="image/",null=True)