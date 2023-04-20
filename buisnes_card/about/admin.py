from django.contrib import admin

from .models import HardSkil


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


admin.site.register(HardSkil, HardSkilAdmin)
