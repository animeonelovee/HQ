from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=20)

    class Meta:
        unique_together = ['username']

class Product(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        'UserModel', on_delete=models.CASCADE,
        related_name='products_owned',
    )
    access = models.ManyToManyField(
        'UserModel',
        through='ProductAccess',
        related_name='products_accessed',
    )
    lessons = models.ManyToManyField(
        'Lesson',
        through='LessonProduct',
        related_name='products'
    )

    class Meta:
        unique_together = ['title']

class ProductAccess(models.Model):
    user = models.ForeignKey(
        'UserModel',
        on_delete=models.CASCADE,
        related_name='productaccess',
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='productaccess',
    )
    has_access = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'product']

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    duration = models.IntegerField()
    views = models.ManyToManyField(
        'UserModel',
		through='LessonViewStatus',
        related_name='viewed_lessons',
    )

    class Meta:
        unique_together = ['title']

class LessonProduct(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='products'
    )
    lesson = models.ForeignKey(
        'Lesson',
        on_delete=models.CASCADE,
        related_name='lessons'
    )

    class Meta:
        unique_together = ['product', 'lesson']

class LessonViewStatus(models.Model):
    user = models.ForeignKey(
        'UserModel',
        on_delete=models.CASCADE,
        related_name='lesson_views'
    )
    lesson = models.ForeignKey(
        'Lesson',
        on_delete=models.CASCADE,
        related_name='view_statuses'
    )
    duration_watched = models.IntegerField(default=0)
    last_time_watched = models.DateTimeField(auto_now=True)
    viewed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'lesson']

    def save(self, *args, **kwargs):
        if self.duration_watched >= self.lesson.duration * 0.8:
            self.viewed = True
        else:
            self.viewed = False
        super().save(*args, **kwargs)