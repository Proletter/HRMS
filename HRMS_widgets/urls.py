"""
HRMS_widget/urls.py
"""

from django.urls import path

from HRMS_widgets import views

urlpatterns = [
    path("get-filter-form", views.get_filter_form, name="get-filter-form"),
]
