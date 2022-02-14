#Part 2:
1.
AMI = Ubtuntu LTS x86_64
DefaultName = i-0b0f35877c6d188fe
2. Select the instance, click actions  and connect VPC
3. Assuming you are going to use an elastic ip, you should not auto assign a public ipv4. The public address is going to be replaced by the elastic ip.
4. Select the "Volumes" subtab in "Elastic Block Store" subtab and choose the instance.
5. Go to the "Tags" property when looking at instance information, Key=Name
Value=Stewart-instance
6.Click actions on security group and associate with instance
7.Go to "Elastic IPs" under the "Network and Security" subtab. From there you can reserve an ip and assoicate it with the instance
9. sudo hostname stewart-ubuntu
