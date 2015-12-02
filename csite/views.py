from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Site, Page

class IndexView(ListView):
    model = Page

    def dispatch(self, request, *args, **kwargs):
        self.site = Site.objects.get(id=1)
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        #queryset = super(IndexView, self).get_queryset()
        #queryset.filter(site=self.site, parent=None)
        queryset = Page.objects.order_by('-sort').filter(site=self.site, parent=None)
        return queryset

    def get_template_names(self):
        return ("csite/" + self.site.theme.slug + "/index.html")



def page_detail(request, page_id=0):
    page = get_object_or_404(Page, id=page_id)
    context = {
        'page': page,
        'child_page': Page.objects.filter(parent=page),
    }
    template_name = "csite/%s/%s.html" % (page.site.theme.slug, page.template.slug)
    return render(request, template_name, context)
