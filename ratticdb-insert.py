# 2014 copyright Guilherme Thomazi (thomazi@linux.com)
# Released under the GPL v2 

import os, pymysql

conn = pymysql.connect(host='104.131.201.135', port=3306, user='rattic', passwd='bnd0h2hg', db='rattic')
cur = conn.cursor()

def add(title, username, password, description, group_id, url):
	query_insert = """
		insert into cred_cred(title, username, password, description, group_id, is_deleted, url, latest_id, created, iconname, descriptionmarkdown, modified, attachment, attachment_name)
		values ('%s', '%s', '%s', '%s', %d, 0, '%s', NULL, NOW(), 'Key.png', 0, NOW(), '', NULL);""" % (title, username, password, description, group_id, url)
	cur.execute(query_insert)


title = raw_input("title: ")
username = raw_input("username: ")
password = raw_input("password: ")
description = raw_input("description: ")
group_id = raw_input("group_id: ")
url = raw_input("url: ")


add(title, username, password, description, int(group_id), url)

cur.close()
conn.close()

