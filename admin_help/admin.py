import json
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from django_admin_bootstrapped.admin.models import SortableInline

from models import Step, Page


class HelpAdminMixin(admin.ModelAdmin):
    change_form_template = "admin/admin_help/change_form.html"

    class Media:
        js = ["/static/admin_help/js/intro.js"]
        css = {
            'all': ["/static/admin_help/css/introjs.css"]
        }

    def get_steps(self):
        content_type = ContentType.objects.get_for_model(self.model)
        help_page = Page.objects.get(content_type=content_type)
        steps = help_page.step_set.all()
        return steps

    def render_steps_json(self):
        queryset = self.get_steps()
        steps = []
        for step in queryset:
            steps.append(dict(
                element=step.element,
                intro=step.intro,
                position=step.position
            ))
        return json.dumps(steps)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['steps'] = self.render_steps_json()
        return self.changeform_view(request, None, form_url, extra_context)


class StepInline(admin.StackedInline, SortableInline):
    model = Step
    extra = 1


class HelpPageAdmin(admin.ModelAdmin):
    list_display = ["content_type", "completed"]

    inlines = [StepInline]


admin.site.register(Page, HelpPageAdmin)
