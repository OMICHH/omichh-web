from django.shortcuts import render
import datetime

# Create your views here.
def calendar_view(request):
    year=int(datetime.datetime.today().year)
    month=int(datetime.datetime.today().month)
    context={
        "TodayDate": [year, month],
    }
    return render(request, "events/calendar.html", context)