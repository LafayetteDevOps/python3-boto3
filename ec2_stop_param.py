#! /usr/bin/python3

import boto3
ec2 = boto3.resource('ec2')

instances = ['i-02b597fa65beb3880','i-0391f89d9c136b9bd']

for id in instances:
    instance = ec2.Instance(id)
    print(instance.stop())
