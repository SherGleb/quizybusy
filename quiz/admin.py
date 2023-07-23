from django.contrib import admin

# Register your models here.

from .models import *


class QuizAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class QuestionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('question',)}


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers)
