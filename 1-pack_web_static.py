#!/usr/bin/python3
"""
    A fabric script to compress the web_sttic data
"""

from fabric.operations import local
from datetime import datetime
import os


def do_pack():
    """
        compresses the web_sttic files for deployment
    """
    # current data and time in string format
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # dir to compress
    source_dir = "web_static"
    
    # archive to store the tgz file
    archive_dir = "versions"

    # create archive dir if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # archive file name
    archive_name = f"web_static_{timestamp}.tgz"

    # path to store the archive file
    archive_path = os.path.join(archive_dir, archive_name)

    # create the .tgz file
    local(f"tar -czvf {archive_path} {source_dir}")

    # check if the archive path created successfully
    if os.path.exists(archive_path):
        print(f"Archive created: {archive_path}")
        return archive_path
    else:
        print("Failed to create the archive.")
        return None