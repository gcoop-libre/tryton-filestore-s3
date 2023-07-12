# This file is part of filestore-s3. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import boto3
import uuid
from trytond.config import config
from trytond.filestore import FileStore


class FileStoreS3(FileStore):

    def get(self, id, prefix=''):
        s3, bucket = get_client()
        key = name(id, prefix)
        response = s3.get_object(Bucket=bucket, Key=key)
        return response['Body'].read()

    def size(self, id, prefix=''):
        s3, bucket = get_client()
        key = name(id, prefix)
        response = s3.head_object(Bucket=bucket, Key=key)
        return response['ContentLength']

    def set(self, data, prefix=''):
        s3, bucket = get_client()
        id = uuid.uuid4().hex
        key = name(id, prefix)
        s3.put_object(Bucket=bucket, Key=key, Body=data)
        return id


def name(id, prefix=''):
    return '/'.join(filter(None, [prefix, id]))


def get_client():
    access_key = config.get('database', 's3_access_key')
    if access_key is None:
        access_key = config.get('database', 'access_key')
    secret_key = config.get('database', 's3_secret_key')
    if secret_key is None:
        secret_key = config.get('database', 'secret_key')
    bucket = config.get('database', 'bucket')
    endpoint_url = config.get('database', 's3_endpoint')
    client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        endpoint_url=endpoint_url,
    )
    return client, bucket
