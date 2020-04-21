
import paramiko
from config import *
class Sshd(object):
	def __init__(self,hostname,
			passwd,
			username='root',
			port=22):
		self.hostname = hostname
		self.passwd = passwd
		self.username=username
		self.port=port

		self.obj=paramiko.Transport((self.hostname,self.port))
		self.obj.connect(username=self.username,password=self.passwd)
		self.ssh = paramiko.SSHClient()
		self.ssh._transport = self.obj
		self.sftp=paramiko.SFTPClient.from_transport(self.obj)
	def op_ssh(self,cmd):
		stdin,stdout,stderr = self.ssh.exec_command(cmd)
		stdout = str(stdout.read().decode())
		stderr = str(stderr.read().decode())
		if stdout:
			return stdout
		else:
			return stderr
	def op_ftp_push(self,froms,tos):
		self.sftp.put(froms,tos)
		return True
	def op_ftp_pull(self,froms,tos):
		self.sftp.get(froms,tos)
		return True
	def close(self):
		self.sftp.close()
		self.obj.close()
	def __str__(self):
		return 'QianFeng cloud computing testing'


if __name__ == '__main__':
    abc = Sshd(hostname='10.30.161.84', passwd='1')
    abc.op_ftp_push('/opt/nginx.conf', '/opt/a')
    s = abc.op_ssh('cat /etc/passwd')
    print(s)
    abc.close()



























