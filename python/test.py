import os
import re
import sys
from os import path


def skip_dir(path,extensions=['*']):
	"""skip all the files under the path """
	print extensions 
	filelist=[]
	for root,dirs,files in os.walk(path):
		for subfile in files:
			filename,extension=os.path.splitext(subfile)
			print filename,extension
			if extension in extensions:
				filelist +=os.path.join(root,subfile)
	return filelist
	
def findsysinclude(filename,includepath):
	"""find he header file in the system inlcude path"""
	if filename ==None:
		return None
	sysincludepath=['/usr/include/','/usr/include/c++/4.4/']
	includepath +=sysincludepath
	for onepath in includepath:
		if path.isfile(onepath+filename):
			return onepath+filename
	print "not found :"+filename
	return None
def findfiles(path):
	"""find all the cpp files under the path"""
	retest=re.compile(r'\.cpp$|\.c$|\.hpp$|\.h$',re.IGNORECASE)
	cppfiles=[]
	for root,dirs,files in os.walk(path):
		oldlen=len(cppfiles)
		cppfiles +=filter(lambda x: retest.search(x)<>None,files)
		for index in range(oldlen,len(cppfiles)):
			cppfiles[index]=root+'/'+cppfiles[index]
	return cppfiles
def findincludename(path):
	"""search the certain header file name in the files under the path"""
	includetest=re.compile(r'\s*#include\s*((<(?P<sysincludefile>.*?)>)|("(?P<userincludefile>.*?)"))')
	cppfiles=findfiles(path)
	for cppfile in cppfiles:
		try:
			fp=open(cppfile,'r')
			print 'finding in file:'+cppfile
			for line in fp:
				result=includetest.search(line)
				if result <> None:
					print "match include line is:"+result.group()
					tmp=findsysinclude(result.group("sysincludefile"),args[1:])
					tmp2=findsysinclude(result.group("userincludefile"),args[1:])
					if tmp <>None and cppfiles.count(tmp)==0:
						cppfiles+=[tmp]
						print 'add sys files:'+tmp
					if tmp2 <>None and cppfiles.count(tmp2)==0:
						cppfiles+=[tmp2]
						print 'add user files:'+tmp2
		finally:
			fp.close()	
	return cppfiles
args=sys.argv
if __name__ == '__main__':
#	filelist=findsysinclude("unistd.h",["/home/zxlei/programming"])
#	head,tail=os.path.split(filelist)
#	print head,tail
#	print filelist
#	sysfilelist=findcppfiles("/home/zxlei/programming/")
#	print "\n"
#	for files in sysfilelist:
#		print files
	includefile=findincludename("/home/zxlei/programing")
	print includefile	
	system("ta")
