from ast import Not
#import imp
from pyexpat import model
import re
from statistics import mode
from django.forms import fields
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Notes
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    login_url = "/login"
    #template_name = "notes/notes_list.html"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/admin"

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    login_url = "/admin"

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    login_url = "/admin"


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes': all_notes})

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
    
#     except Notes.DoesNotExist:
#         raise Http404("Note doesnt exist")
#     return render(request,'notes/notes_detail.html',{'note': note})
