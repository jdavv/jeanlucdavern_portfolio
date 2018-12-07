from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from meta.models import ModelMeta


class Keywords(models.Model):
    class Meta:
        verbose_name_plural = 'keywords'

    name = models.CharField(max_length=16, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Keywords, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('projects:projects_with_keywords_list', kwargs={'slug': self.slug})


class Project(ModelMeta, models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=168)
    repo = models.URLField()
    slug = models.SlugField()
    image = models.ImageField(
            upload_to='project_images',
            default='project_images/default_project.png')
    keywords = models.ManyToManyField(Keywords)
    displayed_on_home_page = models.BooleanField(default=False)

    _metadata = {
        'title': 'title',
        'description': 'description',
        'image': 'get_meta_image',
        'use_twitter': 'True',
    }

    def get_meta_image(self):
        if self.image:
            return self.image.url

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})


class About(ModelMeta, models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to='meta_images')
    meta_description = models.CharField(max_length=160)
    displayed_on_about_page = models.BooleanField(default=False)

    _metadata = {
       'title': 'title',
       'description': 'meta_description',
       'url': 'get_absolute_url',
       'image': 'get_meta_image'
    }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about')

    def get_meta_image(self):
        if self.image:
            return self.image.url
