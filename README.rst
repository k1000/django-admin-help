#################
django-admin-help
#################

Interactive help for django admin.
I allows "stap by step" guidence and direct reference.
It uses `intro.js <https://github.com/usablica/intro.js>` for presentation layer 

============
Installation
============

You will need to add ``admin-help`` to ``INSTALLED_APPS`` your settings.py

Run ``python manage.py collectstatic``

Finally, run ``python manage.py syncdb`` in your application's directory to create the tables.

Optionally can be installed ``django_admin_bootstrapped`` for sotable admin inlines

================
Setup your admin
================

You will need to extend your Admin class with ``HelpAdminMixin`` putting it before ``admin.ModelAdmin``::
	

	from admin_help.admin import HelpAdminMixin

	class YourAdmin(HelpAdminMixin, admin.ModelAdmin):
		...

This among other things overides default ``change_form.html`` admin teplate with ``admin/admin_help/change_form.html``
