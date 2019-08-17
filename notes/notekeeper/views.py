from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import AddNoteForm


@login_required
def dashboard(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'notekeeper/dashboard.html', {'user': user})

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
    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'notekeeper/create_note.html', context)