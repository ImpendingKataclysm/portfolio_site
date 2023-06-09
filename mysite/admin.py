from django.contrib import admin

from .models import Project


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("name", )
    search_fields = ("name", )


admin.site.register(Project, PortfolioAdmin)
