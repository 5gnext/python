import paramiko
import time
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_client.connect(hostname='10.1.1.1', port='22', username='admin', password='admin', look_for_keys=False, allow_agent=False)
router1 = {'hostname': '10.1.1.1', 'port': '22', 'username': 'admin', 'password': 'admin'}
router2 = {'hostname': '10.1.1.3', 'port': '22', 'username': 'admin', 'password': 'admin'}
routers = [router1, router2]
for router in routers:
    print(f'connecting to {router.get("hostname")}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    #print(ssh_client.get_transport().is_active())
    shell = ssh_client.invoke_shell()
    shell.send('term length 0\n')
    shell.send('show version\n')
    time.sleep(1)
    output = shell.recv(50000).decode()
    #print(type(output))
    #output = output.decode('utf-8')
    print(output)
if ssh_client.get_transport().is_active() == True:
    print('closing connection')
    ssh_client.close()