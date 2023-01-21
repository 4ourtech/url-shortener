import pyshorteners as sh
link = 'https://www.youtube.com/@4ourtech'
s = sh.Shortener()

print(s.tinyurl.short(link))

