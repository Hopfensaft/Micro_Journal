from django.shortcuts import render
from django.views.generic import View
from journal_entries.models import JournalEntry


class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "main.html", {})

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        return context


def journal_entry_view(request):
    template_name = "journalview.html"

    je_list = JournalEntry.objects.all()

    context = {
        "object_list": list(je_list)
    }
    return render(request, template_name, context)