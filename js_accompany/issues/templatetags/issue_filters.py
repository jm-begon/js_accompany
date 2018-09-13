from django import template
from ..models import Issue, StateChanged, StateValue, MessagePosted
from tags.models import Action, TagSomething

register = template.Library()


@register.filter
def owner_name(value):
    if isinstance(value, (Issue, Action)):
        return value.owner.username
    else:
        raise ValueError('Can only extract owner from {} or {}'
                         ''.format(Issue.__class__.__name__,
                                   Action.__class__.__name__))


@register.filter
def date(value):
    if isinstance(value, (Issue, Action)):
        return value.date
    else:
        raise ValueError('Can only extract date from {} or {}'
                         ''.format(Issue.__class__.__name__,
                                   Action.__class__.__name__))


@register.filter
def state(value):
    if isinstance(value, (Issue, StateChanged)):
        return value.state
    else:
        raise ValueError('Can only extract state from {} or {}'
                         ''.format(Issue.__class__.__name__,
                                   StateChanged.__class__.__name__))


@register.filter
def is_closed(value):
    if isinstance(value, StateChanged):
        return value.is_closed()
    elif isinstance(value, Issue):
        return value.state.is_closed()
    else:
        raise ValueError('Can only extract state from {} or {}'
                         ''.format(Issue.__class__.__name__,
                                   StateChanged.__class__.__name__))


@register.filter
def messages(value, update=False):
    if isinstance(value, Issue):
        return value.get_messages(update)
    else:
        raise ValueError('Can only get messages from {}'
                         ''.format(Issue.__class__.__name__))


@register.filter
def actions(value, update=False):
    if isinstance(value, Issue):
        return value.get_actions(update)
    else:
        raise ValueError('Can only get actions from {}, got {}'
                         ''.format(Issue.__class__.__name__,
                                   value.__class__.__name__))


@register.filter
def is_action_instance(value, action_cls_name=None):
    if not isinstance(value, Action):
        return False
    if action_cls_name is None:
        return True
    if action_cls_name == "StateChanged":
        return isinstance(value, StateChanged)
    elif action_cls_name == "MessagePosted":
        return isinstance(value, MessagePosted)
    elif action_cls_name == "TagSomething":
        return isinstance(value, TagSomething)
    else:
        return False


@register.filter
def remaining_tags(value):
    if isinstance(value, Issue):
        return value.get_remaining_tags()
    else:
        raise ValueError('Can only get remaining tags from \'\''
                         ''.format(Issue.__name__))


@register.filter
def string(value):
    return str(value)

