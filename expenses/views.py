from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all().order_by('-created_at')

    note_id = request.GET.get('edit')
    note_to_edit = None

    if note_id:
        note_to_edit = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        if note_to_edit:
            form = NoteForm(request.POST, instance=note_to_edit)
        else:
            form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note_to_edit)

    return render(request, 'expenses/index.html', {
        'notes': notes,
        'form': form,
        'note_to_edit': note_to_edit
    })


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('home')
