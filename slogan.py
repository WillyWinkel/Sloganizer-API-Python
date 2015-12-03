#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import cgi
import HTMLParser
import random

def main(wort):
    url = "http://www.sloganizer.net/outbound.php?slogan=" + wort
    r = urllib2.urlopen(url).read()[103:-4]
    r = r.replace('&amp;', "&")
    r = r.replace('&auml;', "ä")
    r = r.replace("&uuml;", "ü")
    r = r.replace("&ouml;", "ö")
    r = r.replace("&szlig;", "ß")
    r = r.replace('&acute;', "'")
    print
    print "         " + r
    print


r = ["Säure", "Sex", "Frauen", "Star-Wars", "Essen", "Spaß", "Batman", "Lesen"]
try:
    main(random.choice(r))
except Exception, e:
    pass
else:
    pass
finally:
    pass
