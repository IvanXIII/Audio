from django.db import models


class Task(models.Model):
    nickname = models.CharField(max_length=20)
    feedback = models.TextField()

    def __str__(self):
        return "Отзыв от " + str(self.nickname)


class Lection(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название лекции')
    number_of_lection = models.IntegerField(verbose_name='Номер лекции')
    description = models.TextField(verbose_name='Краткое описание лекции')
    long_description = models.TextField(verbose_name='Описание(уже подлиннее)')
    photo = models.ImageField(default=0, upload_to='lections/images', verbose_name='Изображение к лекции')
    audio = models.FileField(default=0, upload_to='lections/audios', verbose_name='Аудио к лекции')

    def __str__(self):
        return "Лекция № " + str(self.number_of_lection)

