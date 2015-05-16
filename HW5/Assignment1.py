# Web crawler by title, identifier and content-owner

import urllib.request
from urllib.error import  URLError
import re


def visit_url(url, domain):
	global crawler_backlog
	if(len(crawler_backlog)>100):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("Processing:", url)
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		if(code == 200):
			content=page.read()
			content_string = content.decode("utf-8")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>') # for title
			regexp_identifier = re.compile('<meta name="identifier" content="(?P<identifier>(\d*))" />') # for identifier
			regexp_contentowner = re.compile('<meta name="content-owner" content="(?P<contentowner>([\w\s]+))" />') # for content-owner
			regexp_url = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_title.search(content_string, re.IGNORECASE)
                        
			if result:
				title = result.group("title") # group by title
				print(title)

			result = regexp_identifier.search(content_string, re.IGNORECASE)

			if result:
				identifier = result.group("identifier") # group by identifier
				print(identifier)

			result = regexp_contentowner.search(content_string, re.IGNORECASE)

			if result:
				contentowner = result.group("contentowner") # group by content-owner
				print(contentowner)

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain)
	except URLError as e:
		print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")
