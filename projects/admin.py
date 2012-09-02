from django.contrib import admin
from projects.models import Project
from projects.models import News
from projects.models import Post
from projects.models import Donor

class PostInline(admin.TabularInline):
    model = Post
    extra = 2

class DonorInline(admin.TabularInline):
    model = Donor
    extra = 2

class NewsInline(admin.TabularInline):
    model = News
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    inlines = [PostInline,DonorInline,NewsInline] 

admin.site.register(Project, ProjectAdmin)
admin.site.register(Post)
admin.site.register(Donor)
admin.site.register(News)