import yaml
import boto3


ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

with open("/root/Pythoncode/aws-config.yaml", 'r') as stream:
        try:
           data = yaml.safe_load(stream)
           #print(data)
           #print(data.get('server').get('instance_type'))
        except yaml.YAMLError as exc:
           print(exc)

Value = (data.get('server').get('Tags'))[0].get('Value')
#print(Value)
new_instanceid = ''

response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        #print(instance["InstanceId"])
	statecheck = instance.get(u'State').get(u'Name')
	if statecheck == 'running':
		#print('running state')
		instancename = instance.get(u'Tags')[0].get(u'Value')
		#print(instancename)
		if instancename == Value:		
			ipaddress = instance.get(u'PublicIpAddress')
        		print("Instance Name :",instancename)
			print("Public IP address : ",ipaddress)
			print("Instance ID :",instance["InstanceId"])
			new_instanceid = instance["InstanceId"]	
	
response = sns.create_topic(Name='post_alert')
topicarn = response['TopicArn']
response = sns.subscribe(TopicArn=topicarn, Protocol="email", Endpoint=data.get('server').get('Email'))
subscription_arn = response["SubscriptionArn"]
print(topicarn)

cloudwatch.put_metric_alarm(
    AlarmName='Instance_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=300,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm when server CPU exceeds 70%',
    AlarmActions=[
        topicarn
    ],
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': new_instanceid,
        }
    ]
)

cloudwatch.put_metric_alarm(
    AlarmName='Instance_MEMORY_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='MemoryUtilization',
    Namespace='AWS/EC2',
    Period=300,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm when server Memory exceeds 70%',
    AlarmActions=[
        topicarn
    ],
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': new_instanceid,
        }
    ]
)