
from django.http import JsonResponse
from .models import ErrorLog
from django.conf import settings
import datetime

def djangotelex_home(request):
    return JsonResponse({"message": "Welcome to Django Telex APM!"})

def get_errors(request):
    errors = ErrorLog.objects.values("error_message", "level", "timestamp")
    return JsonResponse(list(errors), safe=False)

def telex_integration(request):
    """API endpoint to provide integration details to Telex"""
    
    base_url = request.build_absolute_uri('/')[:-1]  # Get base URL dynamically

    integration_json = {
        "data": {
            "date": {
                "created_at": datetime.date.today().isoformat(),
                "updated_at": datetime.date.today().isoformat()
            },
            "descriptions": {
                "app_name": "Django_Telex",
                "app_description": "Tracks errors, performance, and code quality in Django applications.",
                "app_logo": "https://imgur.com/a/KSEnvRb.png",
                "app_url": base_url,
                "background_color": "#ffffff"
            },
            "is_active": True,
            "integration_type": "interval",
            "key_features": [
                "- Captures Django errors",
                "- Monitors response times",
                "- Tracks slow database queries",
                "- Detects function complexity",
                "- Identifies code smells"
            ],
            "integration_category": "Development & Code Management",
            "author": "Hetty",
            "website": base_url,
            "settings": [
                {"label": "Site-1", "type": "text", "required": True, "default": "https://github.com"},
                {"label": "interval", "type": "text", "required": True, "default": "*****"},
                {"label": "Slow Query Threshold", "type": "number", "required": False, "default": "0.5"},
                {"label": "Max Complexity Score", "type": "number", "required": False, "default": "10"},
                {"label": "Code Smell Sensitivity", "type": "text", "required": False, "default": "high"},
                {"label": "Error Threshold", "type": "number", "required": True, "default": "10" },
                {"label": "Performance Alert Threshold (ms)", "type": "number", "required": True, "default": "2000"}
            ],
            "target_url": "",
            "tick_url": f"{base_url}/djangotelex/tick"
        }
    }
    
    return JsonResponse(integration_json)
