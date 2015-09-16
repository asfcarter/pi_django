from django.views import generic

class Index2Page(generic.TemplateView):
    template_name = "index.html"
