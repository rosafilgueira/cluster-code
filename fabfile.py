'''
Fab file for deployment.
'''

from fabric.api import env
from deploy import standalone
from deploy import legion

# deploy.standalone configuration.
env.standalone_deploy_dir = 'standalone'
