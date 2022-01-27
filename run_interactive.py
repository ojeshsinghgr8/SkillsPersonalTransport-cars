#!/usr/bin/env python
import logging
import time
from typing import Optional, Union
import re
from scenario.main import actor
from df_engine.core import Actor, Context


from annotators.main import annotate
from init_model import prepare_model
import scenario.condition as cust_cnd
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

logger = logging.getLogger(__name__)



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
    print("Training model")
    cust_cnd.prepModel = prepare_model()
    print("Training model complited")
    clearConsole()
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