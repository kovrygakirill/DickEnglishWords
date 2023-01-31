from django.db import models

from loginsys.models import UserProfile


class Word(models.Model):
    name = models.CharField(max_length=30)
    transcript = models.CharField(max_length=30, blank=True)
    ru_translate = models.CharField(max_length=30)

    class Meta:
        db_table = "word"

    def __str__(self):
        return self.name


class Dictionary(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name='dictionaries')
    words = models.ManyToManyField(Word, related_name='dictionaries')

    class Meta:
        db_table = "dictionary"

    def __str__(self):
        return self.name
