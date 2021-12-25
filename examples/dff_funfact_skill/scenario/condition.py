import logging
import re

from df_engine.core import Actor, Context


FUNFACT_COMPILED_PATTERN = re.compile(
    r"(funfact|fun fact|tell me something fun|tell something interesting|"
    "tell me something interesting|^interesting fact.*)",
    re.IGNORECASE,
)

logger = logging.getLogger(__name__)


def random_funfact_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return bool(FUNFACT_COMPILED_PATTERN.search(request))


def another_funfact_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return bool("other" in request or ctx.misc.get("yes_intent"))
