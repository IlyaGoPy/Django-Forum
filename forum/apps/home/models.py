from django.db import models

from django.utils import timezone

class Theme(models.Model):
	theme_title = models.CharField(max_length = 100)
	theme_text = models.TextField(max_length = 10000)
	pub_date = models.DateTimeField

	def __str__(self):
		return self.theme_title


	class Meta:
		verbose_name = 'Обсуждение'
		verbose_name_plural = 'Обсуждения'


class Comment(models.Model):
	theme = models.ForeignKey(Theme, on_delete = models.CASCADE)
	comment_text = models.TextField(max_length = 10000)

	def __str__(self):
		return self.comment_text

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'