from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Sum
from .models import *
from .serializers import *
from django.db.models import Q
from django.db.models.functions import Coalesce

class LessonsList(APIView):

	def get(self, request, user_id):
		lessons_with_access = Lesson.objects.filter(
    		products__productaccess__user=user_id,
    		products__productaccess__has_access=True,
		).distinct()
		serializer = LessonSerializer(lessons_with_access, many=True, context={'user_id': user_id})
		return Response(serializer.data)

class ProductLessonsList(APIView):

	def get(self, request, user_id, product_id):
		lessons_with_access = Lesson.objects.filter(
    		products__productaccess__user=user_id,
			products__productaccess__product=product_id,
    		products__productaccess__has_access=True
		).distinct()
		serializer = ProductLessonSerializer(lessons_with_access, many=True, context={'user_id': user_id})
		return Response(serializer.data)

class Statistics(APIView):

	def get(self, request):
		product_statistics = Product.objects.annotate(
            num_lessons_viewed=Count('lessons__view_statuses', distinct=True, filter=Q(lessons__view_statuses__viewed=True)),
            total_watch_time=Coalesce(Sum('lessons__view_statuses__duration_watched', distinct=True), 0),
            num_students=Count('access', distinct=True),
            purchase_percentage=Count('access', distinct=True) * 100 / UserModel.objects.count()
        )
		serializer = ProductStatisticsSerializer(product_statistics, many=True)
		return Response(serializer.data)