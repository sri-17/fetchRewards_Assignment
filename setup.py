import yaml
import boto3
import time

ec2 = boto3.resource('ec2')

with open("/root/Pythoncode/aws-config.yaml", 'r') as stream:
        try:
           data = yaml.safe_load(stream)
           #print(data)
           #print(data.get('server').get('instance_type'))
        except yaml.YAMLError as exc:
           print(exc)

user1_authorizedKEY = (data.get('server').get('users'))[0].get('user1_ssh_key')
#print(user1_authorizedKEY)
user2_authorizedKEY = (data.get('server').get('users'))[1].get('user2_ssh_key')
#print(user2_authorizedKEY)

#user data
myCode = """
#!/bin/bash
sudo yum update
sudo lsblk
sudo mount -t  ext4 /dev/xvda /
sudo mkdir /data
sudo mkfs -t xfs /dev/xvdf
sudo mount /dev/xvdf /data
echo "/dev/xvda / auto defaults 0 0" | sudo tee -a /etc/fstab
echo "/dev/xvdf /data xfs defaults 0 0" | sudo tee -a /etc/fstab
sudo adduser user1
sudo adduser user2
sudo mkdir -p /home/user1/.ssh
sudo mkdir -p /home/user2/.ssh
sudo chown -R user1:user1 /home/user1
sudo chown -R user2:user2 /home/user2
echo \"%s\" >> /home/user1/.ssh/authorized_keys
echo \"%s\" >> /home/user2/.ssh/authorized_keys
"""% (user1_authorizedKEY,user2_authorizedKEY)

key = (data.get('server').get('Tags'))[0].get('Key')
value = (data.get('server').get('Tags'))[0].get('Value')
tag_purpose_test = {"Key": key, "Value": value}

#instance creation
instance = ec2.create_instances(
        InstanceType = data.get('server').get('instance_type'),
        ImageId = data.get('server').get('ImageId'),
        MinCount = data.get('server').get('min_count'),
        MaxCount = data.get('server').get('max_count'),
        KeyName = 'ec2-instance',
	    TagSpecifications=([{'ResourceType': 'instance','Tags': [tag_purpose_test]}]),
	    BlockDeviceMappings=[
        {
            'DeviceName' : (data.get('server').get('volumes'))[0].get('device'),
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 10,
            }
        },
        {
            'DeviceName' : (data.get('server').get('volumes'))[1].get('device'),
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 100,
            }
        }
    ],
	UserData = myCode
)
