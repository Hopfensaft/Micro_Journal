from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from journal_entries.models import JournalEntry


class HomeView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        return context


def journal_entry_view(request):
    template_name = "journalview.html"
    je_list = []
    for item in JournalEntry.objects:

        je_list.append(item.day_number)
    print(je_list)
    je_list = JournalEntry.objects.all()
    context = {
        "object_list": list(je_list)
    }
    return render(request, template_name, context)