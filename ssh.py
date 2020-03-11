import spur
import paramiko
paramiko.SSHClient().set_missing_host_key_policy(paramiko.AutoAddPolicy())
shell = spur.SshShell(hostname='0.tcp.ngrok.io', port=14949,  username='pi', password='raspberry')
result = shell.run(["mkdir", "hello"])
print(result.output)