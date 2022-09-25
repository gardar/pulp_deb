# WARNING: DO NOT EDIT!
#
# This file was generated by plugin_template, and is managed by it. Please use
# './plugin-template --github pulp_deb' to update this file.
#
# For more info visit https://github.com/pulp/plugin_template

import os
import sys
import requests

branches = sys.argv[1:]

headers = {
    "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
    "Accept": "application/vnd.github.v3+json",
}

github_api = "https://api.github.com"
workflow_path = "/actions/workflows/update_ci.yml/dispatches"
url = f"{github_api}/repos/pulp/pulp_deb{workflow_path}"

for branch in branches:
    print(f"Updating {branch}")
    requests.post(url, headers=headers, json={"ref": branch})
