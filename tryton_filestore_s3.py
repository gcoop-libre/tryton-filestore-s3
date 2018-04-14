# This file is part of filestore-s3. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import boto3
import uuid

from trytond.config import config
from trytond.filestore import FileStore
from trytond.pool import Pool


class FileStoreS3(FileStore):

    def get(self, id, prefix=''):
        s3, bucket = get_client()
        key = name(id, prefix)
        response = s3.get_object(Bucket=bucket, Key=key)
        return response['Body'].read()

    def getmany(self, ids, prefix=''):
        return [self.get(id, prefix) for id in ids]

    def size(self, id, prefix=''):
        s3, bucket = get_client()
        key = name(id, prefix)
        response = s3.head_object(Bucket=bucket, Key=key)
        return response['ContentLength']

    def sizemany(self, ids, prefix=''):
        return [self.size(id, prefix) for id in ids]

    def set(self, data, prefix=''):
        s3, bucket = get_client()
        id = uuid.uuid4().hex
        key = name(id, prefix)
        s3.put_object(Bucket=bucket, Key=key, Body=data)
        return id

    def setmany(self, data, prefix=''):
        return [self.set(d, prefix) for d in data]

def name(id, prefix=''):
    return '/'.join(filter(None, [prefix, id]))

def get_client():
    access_key = config.get('database', 'access_key', default='')
    secret_key = config.get('database', 'secret_key', default='')
    bucket = config.get('database', 'bucket')
    client = boto3.client('s3',
        aws_access_key_id     = access_key,
        aws_secret_access_key = secret_key,
        )
    return client, bucket
