from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView, DetailView
from . import models

# Create your views here.
#def index(request):
#    return render(request, 'index.html')

#class CBView(View):
#    def get(self, request):
#        return HttpResponse("Hello World!")

## Template view example
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # creating context dictionary
        context['injectme'] = "basic injection"     # now storing key-value pair in dictionary
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'  # default : modelName.lower()_list, Eg: school_list
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'  # default : modelName.lower(), Eg: school
    model = models.School
    template_name = 'basic_app/school_detail.html'









