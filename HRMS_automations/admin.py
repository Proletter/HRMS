from django.contrib import admin

from HRMS_automations.models import MailAutomation

# Register your models here.


admin.site.register(
    [
        MailAutomation,
    ]
)
