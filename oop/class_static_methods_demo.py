class Calculator:
    """A simple calculator demonstrating class and static methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Performs addition of two numbers.
        Does not depend on class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Performs multiplication and accesses a class attribute.
        The 'cls' parameter allows access to class-level data.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
