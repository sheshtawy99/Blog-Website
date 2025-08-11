from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.


class Postadmin(admin.ModelAdmin):
    list_display = ("tittle", "date", "author")
    list_filter = ("author", "tag", "date")
    prepopulated_fields = {"slug": ("tittle",)}

class commentadmin(admin.ModelAdmin):
    list_display = ("User_name",  "post")


admin.site.register(Post, Postadmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment ,commentadmin)
