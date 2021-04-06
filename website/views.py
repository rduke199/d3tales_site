from django.shortcuts import render
from .extraction import *


def home(request):
    return render(request, 'website/home.html')


def about(request):
    context = {
        "title": "About",
        'mission': get_text('mission.txt'),
        'about': get_text('about.txt'),
        'leadership': get_text('leadership.txt')
    }
    return render(request, 'website/about.html', context)


def documents(request):
    context = {"title": "Personnel"}
    return render(request, 'website/documents.html', context)


def personnel(request):
    context = {
        "title": "Personnel",
        "pis": get_members("PIs_SeniorPersonnel"),
        "members": {
            "Postdoctoral Students": get_members("Postdocs"),
            "Graduate Students": get_members("Graduates"),
            # "Undergraduate Students": get_members("Undergraduates"),
            "Evaluation Team": get_members("EvaluationTeam")
        }
    }
    return render(request, 'website/personnel.html', context)


def research(request):
    context = {
        'title': "Research",
        'data_aggregation': get_text('data_aggregation.txt'),
        'molecules': get_text('molecules.txt'),
        'electrolytes': get_text('electrolytes.txt'),
        'data_driven_discovery': get_text('data_driven_discovery.txt')
    }
    return render(request, 'website/research.html', context)


def publications(request):
    context = {
        'title': "Publications",
        'publications': journal_articles(),
    }
    return render(request, 'website/publications.html', context)


def database(request):
    return render(request, 'website/database.html')


def outreach(request):
    return render(request, 'website/outreach.html')
