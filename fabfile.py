from fabric.api import *
from blitz.helpers import Helpers

env.hosts = ["127.0.0.1:2222"]
env.user = "vagrant"
#env.password=""
#env.parallel=True

helpers = Helpers()

def test():
    helpers.test()

def setup():
    helpers.setup()

def push():
    helpers.push_local_commit()
    helpers.pull_to_repo()



