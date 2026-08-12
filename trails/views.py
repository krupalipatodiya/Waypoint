from django.shortcuts import render


def home(request):
    return render(request, "trails/home.html")


def report_trail(request):
    if request.method == "POST":
        trail_name = request.POST.get("trail_name")
        difficulty = request.POST.get("difficulty")

        context = {
            "trail_name": trail_name,
            "difficulty": difficulty,
        }

        return render(request, "trails/thank_you.html", context)

    return render(request, "trails/report_trail.html")

def search_trails(request):
    query = request.GET.get("q", "")

    trails = [
        "Rockwood Trail",
        "Riverside Trail",
        "Mountain Route",
        "Forest Run",
        "Lake Trail",
    ]

    results = []

    if query:
        for trail in trails:
            if query.lower() in trail.lower():
                results.append(trail)

    context = {
        "query": query,
        "results": results,
    }

    return render(request, "trails/search.html", context)