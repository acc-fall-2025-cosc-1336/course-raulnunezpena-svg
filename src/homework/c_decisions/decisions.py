

def get_options_ratio(option: float, total: float) -> float:
    """
    Return option/total as a float in [0, 1].
    Raises ValueError if total <= 0 or option < 0.
    """
    if total <= 0:
        raise ValueError("total must be > 0")
    if option < 0:
        raise ValueError("option must be >= 0")
    ratio = option / float(total)
    # Clamp to [0, 1] to match rubric assumptions
    return max(0.0, min(ratio, 1.0))


def get_faculty_rating(ratio: float) -> str:
    """
    Map ratio to rating per rubric:

      0.00 to 0.60          -> Unacceptable
      >0.60 to 0.70         -> Needs Improvement
      >0.70 to 0.80         -> Good
      >0.80 to 0.90         -> Very Good
      >=0.90 and <1.00      -> Excellent
      1.00 (and above)      -> Excellent  (treated as top tier)

    If ratio is outside [0, 1], it is treated as 0..1 for safety.
    """
    # Normalize unexpected values into [0, 1]
    r = max(0.0, min(float(ratio), 1.0))

    if 0.0 <= r <= 0.60:
        return "Unacceptable"
    if 0.60 < r <= 0.70:
        return "Needs Improvement"
    if 0.70 < r <= 0.80:
        return "Good"
    if 0.80 < r < 0.90:
        return "Very Good"
    # >= 0.90
    return "Excellent"
