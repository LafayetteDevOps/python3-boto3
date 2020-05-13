#! /usr/bin/python3

import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-00fd4273680ebb2d6').start()
