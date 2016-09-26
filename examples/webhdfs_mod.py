#!/usr/bin/python

import os
import subprocess

webhdfs_ip = raw_input("Please enter ip address of WebHdfs server with port number:")
user_name = raw_input("Please enter your user name:")
print '''Various WebHdfs operations with ID:

(1) upload file 
(2) append data
(3) read file
(4) make directory
(5) rename file or directory
(6) delete file or directory
(7) get file file
(8) list items in the directory
(9) summary of directory contents
(10) get file checksome
(11) get home directory
(12) set permission
(13) change owner
(14) set replication factor

'''

operation = int(raw_input("Please enter your Operation number from above list: "))

if operation == 1:

	input_path = raw_input("Please enter your input path: ")
	hdfs_path = raw_input("Please enter your HDFS path: ")
	overwrite = raw_input("Do you want to overwrite existing data? true or false: ")
	url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=CREATE&overwrite=" + overwrite + "&user.name=" + user_name + "'"
	A = os.popen(url).read()
	B = A.split()
	for b in B:
		if b.find('webhdfs') != -1:
			url = b

	c = 'curl -i -H "Content-Type:application/octet-stream" -X PUT -T ' + input_path
	URL =  c + ' "' +url + '"'
	os.system(URL)

elif operation == 2:

	input_path = raw_input("Please enter your input path: ")
	hdfs_path = raw_input("Please enter your HDFS path: ")
	url = "curl -i -X POST 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=APPEND&user.name=" + user_name + "'"
	A = os.popen(url).read()
	B = A.split()
	for b in B:
		if b.find('webhdfs') != -1:
			url = b

	c = 'curl -i -H "Content-Type:application/octet-stream" -X POST -T ' + input_path
	URL =  c + ' "' +url + '"'
	os.system(URL)

elif operation == 3:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	url = "curl -i -L 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=OPEN&user.name=" + user_name + "'"
	os.system(url)

elif operation == 4:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=MKDIR&user.name=" + user_name + "'"
	os.system(url)

elif operation == 5:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	new_name = raw_input("Please enter new name of the file: ")
	url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=RENAME&destination=" + new_name + "&user.name=" + user_name + "'"
	os.system(url)

elif operation == 6:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	url = "curl -i -X DELETE 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=DELETE&user.name=" + user_name + "'"
	os.system(url)

elif operation == 7:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=GETFILESTATUS&user.name=" + user_name + "'"
	os.system(url)

elif operation == 8:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=LISTSTATUS&user.name=" + user_name + "'"
	os.system(url)

elif operation == 9:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=GETCONTENTSUMMARY&user.name=" + user_name + "'"
	os.system(url)

elif operation == 10:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=GETFILECHECKSUM&user.name=" + user_name + "'"
	os.system(url)

elif operation == 11:

	url = "curl -i 'http://" + webhdfs_ip + "/webhdfs/v1?op=GETHOMEDIRECTORY&user.name=" + user_name + "'"
	os.system(url)

elif operation == 12:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	permission = raw_input("Please enter new permission: ")
	url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=SETPERMISSION&user.name=" + user_name + "&permission=" + permission + "'"
	os.system(url)

elif operation == 13:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	owner = raw_input("Please enter new owner name: ")
	group = raw_input("Please enter new group name: ")
	url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=SETOWNER&user.name=" + user_name + "&owner=" + owner + "&group=" + group + "'"
	os.system(url)

elif operation == 14:

	hdfs_path = raw_input("Please enter your HDFS path: ")
	replication_factor = raw_input("Please enter replication factor: ")
	url = "curl -i -X PUT 'http://" + webhdfs_ip + "/webhdfs/v1" + hdfs_path + "?op=SETREPLICATION&user.name=" + user_name + "&replication=" + replication_factor + "'"
	os.system(url)