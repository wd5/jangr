# -*- coding: utf-8 -*-
from util import admin
from forum.models import ForumSection

class ForumSectionAdmin(admin.ModelAdmin):
	list_display = ('name','slug','parent')
	pass	

admin.site.register(ForumSection, ForumSectionAdmin)