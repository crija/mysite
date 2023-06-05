from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path("<int:question_id>/",
views.detail, name="detail"),

    path("<int:question_id>/results/",
views.vote, name="results"),

    path("<int:question_id>/vote/",
views.vote, name="vote"),

    path('criar', views.criar, name='criar'),

    path('criar/cadastro', views.cadastro, name='cadastro'),

    path('cadastro/recursos', views.recursos, name='recursos'),

    path('exer', views.exer, name='exer'),

    path('people', views.exer, name='people'),
]
