from django.contrib import admin
from .models import Student, Cohort, Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "course", "cohort"]
    list_filter = ["course", "cohort"]


admin.site.register([Cohort, Course])
admin.site.register(Student, StudentAdmin)

