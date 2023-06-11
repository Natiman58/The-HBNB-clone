#!/usr/bin/python
"""
    A fabric script that deletes out of date archives
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # Replace with your remote user
env.key_filename = '/path/to/your/private/key'  # Replace with the path to your private key

def do_clean(number=0):
    """
        cleans unecessary archives from the web servers
    """
    number = int(number)
    if number < 0:
        return

    # execute the following command into "versions folder"
    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs rm -rf'.format(number + 1))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number + 1))

def do_pack():
    """
        Packs the archive for deployment
    """
    now = datetime.now()
    archive_filename = 'web_static_' + now.strftime('%Y%m%d%H%M%S') + '.tgz'
    local('mkdir -p versions')
    local('tar -czvf versions/{} web_static'.format(archive_filename))
    return 'versions/{}'.format(archive_filename)

def do_deploy(archive_path):
    """
        deplo< the archive
    """
    if not os.path.exists(archive_path):
        return False

    archive_filename = os.path.basename(archive_path)
    release_dir = '/data/web_static/releases/' + archive_filename[:-4]

    try:
        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Create the release directory
        run('mkdir -p {}'.format(release_dir))

        # Extract the contents of the archive to the release directory
        run('tar -xzf /tmp/{} -C {} --strip-components=1'.format(archive_filename, release_dir))

        # Remove the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete the existing symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_dir))

        print("New version deployed!")
        return True
    except:
        return False

def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
