from django.contrib import admin
from portfolio.models import Home, About, Category, Skills, Project, Experience, JobDescription
# Register your models here.


BasicModels = [Home, Project, About]
admin.site.register(BasicModels)

# Expierience
class JobsInline(admin.TabularInline): # To display inline to About
    model = JobDescription
    extra = 1

@admin.register(Experience)
class AboutJob(admin.ModelAdmin):
    inlines = [
        JobsInline,
    ]


# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]
