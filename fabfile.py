'''
Fab file for deployment.
'''

from fabric.api import env

from deploy import legion
from deploy import urika


env.production_deploy_dir = 'production'
