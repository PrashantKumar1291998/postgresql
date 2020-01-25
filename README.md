#

Ansible Role: oms_postgreSQL
============================

This role can be used to install postgreSQL. This role is customizable, it support basic functionalities like creating database and users. Users can modify the role as per there requirements.

Version History
---------------

|**Date**| **Version**| **Description**| **Changed By** |
|----------|---------|---------------|-----------------|
|**June '15** | v.1.0 | Initial Draft | Sudipt Sharma |

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

```yaml
# vars file for postgresql
postgresql_database: true
version: 9.5
postgresql_users: true
user_list_attr: {attr: CREATEROLE, INHERIT, BYPASSRLS, CREATEDB}
user_list:
        - {user: demo1, password: password1, -user_list_attr}
        - {user: demo2, password: password2, attr: CREATEROLE, INHERIT}
database_list:
        - {db: test1}
        - {db: test2}
user: postgres
group: postgres
```
|Variable | Description|
|---------|------------|
| postgresql_database| Set true when want to create database|
| version | Define version of postgresql|
| postgresql_users | Set true when want to create user|
| user_list_attr | List of users to create|
| database_list | List of database to create|
| user| User of the postgreSQL|
| group | Group of the postgreSQL |


Example Playbook
----------------

Sample playbook will look something like this,

    - hosts: servers
      roles:
         - osm_postgresql

Testing
------------

To test using molecule, define package to install, user list and database list in test_default.py

Author Information
------------------

Ishan Ji Gupta (ishan.gupta@opstree.com)