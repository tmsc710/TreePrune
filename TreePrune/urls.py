from django.contrib import admin
from django.urls import path
from API.views import Tree

urlpatterns = [
    path('demographics/<slug:endpoint>/', Tree.as_view(), name='tree'),
]
