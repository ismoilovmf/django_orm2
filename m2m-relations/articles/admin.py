from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleScope, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count == 0:
            raise ValidationError('Укажите основной раздел!')
        elif count >= 2:
            raise ValidationError('Основным может быть только один раздел!')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ArticleScopeInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name', ]





