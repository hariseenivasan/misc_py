#!/usr/bin/env python
#Reference: https://community.spiceworks.com/scripts/show/982-download-all-dilbert-comics (doesn't work)
import sys, datetime, os, time

# for backwards compatibility
if sys.version_info[0] > 2:
	import urllib.request as ul
else:
	import urllib as ul

def strip(y = datetime.datetime.now().year, m = datetime.datetime.now().month, d = datetime.datetime.now().day, save_as = ''):
	# if no filename specified or if directory
	try:
		# str() faster than decode() when converting from byte array to string
		myhtml = str(ul.urlopen('http://dilbert.com/fast/%04d-%02d-%02d' % (y, m, d)).read())
		# start search at 1000 since dyn is located around 1100-1400
		twit_pos = myhtml.find('twitter:image', 1000)
		if twit_pos != -1:
			mygif = myhtml[twit_pos+24 : myhtml.find('>', twit_pos)-1] 
			return ul.urlretrieve(mygif, str('%s\%04d-%02d-%02d.gif' % (save_as,y, m, d)))[0]
	except:
		return None

# 4-17-89 == first Dilbert
def strips(begin = datetime.date(1989, 4, 17), end = datetime.datetime.now().date(), save_loc = '', delay = 0.12):
	try:
		if save_loc != '' and not(os.path.isdir(save_loc)):
			os.makedirs(save_loc)
	except:
		save_loc = ' '
	y = begin.year
	m = begin.month
	d = begin.day
	y_lim = end.year + 1
	m_lim = 13
	d_lim = 32
	while y < y_lim:
		if y == end.year:
			m_lim = end.month + 1
		while m < m_lim:
			if y == end.year and m == end.month:
				d_lim = end.day + 1
			while d < d_lim:
				print(strip(y, m, d, save_loc))
				time.sleep(delay)
				d += 1
			d = 1
			m += 1
		m = 1
		y += 1

if __name__ == '__main__':
	strips(save_loc = 'c:\dilbert')
