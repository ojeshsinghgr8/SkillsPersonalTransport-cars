#!/usr/bin/env python
import logging
import time
from typing import Optional, Union
import re
from scenario.main import actor
from df_engine.core import Actor, Context
from df_engine.core.keywords import GLOBAL,TRANSITIONS, RESPONSE
import df_engine.conditions as cnd
from annotators.main import annotate
from init_model import prepare_model
import scenario.condition as cust_cnd

plot = {
    "global": {
        "start": {
            RESPONSE: "",
            TRANSITIONS: {
                "intro": cnd.regexp(r"hi|hello", re.IGNORECASE),
            }
        },
        "intro": {
            RESPONSE: "Welcome, to our Car service catbot.\n We provide following services \n 1. Car Renting \n 2. Roadside Assistance \n 3. Car service".format(), 
            TRANSITIONS: {
                ("car_rental", "start"): cust_cnd.is_book_car,
                ("road_assistance", "start"): cust_cnd.is_road_assistance,
                ("car_service", "start"): cust_cnd.is_car_service,
            }
        },
        "fallback": {
            RESPONSE: "Oops!! something went wrong. Lets start again...",
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }
        }
    },
    "car_rental":{
        "start":{
            RESPONSE: "Welcome, to our Rental service.\n What type of car you want to rent SUV, Sedan or Hatchback".format(), 
            TRANSITIONS: {
                    ("car_rental", "suv"): cnd.regexp(r".*suv", re.IGNORECASE),
                    ("car_rental", "sedan"): cnd.regexp(r".*sedan", re.IGNORECASE),
                    ("car_rental", "hatchback"): cnd.regexp(r".*hatchback", re.IGNORECASE),                    
                }
        },
        "suv":{
            RESPONSE: "Great, we have following SUV ".format(), 
        },
        "sedan":{
            RESPONSE: "Great, we have following Sedan ".format(), 
        },
        "hatchback":{
            RESPONSE: "Great, we have following Hatchback ".format(), 
        }
       
    },
    "road_assistance":{
         "start":{
            RESPONSE: "Welcome, to our Roadside assistance service.".format(), 
           
        },
    },
    "car_service":{
         "start":{
            RESPONSE: "Welcome, to our car maintenance service.".format(), 
           
        },
    }
}

logger = logging.getLogger(__name__)

actor = Actor(plot, start_label=("global", "start"), fallback_label=("global", "fallback"))

def turn_handler(
    in_request: str,
    ctx: Union[Context, str, dict],
    actor: Actor,
    true_out_response: Optional[str] = None,
):
    # Context.cast - gets an object type of [Context, str, dict] returns an object type of Context
    ctx = Context.cast(ctx)

    # Add in current context a next request of user
    ctx.add_request(in_request)
    ctx = annotate(ctx)

    # pass the context into actor and it returns updated context with actor response
    ctx = actor(ctx)
    # get last actor response from the context
    out_response = ctx.last_response
    # the next condition branching needs for testing
    if true_out_response is not None and true_out_response != out_response:        
        raise Exception(f"{in_request} -> true_out_response != out_response: {true_out_response} != {out_response}")
    else:
        print(f"{in_request} -> {out_response}")
    return out_response, ctx

# interactive mode
def run_interactive_mode(actor):

    ctx = {}
    while True:
        in_request = input("type your answer: ")
        _, ctx = turn_handler(in_request, ctx, actor)

if __name__ == "__main__":
    ctx = {}
    cust_cnd.prepModel = prepare_model()
    # while True:
    #     in_request = input("type your answer: ")
    #     st_time = time.time()
    #     out_response, ctx = turn_handler(in_request, ctx, actor)
    #     total_time = time.time() - st_time
    #     print(f"exec time = {total_time:.3f}s")
    logging.basicConfig(
        format="%(asctime)s-%(name)15s:%(lineno)3s:%(funcName)20s():%(levelname)s - %(message)s", level=logging.INFO
    )
    # run_test()
    run_interactive_mode(actor)