# -*- coding: utf-8 -*-

from django import template
import datetime, calendar

register = template.Library()
		
	
class CalendarNode(template.Node):
	def __init__(self):
		pass
		
	def render(self, context):
		now = datetime.date.today()
		
		today = now.day
		month = now.month
		
		first_day_of_month = now.replace(day=1)
		first_monday = first_day_of_month - datetime.timedelta(days=first_day_of_month.weekday())
		
		cal = calendar.Calendar().monthdatescalendar(now.year,now.month)
		
		output = u''
		
		output += u'<ul class="events-calendar">'
		
		for i in cal:
			for j in i:
				output += \
					u'<li><a href="#" class="' + \
					(u" this-month" if j.month==now.month else u" other-month") + \
					(u" weekend" if j.weekday()==5 or j.weekday()==6 else "") + \
					(u" today" if j==now else u"") + \
					'">' + \
					unicode(j.day)+u'<div class="calendar-events"><!--&#9733;8-->&nbsp;</div></a></li>'
				
		output += u'</ul>'
		
		return output


@register.tag		
def draw_calendar(parser,token):
	return CalendarNode()