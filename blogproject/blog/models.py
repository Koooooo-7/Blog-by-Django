# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        managed = False
        db_table = 'category'


class Post(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    excerpt = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    tags = models.ForeignKey('Tags', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'get_id': self.article_id})

    class Meta:
        managed = False
        db_table = 'post'


class Tags(models.Model):
    tags_id = models.AutoField(primary_key=True)
    tags_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tags_name

    class Meta:
        managed = False
        db_table = 'tags'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user_name

    class Meta:
        managed = False
        db_table = 'user'
