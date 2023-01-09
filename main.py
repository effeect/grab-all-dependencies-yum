import subprocess
import time

def up_container(vmname,application):
    # https://docs.docker.com/engine/reference/commandline/exec/
    subprocess.run(["docker", "pull", vmname])
    subprocess.Popen(["docker", "run", "--rm", "-e", f"FILES={application}","--name", "temp_container", vmname, "tail" , "-f", "/dev/null"])
    # Need to create failure condition to run this at the start if there is an issue still 
    time.sleep(10)
    subprocess.run(["docker", "cp", "grab-files.sh", "temp_container:/grab-files.sh"])
    # Run a task to create a variable for the script
    subprocess.run(["docker", "exec", "temp_container", "/bin/sh" ,"-c", "./grab-files.sh"])
    subprocess.run(["docker" ,"cp" , "temp_container:/tmp/install-deps/install-deps.zip", "install-deps.zip"])

    subprocess.run(["docker","kill","temp_container"])

if __name__ == "__main__":
    up_container("centos:7.9.2009","docker-ce")
