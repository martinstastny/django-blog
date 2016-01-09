from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50, help_text=_('Category name'))
    slug = models.SlugField(verbose_name=_('URL'), help_text=_('URL'))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = _('Categories')

    def get_absolute_url(self):
        return reverse('blog_category_detail', {'slug': self.slug})

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300, help_text=_('Title of the Entry'), db_index=True)
    body = models.TextField(blank=False, verbose_name=_('Content'))
    slug = models.SlugField(unique=True, verbose_name=_('URL'), help_text=_('URL'))
    user = models.ForeignKey('auth.User')
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title