from waypoint_core.domain import Distance, Trail, DayHike, Itinerary

print("=" * 60)
print("WAYPOINT - WEEK 7 TEST")
print("=" * 60)

# -----------------------------
# Test 1 - Distance
# -----------------------------
print("\nTest 1 - Distance")

distance = Distance(10, "km")

print("Original:", distance)
print("Converted:", distance.convert())

# -----------------------------
# Test 2 - Trail from Dictionary
# -----------------------------
print("\nTest 2 - Trail from Dictionary")

trail_data = {
    "id": 101,
    "name": "Rockwood Trail",
    "distance": 5.5,
    "unit": "km",
    "elevation_gain_m": 120,
    "difficulty": "moderate"
}

trail1 = DayHike.from_dict(trail_data)

print(trail1)

# -----------------------------
# Test 3 - Equality
# -----------------------------
print("\nTest 3 - Equality")

trail2 = DayHike(
    101,
    "Another Trail",
    Distance(15, "km"),
    400,
    "hard"
)

print("Same ID:", trail1 == trail2)

# -----------------------------
# Test 4 - Itinerary
# -----------------------------
print("\nTest 4 - Itinerary")

trail3 = DayHike(
    102,
    "Forest Trail",
    Distance(3, "km"),
    50,
    "easy"
)

trail4 = DayHike(
    103,
    "Mountain Trail",
    Distance(4, "km"),
    350,
    "hard"
)

trip = Itinerary()

trip.add_trail(trail1)
trip.add_trail(trail3)
trip.add_trail(trail4)

print("Total Distance:", trip.total_distance())

# -----------------------------
# Test 5 - Validation
# -----------------------------
print("\nTest 5 - Validation")

try:
    Distance(-5, "km")
except ValueError as e:
    print("Negative distance rejected:", e)

try:
    DayHike(
        104,
        "Bad Trail",
        Distance(5, "km"),
        100,
        "Impossible"
    )
except ValueError as e:
    print("Invalid difficulty rejected:", e)

print("\nAll Week 7 tests completed successfully.")

# -----------------------------
# Test 6 - Default Unit
# -----------------------------
print("\nTest 6 - Default Unit")

Trail.set_default_unit("mi")

new_trail = DayHike.from_dict({
    "id": 200,
    "name": "Lake Trail",
    "distance": 8,
    "elevation_gain_m": 150,
    "difficulty": "easy"
})

print("New Trail Unit:", new_trail.distance.unit)
print("Original Trail Unit:", trail1.distance.unit)

# -----------------------------
# Test 7 - Independent Itineraries
# -----------------------------
print("\nTest 7 - Independent Itineraries")

trip2 = Itinerary()

print("Trip 1 Trails:", len(trip.trails))
print("Trip 2 Trails:", len(trip2.trails))