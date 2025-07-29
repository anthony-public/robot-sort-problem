def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines the sorting category based on dimensions and mass.

    Args:
        width (float): Width of the item in cm.
        height (float): Height of the item in cm.
        length (float): Length of the item in cm.
        mass (float): Mass of the item in kg.

    Returns:
        str: 'STANDARD', 'SPECIAL', or 'REJECTED' based on the sorting criteria.
    """

    volume: float = width * height * length

    is_bulky: bool = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy: bool = mass >= 20

    if is_bulky and is_heavy:
        return 'REJECTED'
    elif is_bulky or is_heavy:
        return 'SPECIAL'
    else:
        return 'STANDARD'
