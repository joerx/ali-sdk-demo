import oss2
import datetime
import os

access_key_id = os.getenv('ALIYUN_ACCESS_KEY_ID')
access_key_secret = os.getenv('ALIYUN_ACCESS_KEY_SECRET')
oss_endpoint = os.getenv('OSS_ENDPOINT', 'http://oss-ap-southeast-3.aliyuncs.com')
oss_bucket = os.getenv('OSS_BUCKET', 'my-demo-bucket')

auth = oss2.Auth(
    access_key_id,
    access_key_secret
)

bucket = oss2.Bucket(auth, oss_endpoint, oss_bucket)

date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# The object key in the bucket is story.txt
key = 'test-{}.txt'.format(date)

# Upload
print("[Uploading]")
bucket.put_object(key, 'Mary had a little lamb')

print("{} - ok".format(key))

print()
print("[Files in bucket]")
# Traverse all objects in the bucket
for object_info in oss2.ObjectIterator(bucket):
    print(object_info.key)
