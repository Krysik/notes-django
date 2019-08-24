from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import AddNoteForm
from .models import Note


@login_required
def dashboard(request, user_id):
    user = User.objects.get(pk=user_id)
    notes = Note.objects.filter(user=user_id)
    error = None
    context = {
        'user': user,
        'notes': notes
    }
    return render(request, 'notekeeper/dashboard.html', context)

@login_required
def create_note(request, user_id):
    user = User.objects.get(pk=user_id)
    form = AddNoteForm()
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('dashboard', user.id)
        else:
            error = 'Coś poszło nie tak, sprawdź poprawność danych'
    context = {
        'user': user,
        'form': form,
        'error': error,
    }
    return render(request, 'notekeeper/create_note.html', context)

@login_required
def update_note_view(request, user_id, note_id):
    user = User.objects.get(pk=user_id)
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
            return redirect('dashboard', request.user.id)
        else:
            error = 'Coś poszło nie tak, sprawdź poprawność danych'
        
    context = {
        'note': note,
        'form': form,
        'error': error,
    }
    return render(request, 'notekeeper/create_note.html', context)
    


