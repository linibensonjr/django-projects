from django.contrib import admin


from .models import *
class TaskAdmin(admin.ModelAdmin):
    list_display = ["task", "completed", "date"]
    class Meta:
        model = Task
# Register your models here.
admin.site.register(Task, TaskAdmin)
