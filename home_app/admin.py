# core/admin.py

from django.contrib import admin
from . import models
from django.utils.html import format_html


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'order', 'icon_preview']  # ← icon_preview اضافه شد
    list_editable = ['percentage', 'order']

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="40" height="40" style="object-fit:contain;" />', obj.icon.url)
        return '❌'

    icon_preview.short_description = 'آیکون'


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'number', 'is_active']


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'is_current']


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution']


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company']


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at', 'is_read']
    list_editable = ['is_read']


@admin.register(models.FunFact)
class FunFactAdmin(admin.ModelAdmin):
    list_display = ['label', 'count', 'order']
