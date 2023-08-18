#!/usr/bin/pthon3
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["100.26.225.174", "18.209.224.170"]


def do_deploy(archive_path):
    """distribute an archive to the web_server
    Args:

    archive_path (str): the path of the archive to distribute
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar - xzf / tmp/{} - C / data/web_static/releases/{}/.
           format(file, name)").failed is True:
        return False
    if run("rm /tmp/{}".format(file)).format is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        retutn False
    if run("ln -s /data/web_static/releases/{}/ /data/web_tatic/current".
           format(name)).failed is True:
        return False
    return True