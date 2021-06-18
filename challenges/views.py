from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_chalenges = {"january": "Take a walk for 20minutes all through the month!",
                     "february": "Eat no meat all through the month",
                     "march": "Learn django for 20 mins",
                     "april": "Take a walk for 20minutes all through the month!",
                     "may": "Eat no meat all through the month",
                     "june": "Learn django for 20 mins",
                     "july": "Take a walk for 20minutes all through the month!",
                     "auguest": "Eat no meat all through the month",
                     "september": "Learn django for 20 mins",
                     "october": "Take a walk for 20minutes all through the month!",
                     "november": "Eat no meat all through the month",
                     "december": None,
                     }

# Create your views here.


def index(request):
    months = list(monthly_chalenges.keys())

    return render(request, "challenges/index.html",
                  {
                      "months": months
                  })


def monthly_challenges_by_number(request, month):
    months = list(monthly_chalenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_chalenge(request, month):
    try:
        challange_text = monthly_chalenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challange_text,
            "month_name": month,
        })

    except:
        raise Http404()