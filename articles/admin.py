from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import *


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_present = False
        for form in self.forms:
            if form.cleaned_data.get('is_main') and main_tag_present:
                raise ValidationError('Основным может быть только один раздел')
            if form.cleaned_data.get('is_main') and not main_tag_present:
                main_tag_present = True
        if not main_tag_present:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
