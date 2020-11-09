def aws():
    import os
    os.system("clear")
    os.system("tput setaf 1")
    os.system("tput bold")
    os.system("tput smul")
    print("\t\t\t\tCONTROL AWS AT YOUR FINGER TIPS")
    os.system("tput rmul")
    os.system("sleep 1")
    os.system("tput setaf 7")
    print("please enter your AWS credentials below")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    os.system("sleep 1")
    os.system("tput rmul")
    os.system("aws configure")
    print("select the service of aws on which you would like to perform operations")
    os.system("sleep 1")
    print("""
            1.EC2(elastic compute cloud)
            2.S3(simple storage service)
            """)
    service=int(input("enter your choice: "))
    if service==1:
        while True:
            os.system("clear")
            print("select the sub-service of EC2")
            print("""
            1.create key-pair
            2.create security group
            3.add ingress rules to security group
            4.create EBS volume
            5.attach volume to instance
            6.launch instance
            7.exit
                """)
            ec2=int(input("enter your choice: "))
            if ec2==1:
                key_name=input("enter the name you want to give to your key: ")
                os.system("aws ec2 create-key-pair --key-name {0} > {0}.pem".format(key_name))
                print("the key is saved as {}.pem".format(key_name))
            elif ec2==2:
                sg_name=input("enter the name you want to give to your security group: ")
                os.system(""" aws ec2 create-security-group --group-name {} --description "security group" """.format(sg_name))
            elif ec2==3:
                print("Rules created can be accessed from all the IP's")
                sg_port=int(input("enter ingress port number: "))
                sg_protocol=input("enter protocol: ")
                sg_groupid=input("enter group-id: ")
                os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr 0.0.0.0/0".format(sg_groupid,sg_protocol,sg_port))
            elif ec2==4:
                ebs_region=input("enter the region to create EBS: ")
                ebs_size=int(input("enter the size for EBS volume in GB: "))
                os.system("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {}".format(ebs_size,ebs_region))
            elif ec2==5:
                vol_id=input("enter volume id: ")
                inst_id=input("enter instance id: ")
                dev=input("enter device name: ")
                os.system ("aws ec2  attach-volume   --volume-id {}  --instance-id {} --device {}".format(vol_id,inst_id,dev))
            elif ec2==6:
                inst_sg_id=input("enter security group id: ")
                inst_type=input("enter instance type: ")
                inst_ami_id=input("enter AMI id: ")
                inst_key=input("enter key name: ")
                os.system("aws ec2 run-instances   --security-group-ids {}  --instance-type {}  --image-id {}   --key-name {} ".format(inst_sg_id,inst_type,inst_ami_id,inst_key))
            elif ec2==7:
                exit()
            else:
                print("option not supported")
            input("enter any key to continue....")
    if service==2:
        while True:
            os.system("clear")
            print("select sub-service of S3")
            print("""
                    1.create a bucket
                    2.add object to bucket
                    3.exit
                    """)
            s3=int(input("enter your choice: "))
            if s3==1:
                s3_name=input("enter the name you want to give to the S3 bucket: ")
                s3_region=input("enter the region to create S3 bucket: ")
                os.system("aws s3api create-bucket --bucket {0} --region {1} --acl public-read --create-bucket-configuration LocationConstraint={1}".format(s3_name,s3_region))
            elif s3==2:
                s3_local_path=input("enter your local path for file: ")
                s3_bucket_name=input("enter the name of bucket to upload: ")
                os.system("""aws s3 cp {} s3://{} --acl public-read""".format(s3_local_path,s3_bucket_name))
            elif s3==3:
                exit()
            else:
                print("option not supported")
            input("enter any key to continue....")


aws()
