import paramiko


# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='10.30.161.84', port=22, username='root', password='1')
# stdin, stdout, stderr = ssh.exec_command('ip a')
#ssh.close()

trans = paramiko.Transport(('10.30.161.84', 22))
trans.connect(username='root', password='1')
ssh = paramiko.SSHClient()
ssh._transport = trans
a, b, c = ssh.exec_command('ip a')

sftp = paramiko.SFTPClient.from_transport(trans)

sftp.put('/opt/a', '/tmp/a')

#sftp.get('/tmp/ssh-key.py', 'ssh-key.txt')

print(b.read().decode())
trans.close()



# pkey = paramiko.RSAKey.from_private_key_file('yxsyxs')
# #建立连接
# ssh = paramiko.SSHClient()
# #允许将信任的主机自动加入到known_hosts列表
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='10.30.161.84',port=22,username='root',pkey=pkey) #指定密钥连接
# #执行命令
# stdin,stdout,stderr=ssh.exec_command('free -m')
# print(stdout.read().decode())
# ssh.close()








