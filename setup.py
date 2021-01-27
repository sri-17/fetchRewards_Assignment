import yaml
import boto3
import time
import os
import subprocess

ec2 = boto3.resource('ec2')
path = os.getcwd()
#print('cwd path  :',path)
yamlpath = os.path.join(os.getcwd(),"aws-config.yaml")
print('yaml path : ',yamlpath)

#Read aws parameter yaml file
with open(os.path.join(os.getcwd(),"aws-config.yaml"), 'r') as stream:
        try:
           data = yaml.safe_load(stream)
           #print(data)
           #print(data.get('server').get('instance_type'))
        except yaml.YAMLError as exc:
           print(exc)


#Creating private and public key for users
username1 = (data.get('server').get('users'))[0].get('login')
username2 = (data.get('server').get('users'))[1].get('login')
print('username1 :',username1)
print('username2 :',username2)

user1_rsa = username1+"_rsa.pub"
user2_rsa = username2+"_rsa.pub"

#call generate_userssh.sh
subprocess.call("sh generate_userssh.sh %s %s"%(username1,username2), shell=True)
user1_authorizedKEY = open(os.path.join(os.getcwd(),user1_rsa), 'r')
auth1 = user1_authorizedKEY.read()
#print('auth1---------->',auth1) 	
user2_authorizedKEY = open(os.path.join(os.getcwd(),user2_rsa), 'r')
auth2 = user2_authorizedKEY.read()
#print('auth2----------->',auth2)

#auth1 = (data.get('server').get('users'))[0].get('user1_ssh_key')
#auth2 = (data.get('server').get('users'))[1].get('user2_ssh_key')

#call userdata.sh 
userdatascript = open(os.path.join(os.getcwd(),"userdata.sh"), 'r')
userdatacode = userdatascript.read()
userdatacode = userdatacode.replace("%1",username1).replace("%2",username2).replace("%3",auth1).replace("%4",auth2)
#print('------')
#print('userdata :------------->',userdatacode)

#Print ImagId
instance_amitype = data.get('server').get('ami_type')
print('instance_amitype',instance_amitype)
instance_region = data.get('server').get('region')
print('instance_region',instance_region)
ec2_instance = boto3.client('ec2', region_name=instance_region)
response = ec2_instance.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        new_imageId = instance["ImageId"]
	#print(instance["ImageId"])
print('ImageId :',new_imageId)

key = (data.get('server').get('Tags'))[0].get('Key')
value = (data.get('server').get('Tags'))[0].get('Value')
tag_purpose_test = {"Key": key, "Value": value}

#instance creation
instance = ec2.create_instances(
        InstanceType = data.get('server').get('instance_type'),
        ImageId = new_imageId,
        MinCount = data.get('server').get('min_count'),
        MaxCount = data.get('server').get('max_count'),
        KeyName = data.get('server').get('keyname'),
	TagSpecifications=([{'ResourceType': 'instance','Tags': [tag_purpose_test]}]),
	BlockDeviceMappings=[
        {
            'DeviceName' : (data.get('server').get('volumes'))[0].get('device'),
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': (data.get('server').get('volumes'))[0].get('size_gb')
            }
        },
        {
            'DeviceName' : (data.get('server').get('volumes'))[1].get('device'),
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': (data.get('server').get('volumes'))[1].get('size_gb')
            }
        }
    ],
	UserData = userdatacode
)
