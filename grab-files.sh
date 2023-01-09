mkdir /tmp/install-deps
cd /tmp/install-deps

yum install yum-plugin-downloadonly yum-utils zip -y
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
echo "Variable is"
echo $FILES
yum install --downloadonly --downloaddir=/tmp/install-deps $FILES 
zip install-deps *