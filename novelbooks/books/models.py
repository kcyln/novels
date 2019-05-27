from django.db import models

# Create your models here.

class BookType(models.Model):
    """小说类型模型类"""
    name = models.CharField(max_length=20, verbose_name='分类名称')

    class Meta:
        db_table = 'bk_book_type'
        verbose_name = '小说分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Book(models.Model):
    """小说模型类"""
    type = models.ForeignKey('BookType', verbose_name='小说分类', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='小说名称')
    
    class Meta:
        db_table = 'bk_book_name'
        verbose_name = '小说名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BookContent(models.Model):
    """小说章节模型类"""
    book = models.ForeignKey('Book', verbose_name='小说名称', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='章节名称')
    content = models.TextField()
    
    class Meta:
        db_table = 'bk_book_content'
        verbose_name = '小说章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name