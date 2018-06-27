'''
Set up to run locally. This is designed to be used for testing.
'''

import os
import pandas as pd
from fabric.api import task, env, execute, lcd, local


@task
def setup(query):
    '''
    Prepare instance for running. Generates necessary files.
    '''
    execute(install, query=query)


@task
def install(query):
    '''
    Generate necessary files.
    '''
    local('rm -rf ' + env.standalone_deploy_dir)
    local('mkdir -p ' + env.standalone_deploy_dir)
    with lcd(env.standalone_deploy_dir):  # pylint: disable=not-context-manager
        local('cp -r ../bluclobber/ .')
        local('cp ../' + query + ' ./bluclobber/harness/query_sub.py')
        local('cp ../deploy/urika.sh ./harness/.')
        local('find . -iname "*.pyc" -delete')
        local('find . -iname "__pycache__" -delete')


@task
def test():
    '''
    Run the query.
    '''
    with lcd(env.standalone_deploy_dir+'./bluclobber/harness'):  # pylint: disable=not-context-manager
        local('./urika.sh query_sub.py')


@task
def pytest():
    '''
    Run pytest tests.
    '''
    with lcd(env.standalone_deploy_dir):  # pylint: disable=not-context-manager
        local('py.test')
