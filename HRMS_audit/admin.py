"""
admin.py
"""

from django.contrib import admin

from HRMS_audit.models import AuditTag, HRMSAuditInfo, HRMSAuditLog

# Register your models here.

admin.site.register(AuditTag)
