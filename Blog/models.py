from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    publishedAt = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("BlogPost")
        verbose_name_plural = ("BlogPosts")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("BlogPost_detail", kwargs={"pk": self.pk})

