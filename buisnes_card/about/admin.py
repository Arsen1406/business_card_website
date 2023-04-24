from django.contrib import admin

from .models import HardSkil, Training, Carrier


class HardSkilAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'mastered',
        'color',
    )

    search_fields = ('title',)
    filter_horizontal = ('course', 'carriers',)
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


class CarrierAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'post',
        'company',
        'duties',
        'achievements',
        'start_date',
        'end_date',
    )

    search_fields = ('post',)
    list_filter = ('start_date',)
    empty_value_display = '-пусто-'


admin.site.register(Carrier, CarrierAdmin)
admin.site.register(HardSkil, HardSkilAdmin)
admin.site.register(Training, TrainingAdmin)
