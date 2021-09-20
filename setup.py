# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import os
import io
from setuptools import setup


def read(fname):
    return io.open(
        os.path.join(os.path.dirname(__file__), fname),
        'r', encoding='utf-8').read()

setup(name='tryton-filestore-s3',
    version='0.1.3',
    author='gcoop',
    author_email='info@gcoop.coop',
    url='https://github.com/gcoop-libre/tryton-filestore-s3',
    description='Store Tryton files on S3 AWS Storage.',
    long_description=read('README'),
    py_modules=['tryton_filestore_s3'],
    zip_safe=False,
    platforms='Posix; MacOS X; Windows',
    keywords='tryton s3 aws storage attachments',
    classifiers=[
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet'
        ],
    license='GPL-3',
    install_requires=[
        'boto3',
        'trytond > 4.2',
        ],
    )
