from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all().order_by('-title')

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    return render(request, 'expenses/index.html', {
        'notes': notes,
        'form': form
    })
