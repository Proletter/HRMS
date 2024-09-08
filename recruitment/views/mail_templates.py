"""
offerletter.py

This module is related offerletter feature in HRMS
"""

from django import template
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from base.models import HRMSMailTemplate
from HRMS.decorators import hx_request_required, login_required, permission_required
from recruitment.models import Candidate
