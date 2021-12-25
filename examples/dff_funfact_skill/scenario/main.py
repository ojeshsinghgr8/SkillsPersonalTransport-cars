import df_engine.conditions as cnd
from df_engine.core import Actor
from df_engine.core.keywords import LOCAL, RESPONSE, TRANSITIONS


import scenario.condition as loc_cnd
import scenario.response as rsp

plot = {
    "service": {
        LOCAL: {
            TRANSITIONS: {
                ("funfact", "random"): loc_cnd.random_funfact_condition,
            }
        },
        "start": {RESPONSE: ""},
        "fallback": {RESPONSE: "Sorry"},
    },
    "funfact": {
        "random": {
            RESPONSE: rsp.random_funfact_response,
            TRANSITIONS: {
                ("funfact", "random"): cnd.any([loc_cnd.random_funfact_condition, loc_cnd.another_funfact_condition])
            },
        },
    },
}

actor = Actor(plot, start_label=("service", "start"), fallback_label=("service", "fallback"))
