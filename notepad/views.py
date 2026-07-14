from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NoteForm
from .models import Note
# Create your views here.

def index(request):
    notes = Note.objects.all()
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("/")
        else:
            return HttpResponse("somethig went wrong")
    elif request.method == "GET":
        context = {'form': form, 'notes': notes}
        return render(request, 'notes/index.html',  context)

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect("/")


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("/")
        else:
            return HttpResponse("somethig went wrong")
    else:
        context = {'form': form, 'note': note}
        return render(request, 'notes/update_note.html', context)

'''
def add_note(request):
    if request.method == "POST":
        print('POST')
        form = NoteForm(request.POST)
        if form.is_valid():
            print(form.errors)
            form.save()
            return redirect("/")
        else:
            return HttpResponse("somethig went wrong")
    elif request.method == "GET":
        form = NoteForm()
        return render(request, 'notes/index.html', {'form': form})
'''

'''
def index(request):
    notes = Note.objects.all()
    form = NoteForm()
    return render(request, 'notes/index.html', {'notes': notes, 'form': form})

def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = NoteForm()

    return render(request, 'notes/add_note.html', {'form': form})

'''
