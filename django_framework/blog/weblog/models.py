from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField('date publiched', auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    body = models.TextField()
    date = models.DateTimeField('date commented', auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.id, self.post.title)
