class Circle:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a Circle.

        Arg:
            radius (float or int): The radius of the new Circle.
        """
        self.radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

    def get_area(self):
        """Return the area of the Circle."""
        return (self.radius ** 2 * math.pi)

    def get_circumference(self):
        """Return The circumference of the Circle."""
        return (2 * math.pi * self.radius)
