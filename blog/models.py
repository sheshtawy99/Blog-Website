from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption


class Author(models.Model):
    firts_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def fullname(self):
        return f"{self.firts_name} {self.last_name}"

    def __str__(self):
        return self.fullname()


class Post(models.Model):
    tittle = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self) :
        return self.tittle

class Comment(models.Model):
    User_name = models.CharField(max_length=120)
    User_Email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name="comment")
