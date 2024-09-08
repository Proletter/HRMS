"""
HRMS_middlewares.py

This module is used to register HRMS's middlewares without affecting the HRMS/settings.py
"""

import threading

from django.http import HttpResponseNotAllowed
from django.shortcuts import render

from HRMS.settings import MIDDLEWARE

MIDDLEWARE.append("base.middleware.CompanyMiddleware")
MIDDLEWARE.append("HRMS.HRMS_middlewares.MethodNotAllowedMiddleware")
MIDDLEWARE.append("HRMS.HRMS_middlewares.ThreadLocalMiddleware")
_thread_locals = threading.local()


class ThreadLocalMiddleware:
    """
    ThreadLocalMiddleWare
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request = request
        response = self.get_response(request)
        return response


class MethodNotAllowedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if isinstance(response, HttpResponseNotAllowed):
            return render(request, "405.html")
        return response
