#!/usr/bin/env python
import paramiko
class Servers(object):
	def __init__(self,hostname,cmd):
		self.hostname=hostname
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname,username="root",password="redhat")
		stdin,stdout,stderr=ssh.exec_command(cmd)
		print stdout.readlines()
		ssh.close()

