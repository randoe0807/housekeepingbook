from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    class Meta:
        db_table = 'custom_user'
        verbose_name_plural = 'CustomUser'
    
    def __str__(self):
        return self.username
# Create your models here.
