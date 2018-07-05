'''
Fab file for deployment.
'''

from fabric.api import env
from deploy import standalone
from deploy import urika

# deploy.standalone configuration.
env.standalone_deploy_dir = 'standalone'
env.production_deploy_dir = 'production'
