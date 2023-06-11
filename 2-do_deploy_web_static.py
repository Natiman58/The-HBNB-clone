#!/usr/bin/python3
"""
    A fabric script to distribute an archive to web servers
"""
import os
from fabric.api import *

env.hosts = ["IP web-01", "IP-web-02"]

def do_deploy(archive_path):
    """
        deploys an archive to web servers
    """
    # if the archive does't exsist; return False
    if not os.path.exists(archive_path):
        return False
    try:
        # upload the package to temp folder on the server
        put(archive_path, '/tmp')

        # Uncompress the archive to the /data/web_static/releases/archive_filename w/o extensions(.tgz)
        # on the server
        archive_filename = os.path.basename(archive_path)
        release_dir = "/data/web_static/releases" + archive_filename[:-4]  # remove extension
        run(f"mkdir -p {release_dir}")
        run(f"tar -xzf /tmp/{archive_filename} -C {release_dir} --strip-components=1")
        
        # delete the archive from the web server
        run(f"rm /tmp/{archive_filename}")

        # delete the symbolic link /data/web_static/current
        run("rm -f /data/web_static/current")

        # create a new symbolic link /data/web_static/current linked to the new version
        run(f"ln -s {release_dir} /data/web_static/current")

        print("New version deployed successfully")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
