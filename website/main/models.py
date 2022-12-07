from django.db import models

class Task(models.Model):
    title=models.CharField("Название", max_length=50)
    task=models.TextField ("Описание")

    def __str__(self):
         return self.title

    class Meta:
         verbose_name="Задача",
         verbose_name_plural="Задачи"

class Notes (models.Model):
    title=models.CharField("Название",max_length=50)
    full_text=models.TextField("Описание")
    date=models.DateTimeField('Дата записи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Заметка",
        verbose_name_plural="Заметки"