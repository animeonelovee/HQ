from rest_framework import serializers
from .models import *


class LessonViewStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonViewStatus
        fields = ['duration_watched', 'viewed']

class LessonSerializer(serializers.ModelSerializer):
    view_statuses = serializers.SerializerMethodField()

    def get_view_statuses(self, obj):
        user_id = self.context.get('user_id')
        view_statuses = obj.view_statuses.filter(user_id=user_id)
        return LessonViewStatusSerializer(view_statuses, many=True).data

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_link', 'duration', 'view_statuses']



class ProductLessonViewStatusSerializer(LessonViewStatusSerializer):
    class Meta(LessonViewStatusSerializer.Meta):
        fields = LessonViewStatusSerializer.Meta.fields + ['last_time_watched']

class ProductLessonSerializer(LessonSerializer):
    view_statuses = serializers.SerializerMethodField()

    def get_view_statuses(self, obj):
        user_id = self.context.get('user_id')
        view_statuses = obj.view_statuses.filter(user_id=user_id)
        return ProductLessonViewStatusSerializer(view_statuses, many=True).data

    class Meta(LessonSerializer.Meta):
        pass


class ProductStatisticsSerializer(serializers.ModelSerializer):
    num_lessons_viewed = serializers.IntegerField()
    total_watch_time = serializers.IntegerField()
    num_students = serializers.IntegerField()
    purchase_percentage = serializers.FloatField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'num_lessons_viewed', 'total_watch_time', 'num_students', 'purchase_percentage']