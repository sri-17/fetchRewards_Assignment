# FetchRewards Assignment

## Technology Used 

  - Amazon Web Services
  - Python 
  - Boto3

## How to 
  1. Please change the parameter values in yaml file depending on the requirement, such as: Email, keyname, Value, login
  2. Preparation/Setup 
     - Make Sure provide programmatic access to the user
     - To generate the User Access Key and Secret key, please follow this [guide](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html). Then save the Access and Secret key.
     - Use a Linux or MacOs system 
     - Else use [Windows](https://gitforwindows.org) instruction
  3. Make sure you have ```pip``` installed
  4. Need to install pyyaml using below command:
      ```pip install pyyaml```
  5. Need to install boto3 using below command:   
      ```pip install boto3```
  6. Need to install AWS CLI depending on the [OS](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)
  7. Then, run the command: 
       ```aws configure``` .
	You will be promted to give Access key, then Paste the saved Access Key. Click enter and again you will be promted to give Secret key, then Paste the saved Secret key, and again click enter and give default region when promted(eg: us-east-1).
  8. After the above are installed, run below command:
      ```python setup.py```
  9. Wait for atleast a minute for the instance to be created
  10. Both public and private keys will be generated and placed in same folder as setup.py file is saved
  11. Run below command to get the public IP address for the created instance:
        ```python public_ip.py```
  12. By running the above command, cloud watch alerts have been configured using cloud watch metrics and publish to an email(specified in yaml) using AWS SNS.
  13. Take the public key and IP address and use in the below command to ssh to both the users:
        ```ssh -i user1_rsa user1@1.xx.xx.xx```
        ```ssh -i user2_rsa user2@1.xx.xx.xx```
