mkdir /tmp/install-deps
cd /tmp/install-deps

yum install yum-plugin-downloadonly yum-utils zip -y
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install --downloadonly --downloaddir=/tmp/install-deps docker-ce docker-ce-cli containerd.io docker-compose-plugin
zip install-deps *