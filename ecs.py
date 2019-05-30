# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
import os

access_key_id = os.getenv('ALIYUN_ACCESS_KEY_ID')
access_key_secret = os.getenv('ALIYUN_ACCESS_KEY_SECRET')

# Create an AcsClient instance
client = AcsClient(
   access_key_id, 
   access_key_secret,
   "ap-southeast-3"
)

# Create a request and set parameters
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)

# Initiate an API request and display the response value
response = client.do_action_with_exception(request)

print(response)
