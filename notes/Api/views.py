from rest_framework import generics

from Notes.models import Note
from Api.serializers import NoteSerializer
# Create your views here.



class NoteListCreateApiView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer