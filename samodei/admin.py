# -*- coding: utf-8 -*-
from util import admin
from samodei.models import City

class CityAdmin(admin.ModelAdmin):
	pass

admin.site.register(City, CityAdmin)