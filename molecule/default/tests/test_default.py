import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

@pytest.fixture
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    debian_files = "file=../../vars/Debian.yml name=role_debian"
    redhat_files = "file=../../vars/RedHat.yml name=role_redhat"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        debian_files)["ansible_facts"]["role_debian"])

    ansible_vars.update(host.ansible(
        "include_vars",
        redhat_files)["ansible_facts"]["role_redhat"])

    return ansible_vars


def test_pkg_install(host, get_vars):
    os = host.system_info.distribution
    version = str(get_vars['version'])

    if os == 'ubuntu':
        for pkg in get_vars['debian_package']:
            if (pkg.find("{{ version }}") != -1):
                pkg =pkg.replace("{{ version }}",version)
            
            debian_package = host.package(pkg)
            assert debian_package.is_installed

    if os == 'Centos':
        for pkg in get_vars['redhat_package']:
            if (pkg.find("{{ version | replace('.', '') }}") != -1):
                version =version.replace('.','')
                pkg =pkg.replace("{{ version | replace('.', '') }}",version)

            redhat_package = host.package(pkg)
            assert redhat_package.is_installed


def test_postgresql_service(host, get_vars):
    os = host.system_info.distribution
    version = str(get_vars['version'])
    if os == 'ubuntu':        
        debian_service = host.service('postgresql')

        assert debian_service.is_running

    elif os == 'CentOS':
        redhat_service = host.service("".join(['postgresql-', version]))

        assert redhat_service.is_running


def test_user(host, get_vars):
    c1 = "sudo -u postgres psql -t -c '\\du' | cut -d '|' -f 1"
    for users in get_vars['user_list']:
        user_status = host.run(c1+"| grep -w "+ users['user'])
        assert user_status.succeeded


def test_database(host, get_vars):
    c1 = "sudo -u postgres psql -t -c'\\l' | cut -d '|' -f 1"
    for db in get_vars['database_list']:
        db_status = host.run(c1+"| grep -w "+ db['db'])

    assert db_status.succeeded
