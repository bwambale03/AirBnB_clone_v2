#!/usr/bin/python3
"""This generates a .tgz archive from the contents of the web_static folder.
"""
from fabric import task
import time

@task
def do_pack(c):
    """this script generates a tg archive from web_static folder"""
    print("Packing web_static to .tgz archive")
    try:
        c.run("mkdir -p versions")
        timestamp = time.strftime("%Y%m%d%H%M%S")
        c.run("tar -cvzf versions/web_static_{}.tgz web_static".format(
            time.strftime("%Y%m%d%H%M%S")))
        
        return f"versions/web_static_{timestamp}.tgz"
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
