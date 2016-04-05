import marshal

"""   Conver the input to string """
# string = '"{}"'.format(input("Enter string for Byte variable "))

import sys

string = {12: 'twelve', 'feep': list('ciao'), 1.23: 4 + 5j, (1, 2, 3): u'wer'}
print string
bytes = marshal.dumps(string)
print bytes
reconstruct = marshal.loads(bytes)
print reconstruct
