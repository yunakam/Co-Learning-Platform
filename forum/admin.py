from django.contrib import admin

from .models import Answer, Chapter, Course, Question, User

# Class for each Models
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}    # auto-generate the slug name when entering the title

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'slug',)
    list_filter = ('title', 'course',)
    prepopulated_fields = {'slug': ('course', 'title',)}

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'chapter')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'question')


# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)