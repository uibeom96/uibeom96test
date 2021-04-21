from django.db import models
from conf.models import Base_model
from django.shortcuts import reverse, redirect

class Category(Base_model):
    title = models.CharField(max_length=10000000)
    slug = models.SlugField(max_length=10000000, unique=True, allow_unicode=True)

    class Meta:
        ordering = ("created", )
        db_table = "category"
        verbose_name = "카테고리들"
        verbose_name_plural = "카테고리"

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("webs:current_main", args=[self.slug])

class Webs(Base_model):
    image = models.ImageField(upload_to="screen/%Y-%m-%d")
    title = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)
    rank = models.CharField(max_length=100)
    ship = models.CharField(max_length=100)
    url = models.URLField(max_length=100)

    class Meta:
        ordering = ("-created", )
        db_table = "couweb"
    

    def __str__(self):
        return self.title


    