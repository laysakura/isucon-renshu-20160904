from fabric.api import env, run, sudo, cd
from fabric.contrib.files import exists
from fabric.decorators import task, runs_once
from fabric.colors import blue
from fabric.context_managers import settings
from functools import wraps

env.user = "isucon"
env.hosts = ["13.78.93.115"]

@task
def pull():
    with cd("webapp"):
        run("git pull origin master")
        with cd("ruby"):
            run("bundle install")

@task
def status():
    sudo("systemctl status --no-pager isuxi.ruby")

@task
def restart_ruby():
    sudo("systemctl restart isuxi.ruby")

@task
def restart_nginx():
    sudo("systemctl restart nginx")

@task
def deploy():
    pull()
    restart_ruby()
    restart_nginx()

@task
def hello():
    run("echo hello")
