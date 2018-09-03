from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView


from Notes.models import Note
from Notes.forms import NoteForm

# Create your views here.

def index_view(request):
    template = 'index.html'
    queryset = Note.objects.values('id', 'text')
    context = {
        'notes': queryset,
        'form': NoteForm
    }
    return render(request, template, context)

def handle_form(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
    return redirect('index')
