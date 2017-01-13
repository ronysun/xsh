import paramiko
import interactive

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.107.52', username='root',password='aaaaaa')
channel = ssh.invoke_shell()
interactive.interactive_shell(channel)
channel.close
ssh.close