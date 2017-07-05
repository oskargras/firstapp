from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note
from django.views import View
from .forms import NoteForm


# Create your views here.
class HomeView(View):
    def get(self, request):
        notes = Note.objects.all()
        form = NoteForm()
        ctx = {"notes": notes, "form": form}
        return render(request, "note.html", ctx)

    def post(self,request):
        form = NoteForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            ctx = {"form": form}
            return render(request, 'note.html', ctx)
        return render(request, 'note.html', {"form":form})