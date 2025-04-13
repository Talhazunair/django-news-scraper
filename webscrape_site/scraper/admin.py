from django.contrib import admin
from .models import Headlines
# Register your models here.

admin.site.register(Headlines)
# @admin.site.register(Headlines)
# class HeadlineAdmin(admin.ModelAdmin):
#     list_display = ('title','url','scraped_at')
#     search_fields = ('title',)
