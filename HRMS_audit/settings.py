"""
HRMS_audit/settings.py

This module is used to write settings contents related to payroll app
"""

from HRMS.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "HRMS_audit.context_processors.history_form",
)
