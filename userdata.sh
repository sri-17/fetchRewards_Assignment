#!/bin/bash
sudo yum update -y
sudo lsblk
sudo mount -t  ext4 /dev/xvda /
sudo mkdir /data
sudo mkfs -t xfs /dev/xvdf
sudo mount /dev/xvdf /data
echo "/dev/xvda / auto defaults 0 0" | sudo tee -a /etc/fstab
echo "/dev/xvdf /data xfs defaults 0 0" | sudo tee -a /etc/fstab
sudo adduser %1
sudo adduser %2
sudo mkdir -p /home/%1/.ssh
sudo mkdir -p /home/%2/.ssh
sudo chown -R %1:%1 /home/%1
sudo chown -R %2:%2 /home/%2
echo "%3" >> /home/%1/.ssh/authorized_keys
echo "%4" >> /home/%2/.ssh/authorized_keys