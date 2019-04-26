from django.shortcuts import render

from ebaytrading import settings


def home(request):
    from .ebay.findbykeywords import findbykeywords
    return render(request, "home.html", {"findbykeywords": findbykeywords})


def about(request):
    from pages.namer import namer
    return render(request, "about.html", {"aboutme": namer})


def contact(request):
    return render(request, "contact.html", {})


def get_session(request):
    from .ebay.fetchtoken import get_session_id
    return render(request, "home.html", {"session_id": get_session_id, "runame": settings.URNAME})


def get_token(request):
    from .ebay.fetchtoken import get_token
    return render(request, "home.html", {"token": get_token})


