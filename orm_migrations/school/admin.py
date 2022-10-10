from django.contrib import admin

from .models import Student, Teacher, StudentPosition


class StudentPositionInline(admin.TabularInline):
    model = StudentPosition
    extra = 1
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentPositionInline,]
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
