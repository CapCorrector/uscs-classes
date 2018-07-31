import boto3 
import json
import sys

region='us-west-1'
ec2c=boto3.client('ec2',region_name=region)

### VPC and Subnet

resp=ec2c.describe_vpcs()
vpcidtouse=resp['Vpcs'][0]['VpcId']
subnetlist=ec2c.describe_subnets(Filters=[ {'Name': 'vpc-id', 'Values': [vpcidtouse]} ])
#print(json.dumps(subnetlist,indent=2,separators=(',',':'))) ### Show json reply
subnetid=subnetlist['Subnets'][0]['SubnetId']

### Sec Group

secgrpname='sshtoall'
try:
	secgrpfilter = [
		{
			'Name':'group-name', 'Values':[secgrpname]
		}
	]
	secgroups = ec2c.describe_security_groups(
		Filters=secgrpfilter
	)
	secgrptouse = secgroups["SecurityGroups"][0]
	secgrpid = secgrptouse['GroupId']
except:
	print('no security group, will create security group' + secgrpname)
	secgrptouse = ec2c.create_security_group(
		GroupName=secgrpname,
		Description='Allow ssh from everywhere',
		VpcId=vpcidtouse)

	secgrpid = secgrptouse['GroupId']
	print("created security group:" + secgrpid)
	portlist = [22]
	for port in portlist:
		try:
			data = ec2c.authorize_security_group_ingress(
				GroupId=secgrpid,
				IpPermissions=[
					{'IpProtocol': 'tcp',
					'FromPort': port,
					'ToPort': port,
					'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
					{'IpProtocol': 'tcp',
					'FromPort': port,
					'ToPort': port,
					'Ipv6Ranges': [{'CidrIpv6': '::/0'}]}
				])
		except:
			print("error opening port:" + str(port))
			exit()

### Run

amiid='ami-4aa04129' ### Ubuntu Server 16.04 LTS (HVM), SSD Volume Type
insttype='t2.micro'
secgrpidlist=[secgrpid]
sshkeypair='Corrector'
numinstances = 1
resp = ec2c.run_instances(
	ImageId=amiid,
	InstanceType=insttype,
	KeyName=sshkeypair,
	SecurityGroupIds=secgrpidlist,
	SubnetId=subnetid,
	MaxCount=numinstances,
	MinCount=numinstances)

#print(json.dumps(resp,indent=2,separators=(',',':'))) ### Show json reply

inst=resp["Instances"][0]
instid=inst["InstanceId"]
print('Waiting for instance to enter running state')

bIsRunning = False
while bIsRunning == False:
	rz=ec2c.describe_instance_status(InstanceIds=[instid])
	#call can return before all data is available
	if not bool(rz):
		continue
	if len(rz["InstanceStatuses"]) == 0:
		continue

	#print(json.dumps(rz,indent=2,separators=(',',':'))) ### Show json reply

	inststate=rz["InstanceStatuses"][0]["InstanceState"]
	#print(json.dumps(inststate,indent=2,separators=(',',':'))) ### Show instance state part of json reply
	state=inststate["Name"]
	if state == 'running':
		bIsRunning = True

### Getting IP
bGotIp = False
while bGotIp == False:
	outp = ec2c.describe_instances(InstanceIds=[instid])
	inst=outp["Reservations"][0]["Instances"][0]
	instid=inst["InstanceId"] #### We already have it no? Overkill?
	publicip=inst.get('PublicIpAddress')
	if not publicip:
		print('do not have ip address yet')
		continue
	else:
		bGotIp = True

print('ip=' + publicip)

### Press any key
input("Press Enter to terminate instance...")

### Kill it
resp=ec2c.stop_instances(InstanceIds=[instid])
print(json.dumps(resp,indent=2,separators=(',',':'))) ### Show json reply

resp=ec2c.terminate_instances(InstanceIds=[instid])
print(json.dumps(resp,indent=2,separators=(',',':'))) ### Show json reply
