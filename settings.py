BACKEND = 'appengine-cloudsql'

if BACKEND == 'appengine-nonrel':
	from settings_on_appengine_nonrel import *
elif BACKEND == 'appengine-cloudsql':
	from settings_on_appengine_cloudsql import *