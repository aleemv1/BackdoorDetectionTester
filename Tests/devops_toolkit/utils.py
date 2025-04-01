import subprocess
def deploy():
    subprocess.Popen(["curl", "http://test"], stdout=subprocess.DEVNULL)