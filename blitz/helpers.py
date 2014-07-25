from fabric.api import *
import os
import subprocess


current_dir = os.path.abspath(os.path.dirname(__file__))


class Helpers():

    def __init__(self):
        self.app_name = None
        self.github_repo_url = None
        self.deploy_path = None
        self.working_path = None
        self.repo_path = None
        self.releases_path = None
        self.shared_path = None
        self.read_in_config_and_set()

    def setup(self):
        print("*****INSTALLING PACKAGES*****")
        sudo('apt-get -y install git')
        sudo('apt-get -y install git-flow')
        print("*****INITIALIZING DIRECTORIES*****")
        directories = (
            self.deploy_path,
            self.working_path,
            self.releases_path,
            self.repo_path,
            self.shared_path
        )
        for directory in directories:
            sudo('mkdir -p %s' % directory)
        sudo('cd %s && git init '% self.repo_path)
        local('echo ******FINISH*****')

    # Config files format so far:
    #   app_name: testapp
    #   github_repo_url: https://github.com/testperson/testapp.git
    #   EOL
    def read_in_config_and_set(self):
        f = open('%s/.blitzConfig' % current_dir)
        lines = f.readlines()
        if lines[0].startswith('app_name:'):
            app_name_line = lines[0]
            self.app_name = app_name_line[app_name_line.index('app_name:')+len('app_name:'):].strip()
            self.deploy_path = '/var/www/%s' % self.app_name
            self.working_path = '%s/current' % self.deploy_path
            self.repo_path = '%s/repo' % self.deploy_path
            self.releases_path = '%s/releases' % self.deploy_path
            self.shared_path = '%s/shared' % self.deploy_path
            if lines[1].startswith('github_repo_url:'):
                github_url_line = lines[1]
                self.github_repo_url = \
                    github_url_line[github_url_line.index('github_repo_url:')+len('github_repo_url:'):].strip()
            else:
                print("NEED TO ADD GIT_HUB_REPO_URL")
        else:
            print("NEED TO ADD APP_NAME")

    def pull_to_repo(self):
        #local('git push origin master')
        sudo('rm -rf %s/*' % self.repo_path)
        sudo('cd %s && git clone %s' % (self.repo_path, self.github_repo_url))
        sudo('rm -rf %s/* && cp -rf %s/* %s' % (self.working_path, self.repo_path, self.working_path))
        sudo('cd %s &&'
             ' COMMITHASH=$(git rev-parse HEAD) && '
             'cd %s && mkdir -p ${COMMITHASH} && '
             'cp -rf %s/* ${COMMITHASH} ' % (self.repo_path, self.releases_path, self.repo_path) )
        sudo('rm -rf %s/.git' % self.working_path)

    def push_local_commit(self):
        pass





