from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='uploads', null=True, blank=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    num_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.content}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")

    def __str__(self):
        return f"{self.user} liked {self.post}"
        


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_set')

    def __str__(self):
        return f"{self.follower} follows {self.followed}"


