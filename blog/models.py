from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="post_img/", blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=25)
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")


class Subscriber(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    date_added = models.DateField()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("post_list")

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        return super(Subscriber, self).save(*args, **kwargs)
