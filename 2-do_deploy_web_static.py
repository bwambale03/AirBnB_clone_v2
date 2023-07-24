#!/usr/bin/env python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import env, put, run, cd
import os

env.hosts = ["54.237.80.101", "100.26.121.175"]
env.user = "ubuntu"

def do_pack():
    """
    Return the archive path if the archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distribute the archive.
    """
    if os.path.exists(archive_path):
        archived_file = os.path.basename(archive_path)
        newest_version = "/data/web_static/releases/" + archived_file[:-4]

        with cd("/tmp/"):
            put(archive_path, archived_file)

        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version, newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
