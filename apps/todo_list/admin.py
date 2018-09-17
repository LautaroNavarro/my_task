from django.contrib import admin

from apps.todo_list.models import Priority, Estate, Task
# Register your models here.
admin.site.register(Priority)
admin.site.register(Estate)
admin.site.register(Task)
