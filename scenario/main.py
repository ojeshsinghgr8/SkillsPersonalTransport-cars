from df_engine.core import Actor
from df_engine.core.keywords import RESPONSE


# TODO: extend graph
plot = {
    "service": {
        "start": {RESPONSE: ""},
        "fallback": {RESPONSE: "hi"},
    },
}

actor = Actor(plot, start_label=("service", "start"), fallback_label=("service", "fallback"))
