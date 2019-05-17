from django.db import models
from django.utils.text import slugify
from .validators import validate_author_email
from django.db.models.signals import pre_save, post_save 
from django.utils import timezone
from django.utils.timesince import timesince
from datetime import timedelta, datetime, date

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private')
)

class PostModel(models.Model):
    id              = models.BigAutoField(primary_key=True)
    active          = models.BooleanField(default=True)
    title           = models.CharField(
        max_length=240,
        verbose_name="Post Title", 
        unique=True,
        error_messages = {
            "unique": "Ayni baslikta baska kayit olamaz",
            "blank": "This field can not be blank"
        },
        help_text = "Must be unique title",
        )
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False)
    author_email    = models.EmailField(max_length=240, validators=[validate_author_email], null=True, blank=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs): # models.Model icinde yer alan save methodunu override ediyoruz. isine yarayacak
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)
        


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        #unique_together = [('title', 'slug')]

    def __str__(self):
        return self.title

    def age(self):
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine (
                self.publish_date,
                datetime.now().min.time()
            )
            try:
                difference = now - publish_time
            except:
                return "Unknown"
            if difference <= timedelta(minutes=1):
                return 'just now'
            return f"{timesince(publish_time).split(', ')[0]} ago"
        return "Not Published"

# save fonksiyonunu override etmek yerine signals kullanmak daha saglikliymis
def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("before save")
    if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            

post_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)

def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("after save")
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(blog_post_model_post_save_receiver, sender=PostModel)