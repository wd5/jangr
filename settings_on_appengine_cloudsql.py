import os

GAE_SETTINGS_MODULES = (
	'gae_settings',
)

DATABASES = {
	'default': {
		'ENGINE': 'google.appengine.ext.django.backends.rdbms',
		'INSTANCE': 'jangr-db:jangr-db',
		'NAME': 'jangr',
	}
}

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
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


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '_media')
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

IS_LESS = True