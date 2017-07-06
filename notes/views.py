from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note
from django.views import View
from .forms import NoteForm


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
    def get(self, request):
        notes = Note.objects.all()
        ctx = {"notes": notes}
        return render(request, "del_note.html", ctx)
