import json
import requests
from behave import when, then
import time
import os, stat
from utils import *
import glob
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from auth_vars import *

VERMILLION_URL = 'https://localhost'
SEARCH_ENDPOINT = '/search'
PUBLISH_ENDPOINT = '/publish'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# XXX Open-files tests need definition here


@when('The consumer publishes with a valid token')
def step_imp(context):
    payload = (

        ("id", res[0]),
        ('token', tokens["master"]),

        ("id", res[0]
         ),
        ('token', tokens["master"]),

    )
    files = {
        'file': ('sample.txt', open('sample.txt', 'rb')),
        'metadata': ('meta.json', open('meta.json', 'rb')),
    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer publishes with invalid resource id')
def step_imp(context):
    payload = (

        ("id", id_prefix + generate_random_chars()),
        ('token', tokens["master"]),

        ("id", id_prefix + generate_random_chars()
         ),
        ('token', tokens["master"]),

    )
    files = {
        'file': ('sample.txt', open('sample.txt', 'rb')),
        'metadata': ('meta.json', open('meta.json', 'rb')),
    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer publishes with empty resource id')
def step_imp(context):
    payload = (

        ("id", ""),
        ('token', tokens["master"]),

        ("id", ""
         ),
        ('token', tokens["master"]),

    )
    files = {
        'file': ('sample.txt', open('sample.txt', 'rb')),
        'metadata': ('meta.json', open('meta.json', 'rb')),
    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer publishes with invalid token')
def step_imp(context):
    payload = (

        ("id", res[0]),
        ('token', generate_random_chars()),

        ("id", res[0]
         ),
        ('token', generate_random_chars()),

    )
    files = {
        'file': ('sample.txt', open('sample.txt', 'rb')),
        'metadata': ('meta.json', open('meta.json', 'rb')),
    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer publishes with empty token')
def step_imp(context):
    payload = (

        ("id", res[0]),
        ('token', ''),

        ("id", res[0]
         ),
        ('token', ''),

    )
    files = {
        'file': ('sample.txt', open('sample.txt', 'rb')),
        'metadata': ('meta.json', open('meta.json', 'rb')),
    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer publishes by removing file form parameter')
def step_imp(context):
    payload = (

        ("id", res[0]),
        ('token', tokens["master"]),
    )

    files = {
        # 'file': ('sample.txt', open('sample.txt', 'rb')),

        'metadata': ('meta.json', open('meta.json', 'rb')),
    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer publishes by removing metadata form parameter')
def step_imp(context):
    payload = (

        ("id", res[0]),
        ('token', tokens["master"]),
    )

    files = {
        'file': ('sample.txt', open('sample.txt', 'rb')),
        # 'metadata': ('meta.json', open('meta.json', 'rb')),

    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


def get_umask():
    umask = os.umask(0)
    os.umask(umask)
    return umask

# Providing permissions to access the files
def chmod_plus_x(path):
    os.chmod(
        path,
        os.stat(path).st_mode | ((stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                                 & ~get_umask()))


@when('The consumer publishes by using extraneous form parameter')
def step_imp(context):
    payload = (

        ("id", res[0]),
        ('token', tokens["master"]),

        ("id", res[0]
         ),
        ('token', tokens["master"]),

    )
    files = {
        'abc': ('samplecsv.csv', open('samplecsv.csv', 'rb')),
        'efg': ('samplepdf.pdf', open('samplepdf.pdf', 'rb')),
    }
#This part of code removes the files present in the file-uploads folder that existed previously
    fil = glob.glob('../api-server/file-uploads/*')
    for f in fil:
        os.remove(f)

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer publishes with empty form parameter')
def step_imp(context):
    payload = (
        ("id", res[0]
         ),
        ('token', tokens["master"]),

    )
    files = {
        # 'file': ('sample.txt', open('sample.txt', 'rb')),
        # 'metadata': ('meta.json', open('meta.json', 'rb')),

    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer publishes with more than 2 form parameters')
def step_imp(context):
    payload = (
        ("id", res[0]),
        ('token', tokens["master"]),
    )

    files = {
        'file': ('sample.txt', open('sample.txt', 'rb')),
        'metadata': ('meta.json', open('meta.json', 'rb')),
        'fille': ('samplecsv.csv', open('samplecsv.csv', 'rb')),
        'fie': ('samplepdf.pdf', open('samplepdf.pdf', 'rb'))

    }

    r = requests.post(url=VERMILLION_URL + PUBLISH_ENDPOINT,
                      data=payload,
                      files=files,
                      verify=False)

    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


@when('The consumer downloads the file')
def step_imp(context):
    urd = 'https://localhost/provider/public/'
    r = requests.get(url=urd + res[0], verify=False)
    open('test-resource.public', 'wb').write(r.content)
    context.response = r
    context.status_code = r.status_code
    print(context.status_code, context.response)


