Must have ssh access to EC2 instance to run this.

Route 53 must have domain_name A record pointed to EC2 instance.

Playbook also assumes user is ubuntu.

/etc/ansible/hosts should be set up like this:

[servergroup]
[sub-domain.example.com] ansible_python_interpreter=/usr/bin/python3 domain_name=sub-domain.example.com env_file=/path/to/your/env/secrets/
