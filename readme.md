# FetchRewards Assignment

## Technology Used 

  - Amazon Web Services
  - Python 
  - Boto3

## How to 
  1. Please change the parameter values in yaml file depending on the requirement, such as: Email, keyname, Value, login
  1. Preparation/Setup 
     - Make Sure provide programmatic access to the user and save User Access Key and Secret key
     - Use a Linux or MacOs system 
     - Else use [Windows](https://gitforwindows.org) instruction
  2. Make sure you have ```pip``` installed
  3. Need to install pyyaml using below command:
      ```pip install pyyaml```
  4. Need to install boto3 using below command:   
      ```pip install boto3```
  5. Need to install AWS CLI depending on the [OS](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)
  6. Then, run below command: 
	    ```aws configure```
	        Paste the saved Access Key 
	        Paste the saved Secret key
	        use default region
  7. After the above are installed, run below command:
      ```python setup.py```
  8. Wait for atleast a minute for the instance to be created
  9. Both public and private keys will be generated and placed in same folder as setup.py file is saved
  10. Run below command to get the public IP address for the created instance:
        ```python public_ip.py```
  11. By running the above command, cloud watch alerts have been configured using cloud watch metrics and publish to an email(specified in yaml) using AWS SNS.
  12. Take the public key and IP address and use in the below command to ssh to both the users:
        ```ssh -i user1_rsa user1@1.xx.xx.xx```
        ```ssh -i user2_rsa user2@1.xx.xx.xx```
