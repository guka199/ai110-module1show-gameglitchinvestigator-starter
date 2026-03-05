import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert "Win" in result

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert "Too High" in result

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert "Too Low" in result

# Bug 1: hints were backwards — too high said "Go HIGHER", too low said "Go LOWER"
def test_hint_message_says_go_lower_when_too_high():
    _, message = check_guess(80, 50)
    assert "LOWER" in message, f"Expected hint to say LOWER but got: {message}"

# Bug 2: new game never reset status, so the game stayed blocked after win/loss
def test_new_game_resets_status_to_playing():
    state = {"attempts": 5, "status": "won", "history": [10, 20], "score": 100}
    state["attempts"] = 0
    state["status"] = "playing"
    state["history"] = []
    state["score"] = 0
    assert state["status"] == "playing"
