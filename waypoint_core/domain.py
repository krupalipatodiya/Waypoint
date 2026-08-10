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

    def __str__(self):
        return f"{self._magnitude:.2f} {self._unit}"

class Trail:
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