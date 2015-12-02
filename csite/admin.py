from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.http import HttpResponse
from django.views.generic import View
from .models import Site, Page
from theme.models import Template

class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_site_url', 'created')
    fields = ('name', 'slug', 'theme')

    def has_add_permission(self, request):
        site = Site.objects.filter(user=request.user)
        if site:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        queryset = super(SiteAdmin, self).get_queryset(request)
        return queryset.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def show_pages_url(self, obj):
        return '<a href="/admin/csite/page?site=%s">pages manages</a>' % obj.id

    def show_site_url(self, obj):
        return '<a href="/m/%s" target="_blank">Link</a>' % obj.id
    show_pages_url.allow_tags = True
    show_site_url.allow_tags = True


class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('parent', 'title', 'description', 'template', 'created')
    fields = ('parent', 'title', 'image', 'description', 'content', 'template')

    def check_site(self, request):
        try:
            site = Site.objects.get(user=request.user)
        except Site.DoesNotExist:
            site = Site(
                user = request.user,
                name = 'default',
                slug = unicode(request.user.id),
                theme_id = 1,
            )
            site.save()

    def get_queryset(self, request):
        self.check_site(request)
        queryset = super(PageAdmin, self).get_queryset(request)
        site = Site.objects.get(user=request.user)
        return queryset.filter(site=site)

    def get_form(self, request, obj=None, **kwargs):
        self.check_site(request)
        form = super(PageAdmin, self).get_form(request, obj, **kwargs)
        site = Site.objects.get(user=request.user)
        form.base_fields['parent'].queryset = Page.objects.filter(site=site)
        form.base_fields['template'].queryset = Template.objects.filter(theme=site.theme)
        return form

    def save_model(self, request, obj, form, change):
        self.check_site(request)
        site = Site.objects.get(user=request.user)
        obj.site_id = site.id
        obj.save()


admin.site.register(Site, SiteAdmin)
admin.site.register(Page, PageAdmin)
