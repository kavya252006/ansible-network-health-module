
#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import socket
import subprocess

def ping_host(host):
    result=subprocess.run(
            ["ping","-c","1",host],
            capture_output=True         #subprocess returns completedprocess named object and it is stored in variable named result and it contains attributes like stdout,stderr,returncode
    )

    return result.returncode==0

def check_port(host,port):
    sock=socket.socket(
            socket.AF_INET, #ipv4
            socket.SOCK_STREAM #TCP
    )

    sock.settimeout(3)
    result=sock.connect_ex((host,port))
    sock.close()
    return result==0

def run_module():
    module_args=dict(
            host=dict(type='str',required=True),
            port=dict(type='int',required=True)
    )

    module=AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
    )
    
    host=module.params['host']
    port=module.params['port']

    ping_status=ping_host(host)
    port_status=check_port(host,port)

    result=dict(
            changed=False,
            ping_reachable=ping_status,
            port_open=port_status,

            checked_host=host,
            checked_port=port
    )

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

