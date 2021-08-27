from django.urls import path
from textutils.views import index, analyze, read_text, personal_navigator

urlpatterns = [
    path('', index, name='home'),
    path('analyze/', analyze, name='analyze'),
    path('rt/', read_text, name='read_text'),
    path('pn/', personal_navigator, name='personal_navigator'),
]
