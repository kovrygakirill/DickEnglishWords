from django.db import models
from loginsys.models import UserProfile


class Dictionary(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name='dictionaries')

    class Meta:
        db_table = "dictionary"

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=30)
    transcript = models.CharField(max_length=30, blank=True)
    ru_translate = models.CharField(max_length=30)
    dictionaries = models.ManyToManyField(Dictionary, related_name='words')

    class Meta:
        db_table = "word"

    def __str__(self):
        return self.name
