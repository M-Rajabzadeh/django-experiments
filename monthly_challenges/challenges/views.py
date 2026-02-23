from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Learn Django at least 20minutes every day" 
    elif month == "february":
        challenge_text = "Study for 3 hours python"
    elif month == "march":
        challenge_text = "Walk for at least 30 minutes every day"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)