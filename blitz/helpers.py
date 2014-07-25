from fabric.api import *
import os
import blitz.configfile as cf


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
        local('echo ******FINISH*****')

    # Config files format so far:
    #   app_name: testapp
    #   github_repo_url: https://github.com/testperson/testapp.git
    #   EOL
    def read_in_config_and_set(self):
        if cf.get_appname() is not None:
            self.app_name = cf.get_appname()
            self.deploy_path = '/var/www/%s' % self.app_name
            self.working_path = '%s/current' % self.deploy_path
            self.repo_path = '%s/repo' % self.deploy_path
            self.releases_path = '%s/releases' % self.deploy_path
            self.shared_path = '%s/shared' % self.deploy_path
            if cf.get_github_repo_url() is not None:
                self.github_repo_url = cf.get_github_repo_url()
            else:
                print("NEED TO ADD GIT_HUB_REPO_URL")
        else:
            print("NEED TO ADD APP_NAME")

    def pull_to_repo(self):
        #assumes there is a new commit ready on github
        if self.is_repo_empty():
            sudo('cd %s && git init && git clone %s' % (self.repo_path, self.github_repo_url))
        else:
            sudo('cd %s && git pull %s' % (self.repo_path, self.github_repo_url))
        if self.need_to_prune_releases():
            sudo("cd %s && rm -rf `ls -t | awk 'NR>4'`" % self.releases_path)
        sudo('cd %s && '
             'COMMITHASH=$(git rev-parse HEAD) && '
             'cd %s && mkdir -p ${COMMITHASH} && '
             'cp -rf %s/* ${COMMITHASH} && '
             'rm -rf %s/* && '
             'ln -s %s/${COMMITHASH} %s'
             % (self.repo_path, self.releases_path, self.repo_path,
                self.working_path, self.releases_path, self.working_path))

    def push_local_commit(self):
        pass

    def is_repo_empty(self):
        answer = run('[ "$(ls -A %s)" ] && echo "Not Empty" || echo "Empty"' % self.repo_path)
        if "Not" not in answer:
            return True
        else:
            return False

    def need_to_prune_releases(self):
        answer = run('cd %s && ls -l | grep -v ^l | wc -l' % self.releases_path)
        num_dirs = int(answer)  # This will be +1 off actual num_dirs when at least one dir exists
        print(num_dirs)
        if num_dirs > 5:
            return True
        else:
            return False
