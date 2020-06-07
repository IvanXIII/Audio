from django.db import models


class Task(models.Model):
    nickname = models.CharField(max_length=20)
    feedback = models.TextField()

    def __str__(self):
        return "Отзыв от "+str(self.nickname)