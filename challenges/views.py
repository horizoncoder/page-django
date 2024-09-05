
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": "December challenge!"
}
def monthly_challenge_by_number(request, month):
    if month > len(month):
        return HttpResponseNotFound('invalid month')
    months = list(monthly_challenges.keys())
    redirect_month = months[month -1]
    return HttpResponseRedirect(reverse("challenge", args=[redirect_month]))

def monthly_challenge(request, month):
    try:
         challenge_text = monthly_challenges[month]
         response_data = f"<h1>{challenge_text}</h1>"
         return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")


