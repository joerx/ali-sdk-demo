# Aliyun SDK Demo

Quick python demo for Aliyun SDKs

## Preconditions

- Aliyun account
- Valid credentials for API access

## OSS Example

- Prepare venv and install requirements

```sh
virtualenv venv -p $(which python3)
. venv/bin/activate
pip install -r requirements.txt
```

- Setup environment

```sh
export ALIYUN_ACCESS_KEY_ID=...
export ALIYUN_ACCESS_KEY_SECRET=...
export OSS_ENDPOINT=http://oss-ap-southeast-3.aliyuncs.com # optional
export OSS_BUCKET='my-demo-bucket'
```

- Run example

```sh
python oss.py
```
