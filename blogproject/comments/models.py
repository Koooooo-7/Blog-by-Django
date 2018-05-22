from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text[:20]

#
# class Comment(models.Model):
#     name = models.CharField(max_length=100)
#     text = models.TextField()
#     created_time = models.DateTimeField()
#     post = models.ForeignKey('Post', models.DO_NOTHING)
#
#     def __str__(self):
#         return self.text[:20]
#
#     class Meta:
#         managed = False
#         db_table = 'comment'

