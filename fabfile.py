'''
Fab file for deployment.
'''

from deploy import standalone

# deploy.remote configuration.
env.user='rfilguei'
env.results_dir="/home/"+env.user+"/output"
env.model="bluclobber"
env.corpus='/rdZone/live/rd003v/CompressedALTO-fromJamesH/CompressedALTO'
env.deploy_to="/home/"+env.user+"/BluclobberSpark"

# deploy.standalone configuration.
env.standalone_deploy_dir = 'standalone'
