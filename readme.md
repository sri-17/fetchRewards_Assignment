# FetchRewards Assignment

## Technology Used 

  - Amazon Web Services
  - Python 
  - Boto3

## How to 
  1. Preparation/Setup 
     - Make sure you are logged into AWS in the terminal
     - Use a Linux or MacOs system 
     - Else use [Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) instruction
  2. Make sure you have ```pip``` installed
  3. Need to install pyyaml using below command:
      ```pip install pyyaml```
  4. Need to install boto3 using below command:   
      ```pip install boto3```
  5. After the above are installed, run below command:
      ```python setup.py```
  6. Wait for atleast a minute for the instance to be created
  7. Both public and private keys will be generated and placed in same folder as setup.py file is saved
  8. Run below command to get the public IP address for the created instance:
        ```python public_ip.py```
  9. Take the public key and IP address and use in the below command to ssh to both the users:
        ```ssh -i user1_rsa user1@1.xx.xx.xx```
        ```ssh -i user2_rsa user2@1.xx.xx.xx```
