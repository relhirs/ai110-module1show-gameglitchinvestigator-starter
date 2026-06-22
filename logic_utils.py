# Fix: i identified that logic and UI were tangled in app.py; AI extracted all pure functions into this module.

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # AI moved this out of app.py so it can be tested without importing streamlit.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def get_attempt_limit(difficulty: str) -> int:
    """Return the number of allowed attempts for a given difficulty."""
    # i noticed the inline dict in app.py was logic, not UI; AI turned it into a named function.
    limits = {"Easy": 6, "Normal": 8, "Hard": 5}
    return limits.get(difficulty, 8)


def get_attempts_left(attempt_limit: int, attempts_used: int) -> int:
    """Return attempts remaining, clamped to 0."""
    # i reported the counter went negative after the last guess; AI added the max(0,...) clamp and extracted it here so it could be unit-tested.
    return max(0, attempt_limit - attempts_used)


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # AI moved this out of app.py; i confirmed it belongs in logic, not the UI layer.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Fix: original AI-generated code had the hints backwards ("Go HIGHER" when too high).
    # i caught the bug; AI swapped the messages to match the correct direction.
    if guess == secret:
        return "Win", "🎉 Correct!"
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # AI moved this out of app.py; i confirmed the scoring rules should live in logic, not the UI.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
