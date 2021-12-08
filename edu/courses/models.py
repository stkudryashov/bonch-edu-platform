from django.db import models
from django.conf import settings


class Lesson(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='lessons',
        related_query_name='lesson',
        verbose_name='преподаватель')

    message = models.TextField(max_length=200, verbose_name='текст занятия')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата')

    is_approved = models.BooleanField(default=False, verbose_name='одобрено')
    id_rejected = models.BooleanField(default=False, verbose_name='отклонен')

    def __str__(self):
        return f'{self.author.username}-id-{str(self.pk)}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ['-datetime', '-author']
