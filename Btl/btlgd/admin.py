from django.contrib import admin
from btlgd.models import Article, Call

# Register your models here.
admin.site.site_header = "desing-BTL"
admin.site.site_title = "BTL"
admin.site.index_title = "Manager"


class AdminArticle(admin.ModelAdmin):
    list_display = ('name', 'ordered_date')


admin.site.register(Article, AdminArticle)

admin.site.register(Call)