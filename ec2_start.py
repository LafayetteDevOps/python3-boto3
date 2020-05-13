#! /usr/bin/python3

import boto3
ec2 = boto3.resource('ec2')

for id in sys.argv[1:]:
    instance = ec2.instance(id)
    print(instance.start())
