def sort(width, height, length, mass):
    """
    Determines which stack a package should be dispatched to
    based on its dimensions and mass.

    Parameters:
    - width (float): Width in centimeters
    - height (float): Height in centimeters
    - length (float): Length in centimeters
    - mass (float): Mass in kilograms

    Returns:
    - str: The stack name ("STANDARD", "SPECIAL", or "REJECTED")
    """
    volume = width * height * length

    is_bulky = (
        volume >= 1_000_000
        or width >= 150
        or height >= 150
        or length >= 150
    )
    is_heavy = mass >= 20

    # Use a ternary operator for one of the return conditions
    return (
        "REJECTED"
        if is_bulky and is_heavy
        else "SPECIAL" if is_bulky or is_heavy else "STANDARD"
    )

# Example test cases
if __name__ == "__main__":
    test_cases = [
        # STANDARD (not bulky, not heavy)
        {"width": 50, "height": 50, "length": 50, "mass": 10, "expected": "STANDARD"},
        # Bulky only
        {"width": 200, "height": 50, "length": 50, "mass": 10, "expected": "SPECIAL"},
        # Heavy only
        {"width": 50, "height": 50, "length": 50, "mass": 25, "expected": "SPECIAL"},
        # Bulky by volume only
        {"width": 200, "height": 100, "length": 50, "mass": 10, "expected": "SPECIAL"},
        # Both bulky and heavy
        {"width": 200, "height": 100, "length": 50, "mass": 25, "expected": "REJECTED"},
        # Edge case: volume exactly 1,000,000
        {"width": 100, "height": 100, "length": 100, "mass": 5, "expected": "SPECIAL"},
        # Edge case: dimension exactly 150
        {"width": 150, "height": 50, "length": 50, "mass": 5, "expected": "SPECIAL"},
        # Edge case: mass exactly 20
        {"width": 50, "height": 50, "length": 50, "mass": 20, "expected": "SPECIAL"},
        # Both bulky and heavy at thresholds
        {"width": 150, "height": 150, "length": 150, "mass": 20, "expected": "REJECTED"},
    ]

    for idx, case in enumerate(test_cases, start=1):
        result = sort(case["width"], case["height"], case["length"], case["mass"])
        assert result == case["expected"], f"Test case {idx} failed: expected {case['expected']}, got {result}"
        print(f"Test case {idx} passed: {result}")
