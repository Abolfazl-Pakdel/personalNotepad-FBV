from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.views import View


from .forms import NoteForm
from .models import Note
# ---------------
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# ---------------
from django.contrib.auth.decorators import login_required
# Create your views here.

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes/index.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NoteForm()
        return context



class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/index.html"
    success_url = reverse_lazy('notepad:index')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("notepad:index")

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/update_note.html"
    success_url = reverse_lazy("notepad:index")
    # def form_valid(self, form):
    #     form.instance.user = self.request.user

'''@login_required()
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect("/")
'''

'''@login_required()
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
'''@login_required()
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


'''
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
