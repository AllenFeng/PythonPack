from django.contrib import admin

from polls.models import Poll,Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Data Information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    list_display = ('question','pub_date')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    inlines = [ChoiceInline]


admin.site.register(Poll,PollAdmin)

