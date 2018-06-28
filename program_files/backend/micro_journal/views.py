from django.shortcuts import render
from django.views.generic import TemplateView



catchall = TemplateView.as_view(template_name="index.html")

'''
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
'''