1	Preparation/Setup
    Login to Linux or MacOS system 
    Use Windows instruction for Windows system

2	Make sure pip is installed

3	Need to install pyyaml and boto3 using below commands:
    pip install pyyaml
    pip install boto3

4	After the above are installed, run below command:
    python setup.py

5	Wait 1 to 2 minute for the instance to be created

6	Then, run below command to get the IP address:
    python public_ip.py 

7	Please Email me for the private key and make a file and store as ~/.ssh/ec2-instance.pem

8	Then run below command to connect to new instance (take the IP address which you got from above):
    ssh -i wholepath/ec2-instance.pem ec2-user@IP address
