from django.contrib import admin

from myapp.models import Food, Consume


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Consume)
class ConsumeAdmin(admin.ModelAdmin):
    pass
