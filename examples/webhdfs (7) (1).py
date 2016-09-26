#!/usr/bin/python

import os
import subprocess
import sys

webhdfs_ip = sys.argv[1]
user_name = "hdfs"
number_of_files = 3
file_size = 102400

with open("testfile1.txt", "wb") as f:
	f.write("cazena " * file_size)
with open("testfile2.txt", "wb") as f:
	f.write("cazena " * file_size)
with open("testfile3.txt", "wb") as f:
	f.write("cazena " * file_size)

### get home directory
print "get home directory"
url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1?op=GETHOMEDIRECTORY&user.name=" + user_name + "'"
os.system(url)

### make directory
print "creating /user/hdfs/cazena directory"
hdfs_path = "/user/hdfs/cazena"
url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=MKDIRS&user.name=" + user_name + "'"
os.system(url)

### Upload file
print "uploading files"
a = 1
input_path = []
while a <= number_of_files :
	input_path.append("testfile{0}.txt".format(a))
	a = a + 1

a = 1
hdfs_path = []
while a <= number_of_files :
	hdfs_path.append("/user/hdfs/cazena/testfile{0}.txt".format(a))
	a = a + 1

overwrite = 'true'

a = 1
while a <= number_of_files :
	url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path[a-1] + "?op=CREATE&overwrite=" + overwrite + "&user.name=" + user_name + "'"
	A = os.popen(url).read()
	B = A.split()
	for b in B:
		if b.find('webhdfs') != -1:
			url = b

	c = 'curl -i -H "Content-Type:application/octet-stream" -X PUT -T ' + input_path[a-1]
	URL =  c + ' "' +url + '"'
	os.system(URL)
	a = a + 1

### Append data
print "append data"
input_path = "testfile1.txt"
hdfs_path = "/user/hdfs/cazena/testfile1.txt"
url = "curl -i -X POST 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=APPEND&user.name=" + user_name + "'"

A = os.popen(url).read()
B = A.split()
for b in B:
	if b.find('webhdfs') != -1:
		url = b

c = 'curl -i -H "Content-Type:application/octet-stream" -X POST -T ' + input_path
URL =  c + ' "' +url + '"'
os.system(URL)

### Read file
print "open file testfile1.txt"
hdfs_path = "/user/hdfs/cazena/testfile1.txt"
url = "curl -i -L 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=OPEN&user.name=" + user_name + "'"
os.system(url)

### list items in the directory
print "list items in the /user/hdfs/cazena directory"
hdfs_path = "/user/hdfs/cazena"
url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=LISTSTATUS&user.name=" + user_name + "'"
os.system(url)

### summary of directory contents
print "summary of the /user/hdfs/cazena directory"
hdfs_path = "/user/hdfs/cazena"
url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=GETCONTENTSUMMARY&user.name=" + user_name + "'"
os.system(url)

### get file status
print "get file status of testfile1.txt"
hdfs_path = "/user/hdfs/cazena/testfile1.txt"
url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=GETFILESTATUS&user.name=" + user_name + "'"
os.system(url)

### get file checksome
print "get file checksum of testfile1.txt"
hdfs_path = "/user/hdfs/cazena/testfile1.txt"
url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=GETFILECHECKSUM&user.name=" + user_name + "'"
os.system(url)

### rename file or directory
print "renaming testfile1.txt to cazena.txt"
hdfs_path = "/user/hdfs/cazena/testfile1.txt"
new_name = "/user/hdfs/cazena/cazena.txt"
url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=RENAME&destination=" + new_name + "&user.name=" + user_name + "'"
os.system(url)

### delete file or directory
print "delete file cazena.txt"
hdfs_path = "/user/hdfs/cazena/cazena.txt"
url = "curl -i -X DELETE 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=DELETE&user.name=" + user_name + "'"
os.system(url)

### set replication factor
print "set replication factor of testfile2.txt to 3"
hdfs_path = "/user/hdfs/cazena/testfile2.txt"
url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=SETREPLICATION&user.name=" + user_name + "&replication=3'"
os.system(url)

### set permission
print "set file permission of testfile2.txt to 777"
hdfs_path = "/user/hdfs/cazena/testfile2.txt"
url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=SETPERMISSION&user.name=" + user_name + "&permission=777'"
os.system(url)

### change owner
print "change owner of testfile2.txt from hdfs to hive"
hdfs_path = "/user/hdfs/cazena/testfile2.txt"
owner = "hive"
group = "hive"
url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=SETOWNER&user.name=" + user_name + "&owner=" + owner + "&group=" + group + "'"
os.system(url)