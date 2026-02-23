from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Start the year strong: Learn Django at least 20 minutes every day.",
    "february": "Improve your Python skills: Solve one algorithm problem daily.",
    "march": "Focus on health: Walk at least 30 minutes every day.",
    "april": "Build something real: Create a small web project by the end of the month.",
    "may": "Read consistently: Read 10 pages of a technical book every day.",
    "june": "Sharpen your Git skills: Practice branching and merging workflows.",
    "july": "Level up backend knowledge: Learn about REST APIs and build one.",
    "august": "Data month: Practice NumPy and Pandas at least 30 minutes daily.",
    "september": "Algorithm month: Study data structures and implement them from scratch.",
    "october": "Optimization month: Refactor old code and improve its performance.",
    "november": "Testing month: Learn unit testing and test your previous projects.",
    "december": "Reflection month: Review the year, document your progress, and plan next goals."
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month -1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")