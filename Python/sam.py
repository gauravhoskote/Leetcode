import urllib.request

fp = urllib.request.urlopen("http://medium.com/@gaurav_hoskote/top-machine-learning-courses-that-are-too-good-to-be-free-14eacee6391f")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
