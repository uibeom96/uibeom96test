from django.contrib import admin
from couweb.models import Webs, Category


@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("title", )
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Webs)
class WebsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "rank", "ship", "url")
    list_display_links = ("title", )

