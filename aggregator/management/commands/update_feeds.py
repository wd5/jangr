# -*- coding: utf-8 -*-
import datetime, hashlib, feedparser

from django.core.management.base import BaseCommand, CommandError
from aggregator.models import Feed, FeedPost
from unidecode import unidecode


class Command(BaseCommand):
	args = ''
	help = 'Updates all feeds'

	def handle(self, *args, **options):
		all_feeds = Feed.objects.all()
		
		self.stdout.write('Updating feeds...\n')
		
		for f in all_feeds:
			self.stdout.write('\n\n' + f.title + ' (' + f.feed_url + ')\n')
			parsed = feedparser.parse(f.feed_url)
			
			new_posts = 0
			
			for e in parsed.entries:
				h = hashlib.new('md5')
				
				h.update(unidecode(f.title))
				h.update(unidecode(f.feed_url))
				h.update(unidecode(e.title))
				h.update(unidecode(e.link))
				h.update(unidecode(e.description))
				digest = h.hexdigest()
				
				post = FeedPost.objects.filter(hash=digest)
				if len(post) == 0:
			
					new_posts += 1
					
					post = FeedPost()
					post.from_feed = f
					post.title = e.title
					post.url = e.link
					post.description = e.description
					post.date = datetime.datetime.now()
					post.hash = digest
					
					if not f.moderate:
						post.published = True
						
					
					post.save()
					#self.stdout.write(u'* ' + e.title + '\n  ' + e.link + ' :: \n')
					#self.stdout.write(u'* ' + e.title + '\n  ' + e.link + ' :: '+unicode(digest)+'\n')
				
			self.stdout.write(unicode(new_posts) + u' new posts in ' + f.title + u'\n\n')
				
			f.save()