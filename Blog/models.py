from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, default='kushagra')
    created_at = models.DateTimeField(("created_at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(("updated_at"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = ("BlogPost")
        verbose_name_plural = ("BlogPosts")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("BlogPost_detail", kwargs={"pk": self.pk})




class Contact(models.Model):
    name = models.CharField(("name"), max_length=150, blank=False)
    email = models.EmailField(("email"), max_length=254)
    phone = PhoneNumberField(("phone"))
    query = models.TextField(("query"), blank=False)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Contact_detail", kwargs={"pk": self.pk})
