import json
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from django_admin_bootstrapped.admin.models import SortableInline

from models import Step, Page


class HelpAdminMixin(admin.ModelAdmin):
    #change_form_template = "admin/admin_help/change_form.html"

    class Media:
        js = ["/static/intro.js/intro.js", "static/admin-help.js"]
        css = {
            'all': ["/static/intro.js/introjs.css"]
        }

    def get_steps(self, path):
        #import ipdb; ipdb.set_trace()
        try:
            help_page = Page.objects.get(path=path)
        except Page.DoesNotExist:
            # there is still no help for this page
            pass
        else:
            return help_page.step_set.all()

    def render_steps_json(self, steps):
        steps_dict = []
        for step in steps:
            steps_dict.append(dict(
                element=step.element,
                intro=step.desc,
                position=step.position
            ))
        return json.dumps(steps_dict)

    def add_view(self, request, form_url='', extra_context=None):
        # adds steps to the context
        extra_context = extra_context or {}
        steps = self.get_steps(request.get_full_path())
        if steps:
            extra_context['steps'] = self.render_steps_json(steps)
        return self.changeform_view(request, None, form_url, extra_context)


class StepInline(admin.StackedInline, SortableInline):
    model = Step
    extra = 1


class HelpPageAdmin(admin.ModelAdmin):
    list_display = ["path", "completed"]

    inlines = [StepInline]


admin.site.register(Page, HelpPageAdmin)
