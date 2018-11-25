from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Technologies(models.Model):
    name = models.CharField(max_length=16, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Technologies, self).save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=168)
    repo = models.URLField()
    slug = models.SlugField()
    image = models.ImageField(
            upload_to='project_images',
            default='project_images/default_project.png')
    technologies = models.ManyToManyField(Technologies)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})
