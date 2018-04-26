from fabric.api import *
from mako.template import Template
import mako
import os
from datetime import datetime
from contextlib import nested

@task
def prepare(query):
    execute(dependencies)
    execute(install, query=query)
    #execute(storeids)

@task
def install(query):
    local('mkdir -p '+env.deploy_to)
    with lcd(env.deploy_to):
        local('cp -r ../'+env.model +' ./')
        local('cp -r ../setup.py ./')
        local('cp ../' + query + ' ' +env.model+'/query.py')
        local('cp -r ../README.md ./')
        local('find . -iname "*.pyc" -delete')
        local('find . -iname "__pycache__" -delete')
        local('python setup.py develop')
        local('py.test')
@task
def test():
    with lcd(env.deploy_to +'/'+ env.model):
	local ('ls -lht') 
        local('pyspark < query.py')


@task
def sub(query, subsample=1, processes=12, wall='2:0:0'):
    env.processes=processes
    env.subsample=subsample
    env.wall=wall
    now=datetime.now()
    stamp=now.strftime("%Y%m%d_%H%M")
    outpath=os.path.basename(query).replace('.py','')+'_'+stamp

    template_file_path=os.path.join(os.path.dirname(__file__),
                                    env.machine+'.sh.mko')

    env.run_at = env.results_dir + '/'+outpath

    with open(template_file_path) as template:
        script=Template(template.read()).render(**env)
        with open('query.sh','w') as script_file:
            script_file.write(script)

    local('mkdir -p '+env.run_at)
    with cd(env.run_at):
       put(query, 'query.py')
       put('query.sh','query.sh')
       local('cp ../oids.txt .')
       local('qsub query.sh')

@task
def storeids():
    local('mkdir -p '+env.results_dir)
    with cd(env.results_dir):
       with prefix('module load icommands'):
           local('iinit')
           local('iquest --no-page "%s" '+
           '"SELECT DATA_PATH where COLL_NAME like '+
           "'"+env.corpus+"%'"+
           " and DATA_NAME like '%-%.zip' "+
           " and DATA_RESC_HIER = 'wos;wosArchive'"+'" >oids.txt')

@task
def stat():
    local('qstat')

@task
def fetch():
    with lcd(os.path.join(os.path.dirname(os.path.dirname(__file__)),'results')):
      with cd(env.run_at):
        get('*')

@task
def dependencies():
    local('pip install lxml pyyaml pytest' +
          ' psutil requests')
