from django.contrib import admin

from .models import HardSkil, Training


class HardSkilAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'mastered',
    )

    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class TrainingAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'school',
        'begin',
        'end',
        'certificate',
    )

    search_fields = ('title',)
    empty_value_display = '-пусто-'



admin.site.register(HardSkil, HardSkilAdmin)
admin.site.register(Training, TrainingAdmin)
