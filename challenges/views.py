from http.client import responses

from django.http import  HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges={
    "january": "January challenge!",
    "february": "February challenge!",
    "march": "March challenge!",
    "april": "April challenge!",
    "may": "May challenge!",
    "june": "June challenge!",
    "august": "August challenge!",
    "september": "September challenge!",
    "october": "October challenge!",
    "november": "November challenge!",
    "december": None
}

def index(request):
    months = list(monthly_challenges.keys())

    return  render(request, "challenges/index.html", {
        "months": months
    })
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

    redirect_month = months[month -1]
    return HttpResponseRedirect(reverse("challenge", args=[redirect_month]))

def monthly_challenge(request, month):
    try:
         challenge_text = monthly_challenges[month]
         return  render(request, "challenges/challenge.html" , {
             "text": challenge_text,
             "month_name": month
         })
    except:
        response_data =  render_to_string("404.html")
        return HttpResponseNotFound(response_data)


