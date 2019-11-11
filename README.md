ANSIBLE Role for postgreSQL
===========================

This role can be used to install postgreSQL on LINUX Server including Ubuntu, centOS etc., This role is customizable, it support basic functionalities like creating database and users. Users can modify the role as per there requirements.

Requirements
------------

There is no such requirements for the role.

Role Variables
--------------

For now these are the varibales which we are using in our role, which are pretty much basic and are self defining, 
# use this option when want to create database (true/ false) 
postgresql_database: 
# define the version here (11, 10, 9.4, 9.5, 9.6)
version: 
# use this option when want to create user (true/ false)
postgresql_users: 
# when creating user, provide list of users here,
user_list:
# when creating database, provide list of databases here,
database_list:
# user & group of the postgreSQL
user: 
group: 

Dependencies
------------

There are no such dependencies, 

Example Playbook
----------------

Sample playbook will look something like this,

    - hosts: servers
      roles:
         - osm_postgresql

Testing
------------

To test using molecule, define package to install and user list and database list in test_default.py

Author Information
------------------

Ishan Ji Gupta (ishan.gupta@opstree.com)