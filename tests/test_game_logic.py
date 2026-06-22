from logic_utils import check_guess, get_attempt_limit, get_attempts_left

def test_attempts_left_shows_zero_when_exhausted():
    # i reported the UI showed "-1 attempts left"; AI wrote this test to pin the clamped-to-zero behavior.
    for difficulty in ["Easy", "Normal", "Hard"]:
        limit = get_attempt_limit(difficulty)
        assert get_attempts_left(limit, limit) == 0
        assert get_attempts_left(limit, limit + 1) == 0


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
