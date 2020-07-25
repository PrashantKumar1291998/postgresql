Ansible Role: oms_postgreSQL
============================

This role can be used to install postgreSQL with version 9.5 and above. This role is customizable, it support basic functionalities like creating database and users. Users can modify the role as per there requirements.

Version History
---------------

|**Date**| **Version**| **Description**| **Changed By** |
|----------|---------|---------------|-----------------|
|**July '25** | v0.0.1 | Initial Draft | [Ishan Ji Gupta](ishan.gupta@opstree.com), [Abhishek Vishwakarma](abhishek.vishwakarma@opstree.com)|

Supported OS
------------
  * CentOS:7
  * CentOS:6
  * Ubuntu:bionic
  * Ubuntu:xenial

Requirements
------------

There is no such requirements for the role.

Role Variables
--------------
The role variables are defined in the [vars](https://gitlab.com/oosm/osm_pstgresql/tree/master/defaults). Here is the list of variables that is used in this role

|Variable | Description|
|---------|------------|
| postgresql_database| Set true when want to create database|
| version | Define version of postgresql|
| postgresql_users | Set true when want to create user|
| user_list_attr | List of users to create|
| database_list | List of database to create|
| user| User of the postgreSQL|
| group | Group of the postgreSQL |


Inventory
----------
An inventory should look like this:-
```ini
[postgres]                 
192.168.1.198    ansible_user=ubuntu   
192.168.3.201    ansible_user=opstree 
```
Example Playbook
----------------

Sample playbook will look something like this,

    - hosts: postgres
      roles:
         - postgresql

Testing
------------

To test using molecule, define package to install, user list and database list in test_default.py

Author Information
------------------

Ishan Ji Gupta (ishan.gupta@opstree.com)