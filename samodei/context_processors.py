import datetime, settings

def samodeus_util(request):
	return {
		'now':		datetime.datetime.now(),
		'today':	datetime.datetime.today(),
		'is_css':	not settings.IS_LESS,
		'is_less':	settings.IS_LESS,
	}