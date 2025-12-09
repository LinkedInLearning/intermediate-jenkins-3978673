#!/bin/bash
# vi: ft=bash

echo "# $(date) Installation is starting."

# Uncomment the following line if you are using this script
# as user data for an EC2 instance on AWS.
# Output from the installation will be written to /var/log/user-data.log
#exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1

echo "# $(date) Install jenkins key and package configuration..."
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | tee \
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian binary/ | tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null

# install java, nginx, and jenkins
echo "# $(date) Install Java 21, NGINX, and Jenkins..."
apt update
apt-get -y upgrade

apt-get -y install \
    openjdk-21-jdk \
    nginx \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    python3-pip \
    python3-venv

apt-get -y install jenkins

# configure nginx
echo "# $(date) Configure NGINX..."
unlink /etc/nginx/sites-enabled/default

tee /etc/nginx/conf.d/jenkins.conf <<EOF
upstream jenkins {
    server 127.0.0.1:8080;
}

server {
    listen 80 default_server;
    listen [::]:80  default_server;
    location / {
        proxy_pass http://jenkins;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

echo "# $(date) Reload NGINX to pick up the new configuration..."
systemctl reload nginx

# install docker
echo "# $(date) Install docker..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt update
apt-get -y install docker-ce docker-ce-cli containerd.io
docker run hello-world

systemctl enable docker.service
systemctl enable containerd.service

usermod -aG docker ubuntu
usermod -aG docker jenkins

echo "# $(date) Restart Jenkins..."
systemctl restart jenkins

echo "# $(date) Copy the initial admin password to the root user's home directory..."
cp /var/lib/jenkins/secrets/initialAdminPassword ~

clear
echo "Installation is complete."

echo "# Open the URL for this server in a browser and log in with the following credentials:"
echo
echo
echo "    Username: admin"
echo "    Password: $(cat /var/lib/jenkins/secrets/initialAdminPassword)"
echo
echo
