from django.urls import path, include
from .views import *
urlpatterns = [
        path('', index, name='index'),
        path('delete/<int:note_id>', delete_note, name='delete_note'),
        path('edit/<int:note_id>', edit_note, name='edit_note'),
]
