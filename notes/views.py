from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.generic import UpdateView

from .models import Note
from django.views import View
from .forms import NoteForm
from PIL import Image


# Create your views here.
class HomeView(View):
    def get(self, request):
        notes = Note.objects.all()
        ctx = {"notes": notes}
        return render(request, "note.html", ctx)


class AddNoteView(View):
    def get(self, request):
        form = NoteForm
        notes = Note.objects.all()
        ctx = {"form":form,"notes": notes}
        return render(request, "add_note.html", ctx)

    def post(self,request):
        form = NoteForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            ctx = {"form": form}
            return redirect("/")


class DelNoteView(View):
    def get(self, request, note_id):
        note = Note.objects.get(pk=note_id)
        note.delete()
        ctx = {"note": note}
        return redirect("/")


class UpdateNote(UpdateView):
    model = Note
    fields = ['text']
    template_name_suffix = '_update_form'
    success_url = "/"


