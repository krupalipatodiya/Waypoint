from waypoint_core.domain import (
    Distance,
    DayHike,
    GuidedDayHike,
    BackpackingRoute,
    TrailRun,
    FakeTrail
)
print("=" * 60)
print("WAYPOINT - WEEK 8 TESTS")
print("=" * 60)

print("\nTest 1 - Distance Operators")

d1 = Distance(5, "km")
d2 = Distance(3, "km")

print("Addition:", d1 + d2)
print("Subtraction:", d1 - d2)
print("Greater than:", d1 > d2)
print("Less than:", d2 < d1)
print("Equal:", d1 == Distance(5, "km"))

print("\nTest 2 - Trail Subclasses")

day_hike = DayHike(
    101,
    "Rockwood Trail",
    Distance(8, "km"),
    120,
    "moderate"
)

backpacking = BackpackingRoute(
    102,
    "Mountain Route",
    Distance(15, "km"),
    600,
    "hard"
)

trail_run = TrailRun(
    103,
    "Forest Run",
    Distance(8, "km"),
    90,
    "easy"
)

print(day_hike.summary())
print("Estimated time:", day_hike.estimated_time())

print(backpacking.summary())
print("Estimated time:", backpacking.estimated_time())

print(trail_run.summary())
print("Estimated time:", trail_run.estimated_time())

print("\nTest 3 - Guided Day Hike")

guided = GuidedDayHike(
    104,
    "Lake Trail",
    Distance(6, "km"),
    100,
    "easy",
    "Alex"
)

print(guided.summary())

print("\nTest 4 - Packing List")

print("Day hike:", day_hike.packing_list())
print("Backpacking:", backpacking.packing_list())

print("\nTest 5 - Mixins")

day_hike.print_summary()
print(backpacking.share())
print(trail_run.share())

print("\nTest 6 - Method Resolution Order")

for item in BackpackingRoute.mro():
    print(item.__name__)


print("\nTest 7 - Duck Typing / Polymorphism")

fake_trail = FakeTrail("Testing Trail")

mixed_trails = [
    day_hike,
    backpacking,
    trail_run,
    fake_trail
]

for trail in mixed_trails:
    print(
        trail.summary(),
        "-",
        f"{trail.estimated_time():.2f}",
        "hours"
    )

print("\nAll Week 8 tests completed successfully.")