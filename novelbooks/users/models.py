from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'bk_users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name