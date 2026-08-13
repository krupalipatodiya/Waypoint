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

def catalog(request):
    trails = [
        {
            "name": "Rockwood Trail",
            "distance": 8.25,
            "elevation": 220,
            "difficulty": "moderate",
            "is_open": True,
        },
        {
            "name": "Riverside Trail",
            "distance": 5.48,
            "elevation": 110,
            "difficulty": "easy",
            "is_open": True,
        },
        {
            "name": "Mountain Route",
            "distance": 15.76,
            "elevation": 850,
            "difficulty": "expert",
            "is_open": True,
        },
        {
            "name": "Forest Run",
            "distance": 7.34,
            "elevation": 180,
            "difficulty": "moderate",
            "is_open": False,
        },
        {
            "name": "Lake Trail",
            "distance": 4.93,
            "elevation": 75,
            "difficulty": "easy",
            "is_open": True,
        },
        {
            "name": "Summit Trail",
            "distance": 12.68,
            "elevation": 720,
            "difficulty": "hard",
            "is_open": True,
        },
    ]

    return render(request, "trails/catalog.html", {"trails": trails})