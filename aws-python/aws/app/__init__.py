
import boto
import sys
import time
import simplejson

KEY='AKIAIEVEG5NROOLV2Z5A'
SECRET='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'

sqs = boto.connect_sqs()
ec2 = boto.connect_ec2()

bootstrap = """#!/bin/bash

python -c "import boto

KEY = '%(KEY)s'
SECRET = '%(SECRET)s'

conn = boto.connect_sqs(KEY, SECRET)
queue = conn.create_queue('test_q')
conn.send_message(queue, 'this message is written in the aws cloud.')
"
/sbin/shutdown now -h
"""

AMI = 'ami-bb709dd2'
if __name__ == "__main__":

    startup = bootstrap % { 'KEY': KEY, 'SECRET': SECRET }
    # res = ec2.run_instances(image_id='ami-8e83cedc', user_data=startup)

    # # ,
    # #         instance_type='t1.micro', security_groups=['quick-start-1'], key_name='default0'
    # # for r in ec2.get_all_instances():
    # #     if r.id == res.id:
    # #         break
    # # print r.instances[0].public_dns_name

    # q = sqs.create_queue("test_q")
    # print("Waiting for messages")
    # while True:
    #     msg = q.get_messages()
    #     if msg:
    #         print msg[0].get_body()
    #         print("Message is deleted", sqs.delete_message(q, msg[0]))
    # def launch_ec2_instance():
    # get image corresponding to this AMI

    #image = ec2.get_image(AMI)

    print 'Launching EC2 instance ...'
    # launch an instance using this image, key and security groups
    # by default this will be an m1.small instance
    res = ec2.run_instances('ami-bb709dd2', key_name='ec2-sample-key',
                    security_groups=['default'], user_data=startup, max_count=5, min_count=3)
    print res.instances[0].update()
    instance = None
    while True:
        print '.',
        sys.stdout.flush()
        dns = res.instances[0].dns_name
        if dns:
            instance = res.instances[0]
            break
        time.sleep(5.0)
        res.instances[0].update()
    print 'Instance started. Public DNS: ', instance.dns_name
    print 'waiting for the messages...'
    q = sqs.create_queue('test_q')
    while True:
        msg = q.get_messages()
        if msg:
            print msg.status
            print("Message is deleted", sqs.delete_message(q, msg[0]))






