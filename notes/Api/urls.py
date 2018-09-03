from django.urls import path

from Api import views
urlpatterns = [
    path('notes/', views.NoteListCreateApiView.as_view()),

]