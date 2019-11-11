import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

debian_pkg = []
debian_pkg.append('python-psycopg2')
debian_pkg.append('libpq-dev')
debian_pkg.append('pgadmin4')
debian_pkg.append('postgresql-client-9.5')
debian_pkg.append('postgresql-9.5')
debian_pkg.append('postgresql-contrib-9.5')
debian_pkg.append('postgresql-server-dev-9.5')


def test_debian_pkg(host):
    os = host.system_info.distribution

    if os == 'debian':
        debian_package = host.package(debian_pkg)

        assert debian_package.is_installed


redhat_pkg = []
redhat_pkg.append('postgresql-contrib')
redhat_pkg.append('postgresql-devel')
redhat_pkg.append('python-psycopg2')
redhat_pkg.append('postgresql95')
redhat_pkg.append('postgresql95-server')


def test_redhat_pkg(host):
    os = host.system_info.distribution

    if os == 'redhat':
        redhat_package = host.package(redhat_pkg)

        assert redhat_package.is_installed


def test_postgresql_service(host):
    os = host.system_info.distribution

    if os == 'debian':
        debian_service = host.service('postgresql')

        assert debian_service.is_running

    elif os == 'redhat':
        redhat_service = host.service('postgresql9.5')

        assert redhat_service.is_running


@pytest.mark.parametrize('user', ['demo1', 'demo2'])
def test_user(host, user):
    c1 = "sudo -u postgres psql -t -c"
    user_status = host.run(c1+"'\\du' | cut -d \\| -f 1 | grep -w "+user)

    assert user_status.succeeded


@pytest.mark.parametrize('db', ['test1', 'test2'])
def test_database(host, db):
    c1 = "sudo -u postgres psql -t -c"
    db_status = host.run(c1+"'\\l' | cut -d \\| -f 1 | grep -w "+db)

    assert db_status.succeeded
