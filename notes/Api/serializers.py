from rest_framework import serializers

from Notes.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'text', 'count_unique_words')