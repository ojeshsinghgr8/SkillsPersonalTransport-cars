from df_engine.core import Context
from .basic import yes_intent, no_intent

def annotate(ctx: Context):
    ctx = yes_intent(ctx)
    ctx = no_intent(ctx)
    return ctx
