# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

GAE_SETTINGS_MODULES = (
	'gae_settings',
)

DATABASES = {
	'default': {
		'ENGINE': 'dbindexer',
		'TARGET': 'gae',
	},
	'gae': {
		'ENGINE': 'djangoappengine.db',
		'HIGH_REPLICATION': True, 

		'DEV_APPSERVER_OPTIONS': { 
			'high_replication' : True, 
			'use_sqlite': True, 
		} 
	},
}
AUTOLOAD_SITECONF = 'dbindexes'

DBINDEXER_BACKENDS = (
	'dbindexer.backends.BaseResolver',
	'dbindexer.backends.FKNullFix',
	'dbindexer.backends.InMemoryJOINResolver',
)

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

MIDDLEWARE_CLASSES = (
	# This loads the index definitions, so it has to come first
	'autoload.middleware.AutoloadMiddleware',
	
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
	'autoload',
	'dbindexer',
	'djangotoolbox',
	
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	#'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	# 'django.contrib.admindocs',
	'django.contrib.comments',
	'django.contrib.markup',
	
	# 'south', # south 0.7.3 -- schema migration manager
	# 'compressor', # django_compressor
	'sorl.thumbnail', # image thumbnailer
	'genericm2m', # generic many-to-many relations
	# 'mptt', # trees
	# 'django-registration', # user signup
	# 'tagging',
	# 'easy_maps',
	# 'feedjack', # feed aggregation
	
	'util', # global utilities
	'samodei', # homepage, global info (cities)
	'users', # user profiles
	'mycomments', # comment customization
	'documents',
	'archive',
	'newsevents',
	'aggregator',
	'catalog',
	'forum',
	
	'djangoappengine', # djangoappengine should come last, so it can override a few manage.py commands
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.core.context_processors.request",
	"samodei.context_processors.samodeus_util"
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'


ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)


ROOT_URLCONF = 'urls'


MEDIA_ROOT = 'D:/Web/Projects/jangr-appengine/jangr-app/jangr/_media'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), '_sitestatic')
STATICFILES_DIRS = (
	
	os.path.join(os.path.dirname(__file__), '_static'),
)
if DEBUG: 
	STATIC_URL = '/devstatic/'
	MEDIA_URL = '/devmedia/'
else:
	STATIC_URL = '/static/'
	MEDIA_URL = '/media/'

	
COMMENTS_APP = 'mycomments'
AUTH_PROFILE_MODULE = 'users.UserProfile'


SITE_ID = 1


IS_LESS = not False 