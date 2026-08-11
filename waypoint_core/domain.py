from abc import ABC, abstractmethod
from typing import Protocol

class Distance:
    """
    Represents a distance with a value and unit.
    """

    KM_TO_MI = 0.621371
    MI_TO_KM = 1.60934

    def __init__(self, magnitude, unit):
        if magnitude < 0:
            raise ValueError("Distance cannot be negative.")

        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'.")

        self._magnitude = float(magnitude)
        self._unit = unit

    @property
    def magnitude(self):
        return self._magnitude

    @property
    def unit(self):
        return self._unit

    def convert(self):
        if self._unit == "km":
            return Distance(
                self._magnitude * self.KM_TO_MI,
                "mi"
            )

        return Distance(
            self._magnitude * self.MI_TO_KM,
            "km"
        )
    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        if self.unit == other.unit:
            other_magnitude = other.magnitude
        else:
            other_magnitude = other.convert().magnitude

        return Distance(
            self.magnitude + other_magnitude,
            self.unit
        )

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        if self.unit == other.unit:
            other_magnitude = other.magnitude
        else:
            other_magnitude = other.convert().magnitude

        result = self.magnitude - other_magnitude

        if result < 0:
            raise ValueError(
                "Distance subtraction cannot result in a negative value."
            )

        return Distance(result, self.unit)

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return False

        if self.unit == other.unit:
            other_magnitude = other.magnitude
        else:
            other_magnitude = other.convert().magnitude

        return abs(
            self.magnitude - other_magnitude
        ) < 0.0001

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        if self.unit == other.unit:
            other_magnitude = other.magnitude
        else:
            other_magnitude = other.convert().magnitude

        return self.magnitude < other_magnitude

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        if self.unit == other.unit:
            other_magnitude = other.magnitude
        else:
            other_magnitude = other.convert().magnitude

        return self.magnitude > other_magnitude

    def __repr__(self):
        return f"Distance({self.magnitude}, '{self.unit}')"

    def __str__(self):
        return f"{self._magnitude:.2f} {self._unit}"

class Trail(ABC):
    """
    Represents a hiking trail.
    """

    DEFAULT_UNIT = "km"

    ALLOWED_DIFFICULTIES = (
        "easy",
        "moderate",
        "hard",
        "expert"
    )

    def __init__(
            self,
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
    ):

        if not self.validate_name(name):
            raise ValueError("Trail name cannot be empty.")

        if not isinstance(distance, Distance):
            raise TypeError("distance must be a Distance object.")

        if elevation_gain_m < 0:
            raise ValueError("Elevation gain cannot be negative.")

        self.id = trail_id
        self.name = name
        self.distance = distance
        self.elevation_gain_m = elevation_gain_m

        self.__difficulty = None
        self.set_difficulty(difficulty)

    @property
    def difficulty(self):
        return self.__difficulty

    def set_difficulty(self, difficulty):

        difficulty = difficulty.lower()

        if not self.validate_difficulty(difficulty):
            raise ValueError(
                "Difficulty must be easy, moderate, hard or expert."
            )

        self.__difficulty = difficulty

    @classmethod
    def set_default_unit(cls, unit):

        if not cls.validate_unit(unit):
            raise ValueError("Unit must be km or mi.")

        cls.DEFAULT_UNIT = unit

    @classmethod
    def from_dict(cls, trail_data):

        unit = trail_data.get(
            "unit",
            cls.DEFAULT_UNIT
        )

        distance = Distance(
            trail_data["distance"],
            unit
        )

        return cls(
            trail_data["id"],
            trail_data["name"],
            distance,
            trail_data["elevation_gain_m"],
            trail_data["difficulty"]
        )

    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and len(name.strip()) > 0

    @staticmethod
    def validate_unit(unit):
        return unit in ("km", "mi")

    @staticmethod
    def validate_difficulty(difficulty):
        return difficulty in Trail.ALLOWED_DIFFICULTIES

    def __eq__(self, other):

        if not isinstance(other, Trail):
            return False

        return self.id == other.id
    @abstractmethod
    def estimated_time(self):
        pass

    def packing_list(self):
        return [
            "Water",
            "Map",
            "First aid kit"
        ]

    def __str__(self):
        return (
            f"{self.name} | "
            f"{self.distance} | "
            f"{self.elevation_gain_m} m | "
            f"{self.difficulty}"
        )
class Itinerary:
    """
    Represents an ordered list of trails for a trip.
    """

    def __init__(self):
        self._trails = []

    @property
    def trails(self):
        return self._trails.copy()

    def add_trail(self, trail):
        if not isinstance(trail, Trail):
            raise TypeError("Only Trail objects can be added.")

        self._trails.append(trail)

    def total_distance(self):
        total_km = 0.0

        for trail in self._trails:
            if trail.distance.unit == "km":
                total_km += trail.distance.magnitude
            else:
                total_km += trail.distance.convert().magnitude

        return Distance(total_km, "km")

class HasSummary(Protocol):
    def summary(self) -> str:
        ...


class HasName(Protocol):
    name: str


class PrintableMixin:
    """
    Mixin that prints a trail summary.
    """

    def print_summary(self: HasSummary):
        print(self.summary())

class ShareableMixin:
    """
    Mixin that shares a trail.
    """

    def share(self: HasName):
        return f"Sharing '{self.name}' with friends!"


class DayHike(PrintableMixin, Trail):
    """
    Represents a day hike.
    """

    def estimated_time(self):
        return self.distance.magnitude / 4

    def summary(self):
        return f"Day Hike: {self.name}"

class GuidedDayHike(DayHike):
    """
    Represents a guided day hike.
    """

    def __init__(
            self,
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty,
            guide_name
    ):
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

        self.guide_name = guide_name

    def summary(self):
        return (
            super().summary()
            + f" | Guide: {self.guide_name}"
        )

class BackpackingRoute(PrintableMixin, ShareableMixin, Trail):
    """
    Represents a multi-day backpacking route.
    """

    def __init__(
            self,
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
    ):
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    def estimated_time(self):
        return self.distance.magnitude / 3

    def summary(self):
        return f"Backpacking Route: {self.name}"

    def packing_list(self):
        items = super().packing_list()
        items.extend([
            "Tent",
            "Sleeping bag",
            "Food"
        ])
        return items

class TrailRun(ShareableMixin, Trail):
    """
    Represents a trail running route.
    """

    def __init__(
            self,
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
    ):
        super().__init__(
            trail_id,
            name,
            distance,
            elevation_gain_m,
            difficulty
        )

    def estimated_time(self):
        return self.distance.magnitude / 8

    def summary(self):
        return f"Trail Run: {self.name}"


class FakeTrail:
    """
    Duck-typed trail used to demonstrate polymorphism.
    This class does not inherit from Trail.
    """

    def __init__(self, name, hours=1.5):
        self.name = name
        self.hours = hours

    def estimated_time(self):
        return self.hours

    def summary(self):
        return f"Fake Trail: {self.name}"

