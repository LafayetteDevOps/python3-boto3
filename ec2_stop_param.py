#! /usr/bin/python3

import boto3
ec2 = boto3.resource('ec2')

instances = ['i-0d3ca60ac96e8a896']

for id in instances:
    instance = ec2.Instance(id)
    print(instance.stop())
