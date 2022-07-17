from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

def validation_file_extention(value):
    import os
    from django.core.exceptions import ValidationError
    ext=os.path.splitext(value.name)[1]
    valid_extensions=['.jpg','.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension')

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avatar=models.FileField(upload_to='files/user_avatar/',null=False,blank=False,validators=[validation_file_extention])
    description=models.CharField(max_length=512,null=False,blank=False)
    def __str__(self):
        return self.user
class Article(models.Model):
    title=models.CharField(max_length=256,null=False,blank=False)
    cover=models.FileField(upload_to='files/article_cover/',null=False,blank=False,validators=[validation_file_extention])
    content=RichTextField()
    created_at=models.DateTimeField(default=datetime.now,blank=False)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    author=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Category(models.Model):
    title=models.CharField(max_length=128,null=False,blank=False)
    cover=models.FileField(upload_to='files/category_cover/',null=False,blank=False,validators=[validation_file_extention])
    def __str__(self):
        return self.title