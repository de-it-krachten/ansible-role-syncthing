[![CI](https://github.com/de-it-krachten/ansible-role-syncthing/workflows/CI/badge.svg?event=push)](https://github.com/de-it-krachten/ansible-role-syncthing/actions?query=workflow%3ACI)


# ansible-role-syncthing

<basic role description>



## Dependencies

#### Roles
None

#### Collections
- community.general

## Platforms

Supported platforms

- Red Hat Enterprise Linux 8<sup>1</sup>
- Red Hat Enterprise Linux 9<sup>1</sup>
- Red Hat Enterprise Linux 10<sup>1</sup>
- RockyLinux 8
- RockyLinux 9
- RockyLinux 10
- OracleLinux 8
- OracleLinux 9
- OracleLinux 10
- AlmaLinux 8
- AlmaLinux 9
- AlmaLinux 10
- Debian 11 (Bullseye)
- Debian 12 (Bookworm)
- Debian 13 (Trixie)
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Ubuntu 26.04 LTS
- Fedora 43
- Fedora 44<sup>1</sup>

Note:
<sup>1</sup> : no automated testing is performed on these platforms


## Role Variables
### defaults/main.yml
<pre><code>
# API URI
syncthing_api_url: http://127.0.0.1:8384

# User that will start the syncthing service
syncthing_user: syncthing

# service
syncthing_service: syncthing@{{ syncthing_user }}.service

# Execute in Docker
syncthing_docker: false

# Synthing command
syncthing_cmd: syncthing

# Server that should be used as master
syncthing_master: master

# Client that sync through master
syncthing_clients: []

syncthing_gui_patch:
  gui:
    address: "0.0.0.0:8384"
    user: admin
    password: "{{ admin_password | default('admin', true) }}"
  options:
    urAccepted: 3
    urSeen: 3

# Perform software install only
syncthing_install_only: false
</pre></code>

### defaults/family-Debian.yml
<pre><code>
# List of packages
syncthing_packages:
  - syncthing
  - python3-lxml
  # - jq
  # - moreutils
</pre></code>

### defaults/family-RedHat.yml
<pre><code>
# List of packages
syncthing_packages:
  - syncthing
  - python3-lxml
  # - jq
  # - moreutils
</pre></code>

### defaults/family-Suse.yml
<pre><code>
# List of packages
syncthing_packages:
  - syncthing
  - python3-lxml
  # - jq
  # - moreutils
</pre></code>




## Example Playbook
### molecule/default/converge.yml
<pre><code>
- name: sample playbook for role 'syncthing'
  hosts: all
  become: 'yes'
  vars:
    syncthing_user: syncthing
    syncthing_folders:
      - id: f2c6b06bf7d0bc8f6471e3c97933dd421cf9e864
        label: test01
        path: '{{ syncthing_home }}/test01'
      - id: 534e995fef5b8e236deffa878228172dad0578e1
        label: test02
        path: '{{ syncthing_home }}/test02'
        encryption_password: BNaFIsMKcpD+yhzv+zNLP4b8VG5CyWnKPSXchLhBNOs=
  tasks:
    - name: Include role 'syncthing'
      ansible.builtin.include_role:
        name: syncthing
    - name: Create random files
      ansible.builtin.shell:
        cmd: 'echo "TEST" > {{ item.path }}/TEST.txt

          dd if=/dev/urandom of={{ item.path }}/testfile1 bs=1M count=1

          dd if=/dev/urandom of={{ item.path }}/testfile2 bs=1M count=1

          dd if=/dev/urandom of={{ item.path }}/testfile3 bs=1M count=1

          dd if=/dev/urandom of={{ item.path }}/testfile4 bs=1M count=1

          '
      changed_when: true
      loop: '{{ syncthing_folders }}'
      loop_control:
        label: '{{ item.label }}'
      when: inventory_hostname == groups['syncthing_clients'][0]
      tags: molecule-idempotence-notest
</pre></code>
