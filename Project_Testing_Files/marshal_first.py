
data = {12:'twelve','feep':list('ciao'),1.23:4+5j,(1,2,3):u'wer'}

import marshal
bytes = marshal.dumps(data)
#print bytes

#redata = marshal.loads(bytes)
#print redata

ouf = open('datafile','wb')
marshal.dump(data,ouf)
marshal.dump('some string',ouf)
marshal.dump(range(19),ouf)
ouf.close()

inf = open('datafile','rb')
a= marshal.load(inf)
b= marshal.load(inf)
c= marshal.load(inf)

inf.close()

print a
print b
print c

