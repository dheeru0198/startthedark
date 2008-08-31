from django import template
from events.models import Attendance

def event(context, e, event_num=1):
    to_return = {
        'event': e,
        'request': context['request'],
        'event_num': event_num,
    }
    if context['user'].is_authenticated():
        try:
            Attendance.objects.get(event=e, user=context['user'])
            attending = True
        except Attendance.DoesNotExist:
            attending = False
        to_return.update({
            'attending': attending,
            'authenticated': True,
        })
    else:
        to_return.update({'authenticated': False})
    return to_return

register = template.Library()
register.inclusion_tag('events/event.html', takes_context=True)(event)