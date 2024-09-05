from calendar import month

from django.http import HttpResponse, HttpResponseNotFound

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
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
         challenge_text = monthly_challenges[month]
         return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not supported")


