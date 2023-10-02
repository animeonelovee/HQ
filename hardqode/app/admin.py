from django.contrib import admin
from app.models import (
	UserModel,
	Product,
	Lesson,
	ProductAccess,
	LessonViewStatus,
	LessonProduct
)

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username',]

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']

@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_link', 'duration']

@admin.register(ProductAccess)
class AccessModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'has_access']

@admin.register(LessonViewStatus)
class ViewsModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'duration_watched']

@admin.register(LessonProduct)
class LessonProductModelAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'product']
