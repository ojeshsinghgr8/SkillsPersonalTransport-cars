import random

from scenario.main import actor
import run_interactive

random.seed(314)

# testing
testing_dialog = [
    ("hi", "Sorry"),
    (
        "funfact",
        "Some sea snakes can breathe through their skin. Would you like to hear another fun fact?",
    ),
    ("yes", "A 2007 study found that music, classical in particular, can help make plants grow faster. Would you like to hear another fun fact?"),
]


def run_test():
    ctx = {}
    for in_request, true_out_response in testing_dialog:
        _, ctx = run_interactive.turn_handler(in_request, ctx, actor, true_out_response=true_out_response)
    print("test passed")


if __name__ == "__main__":
    run_test()
