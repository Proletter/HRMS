from HRMS.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "HRMS_crumbs.context_processors.breadcrumbs",
)
