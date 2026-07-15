from django.urls import path, include
from .views import *

app_name = 'notepad'

urlpatterns = [
        path('', NoteListView.as_view(), name='index'),
        path('create/', NoteCreateView.as_view(), name='create'),
        path('delete/<int:pk>', NoteDeleteView.as_view(), name='delete_note'),
        path('edit/<int:pk>', NoteUpdateView.as_view(), name='edit_note'),
]
