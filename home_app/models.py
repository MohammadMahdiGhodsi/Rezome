# core/models.py

from django.db import models
from django.utils import timezone


class Profile(models.Model):
    """اطلاعات شخصی"""
    name = models.CharField(max_length=100, default='جرولد')
    title = models.CharField(max_length=200, default='برنامه نویس و طراح UX')
    bio = models.TextField(default='من مشکلات پیچیده کاربران...')
    email = models.EmailField(default='gerolddesign@mail.com')
    phone = models.CharField(max_length=20, default='+01 123 654 8096')
    address = models.TextField(default='گیشای غربی کوچه 38, فاز 57, تهران')
    profile_image = models.ImageField(upload_to='profile/', default='hero/me.png')
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    """شبکه‌های اجتماعی"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='socials')
    name = models.CharField(max_length=50)  # twitter, linkedin, github, etc.
    url = models.URLField()
    icon_class = models.CharField(max_length=50)  # fa-brands fa-twitter

    def __str__(self):
        return f"{self.profile.name} - {self.name}"


class Skill(models.Model):
    """مهارت‌ها"""
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)  # ← این رو اضافه کن
    percentage = models.IntegerField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.percentage}%"


class Service(models.Model):
    """خدمات"""
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=3)  # 01, 02, ...
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    """سابقه کاری"""
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.company}"


class Education(models.Model):
    """تحصیلات"""
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Project(models.Model):
    """پروژه‌ها"""
    CATEGORY_CHOICES = [
        ('uxui', 'UX/UI'),
        ('branding', 'برندینگ'),
        ('mobile-app', 'اپلیکیشن'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_url = models.URLField(blank=True)
    client = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """نظرات مشتریان"""
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    text = models.TextField()
    logo = models.ImageField(upload_to='testimonials/logos/')
    avatar = models.ImageField(upload_to='testimonials/avatars/')

    def __str__(self):
        return f"{self.name} - {self.company}"


class Blog(models.Model):
    """وبلاگ"""
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """پیام‌های تماس"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    service = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class FunFact(models.Model):
    """آمارهای صفحه اصلی"""
    label = models.CharField(max_length=100)  # "سابقه کاری"
    count = models.CharField(max_length=50)  # "14" یا "1.5K"
    description = models.CharField(max_length=200)  # "سال های تجربیات"
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label
