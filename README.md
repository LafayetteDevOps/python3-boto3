# python3-boto3

Repository created to hold python3 boto3 scripts

AWS cli must be installed and configured in order to establish authentication.  'aws configure' must be run to set credentials
in order to interact with the AWS API.

All scripts should be run in the CLI.

The script, ec2_list.py, does not take any command line arguments whereas all the other scripts ec2_reboot.py, ec2_start.py, ec2_stop.py, and ec2_terminate.py do.  The command line argument wil be the \<instance id\> of the ec2 instance.  Eachof the for scripts take at least one argument and do support multiple.

Exempli Gratia

    $ ./ec2_list.py
    $ ./ec2_start.py <instance id>
    $ ./ec2_start.py <instance id> <instance id>
