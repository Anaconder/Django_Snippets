from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import All_snippets


class All_snippetsAdmin(admin.TabularInline):
    list_display = ('Title_text', 'Tags_text','Author_text','Publication_date','Rating_text')
    list_filter = ['Publication_date']
    search_fields = ['Title_text', 'Tags_text','Author_text','Publication_date','Rating_text']
    fieldsets = [
        (None,               {'fields': ['Title_text']}),
        (None,               {'fields': ['Tags_text']}),
        (None,               {'fields': ['Author_text']}),
        (None,               {'fields': ['Rating_text']}),
        ('Date information', {'fields': ['Publication_date']}),
    ]
admin.site.register(All_snippets, All_snippetsAdmin)