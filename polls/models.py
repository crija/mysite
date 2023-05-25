import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class People(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    peso = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Pet(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    tamanho = models.FloatField()
    tipo = models.CharField(max_length=20)
    
# Create your models here.
