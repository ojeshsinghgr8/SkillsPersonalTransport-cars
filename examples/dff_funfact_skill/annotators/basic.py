import re

from df_engine.core import Context

yes_regexp = re.compile(r"\byes\b")


def yes_intent(ctx: Context):
    if yes_regexp.search(ctx.last_request):
        ctx.misc["yes_intent"] = bool(yes_regexp.search(ctx.last_request))
    return ctx


no_regexp = re.compile(r"\bno\b")


def no_intent(ctx: Context):
    if no_regexp.search(ctx.last_request):
        ctx.misc["no_intent"] = bool(no_regexp.search(ctx.last_request))  # сохранение интента в контекст
    return ctx
