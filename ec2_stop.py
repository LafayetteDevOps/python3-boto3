#! /usr/bin/python3

'''
import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-00fd4273680ebb2d6').stop()
'''

import boto3, sys
ec2 = boto3.resource('ec2')

# iterate through instance IDs and terminate them
for id in sys.argv[1:]:
 instance = ec2.Instance(id)
 print(instance.terminate())
