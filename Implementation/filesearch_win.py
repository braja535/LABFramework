# http://stackoverflow.com/questions/5153317/python-how-to-do-a-system-wide-search-for-a-file-when-just-the-filename-not-pa

import os
from os.path import join

filename = "*"
#for root, dirs ,files in os.walk('C:\\Users\\badan\\PycharmProjects\\LABFramework'):

    print "searching", root
    if filename in files:
        print "found : %s " % join(root,filename)
        #break

#lookfor = "#"
#for root, dirs, files in os.walk('C:\\'):
#    print "searching", root
#    if lookfor in files:
#        print "found: %s" % join(root, lookfor)
#        break

# import os
# import sys
# import magic
# import time
# import fnmatch
#
# class FileInfo(object):
#
#     def __init__(self, filepath):
#         self.depth = filepath.strip('/').count('/')
#         self.is_file = os.path.isfile(filepath)
#         self.is_dir = os.path.isdir(filepath)
#         self.is_link = os.path.islink(filepath)
#         self.size = os.path.getsize(filepath)
#         self.meta = magic.from_file(filepath).lower()
#         self.mime = magic.from_file(filepath, mime=True)
#         self.filepath = filepath
#
#
#     def match(self, exp):
#         return fnmatch.fnmatch(self.filepath, exp)
#
#     def readfile(self):
#         if self.is_file:
#             with open(self.filepath, 'r') as _file:
#                 return _file.read()
#
#     def __str__(self):
#         return str(self.__dict__)
#
#
#
# def get_files(root):
#
#     for root, dirs, files in os.walk(root):
#
#         for directory in dirs:
#             for filename in directory:
#                 filename = os.path.join(root, filename)
#                 if os.path.isfile(filename) or os.path.isdir(filename):
#                     yield FileInfo(filename)
#
#         for filename in files:
#             filename = os.path.join(root, filename)
#             if os.path.isfile(filename) or os.path.isdir(filename):
#                 yield FileInfo(filename)
#
#
# for this in get_files('/home/ricky/Code/Python'):
#     if this.match('*.py'):
#         print this.filepath#