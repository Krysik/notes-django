from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AddNoteForm
from .models import Note


@login_required
def dashboard(request):
    notes = Note.objects.filter(user=request.user.id)
    error = None
    context = {
        'notes': notes
    }
    return render(request, 'notekeeper/dashboard.html', context)

@login_required
def create_note(request):
    form = AddNoteForm()
    error = None
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('dashboard')
        else:
            error = 'Coś poszło nie tak, sprawdź poprawność danych'
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'notekeeper/create_note.html', context)

@login_required
def update_note_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    form = AddNoteForm(initial={'title': note.title, 'content': note.content})
    error = None
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            note.title = title
            note.content = content
            note.save(update_fields=['title', 'content'])
            note.save()
            return redirect('dashboard')
        else:
            error = 'Coś poszło nie tak, sprawdź poprawność danych'
    context = {
        'note': note,
        'form': form,
        'error': error,
    }
    return render(request, 'notekeeper/create_note.html', context)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    messages.success(request, 'Notatka została usunięta poprawnie')
    return redirect('dashboard')

@login_required
def user_profile(request):
    return render(request, 'notekeeper/profile.html')

    


