from django.shortcuts import render


def home(request):
    return render(request, "trails/home.html")


def report_trail(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        trail = request.POST.get("trail", "")
        note = request.POST.get("note", "")

        context = {
            "name": name,
            "email": email,
            "trail": trail,
            "note": note,
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