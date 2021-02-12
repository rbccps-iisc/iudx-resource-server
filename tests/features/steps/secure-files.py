import json
import requests
from behave import when
import urllib3
from auth_vars import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

VERMILLION_URL = 'https://localhost'
SEARCH_ENDPOINT = '/search'

PUBLISH_ENDPOINT= '/publish'


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#XXX Secure-files tests need definition here
@when('The consumer publishes along with a valid token')
def step_imp(context):
    params = (
    ('id', res[2]),
    ('token', tokens["master"]),
)

    files = {
    'file': ('sample.txt', open('sample.txt', 'rb')),
    'metadata': ('meta.json', open('meta.json', 'rb')),
}

    r = requests.post('https://localhost/publish', params=params, files=files, verify=False)
    
    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer publishes along with a file and timeseries data')
def step_imp(context):
    params = (
    ('id', res[2]),
    ('token', tokens["master"]),
)
    data = {"data": {"hello": "world"}}
    headers = {'Content-type': 'multipart/form-data'}
    files = {
    'file': ('sample.txt', open('sample.txt', 'rb')),
    'metadata': ('meta.json', open('meta.json', 'rb')),
}

    r = requests.post('https://localhost/publish', data=data,params=params, files=files, verify=False, headers = headers)

    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer publishes along with an invalid token')
def step_imp(context):
    params = (
    ('id', res[2]),
    ('token', generate_random_chars()),
)

    files = {
    'file': ('sample.txt', open('sample.txt', 'rb')),
    'metadata': ('meta.json', open('meta.json', 'rb')),
}

    r = requests.post('https://localhost/publish', params=params, files=files, verify=False)

    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)


@when('The consumer publishes along with an empty token')
def step_imp(context):
    params = (
    ('id', res[2]),
    ('token', ''),
)

    files = {
    'file': ('sample.txt', open('sample.txt', 'rb')),
    'metadata': ('meta.json', open('meta.json', 'rb')),
}

    r = requests.post('https://localhost/publish', params=params, files=files, verify=False)

    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer publishes along with an invalid resource id')
def step_imp(context):
    params = (
    ('id', generate_random_chars()),
    ('token', tokens["master"]),
)

    files = {
    'file': ('sample.txt', open('sample.txt', 'rb')),
    'metadata': ('meta.json', open('meta.json', 'rb')),
}

    r = requests.post('https://localhost/publish', params=params, files=files, verify=False)

    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer publishes along with an empty resource id')
def step_imp(context):
    params = (
    ('id', ''),
    ('token', tokens["master"]),
)

    files = {
    'file': ('sample.txt', open('sample.txt', 'rb')),
    'metadata': ('meta.json', open('meta.json', 'rb')),
}

    r = requests.post('https://localhost/publish', params=params, files=files, verify=False)

    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)



@when('The consumer downloads file by passing a valid token')
def step_imp(context):
    params = (
    ('id', res[2]),
    ('token', tokens["master"]),
)

    r = requests.get('https://localhost/download', params=params, verify=False)
    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)




@when('The consumer downloads file by passing an invalid token')
def step_imp(context):
    params = (
    ('id', res[2]),
    ('token', generate_random_chars()),
)

    r = requests.get('https://localhost/download', params=params, verify=False)
    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer downloads file by passing an empty token')
def step_imp(context):
    params = (
    ('id', res[2]),
        ('token', ''),
)

    r = requests.get('https://localhost/download', params=params, verify=False)
    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer downloads file by passing an invalid resource id')
def step_imp(context):
    params = (
    ('id', generate_random_chars()),
    ('token', tokens["master"]),
    
)

    r = requests.get('https://localhost/download', params=params, verify=False)
    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer downloads file by passing an empty resource id')
def step_imp(context):
    params = (
    ('id', ''),
    ('token', tokens["master"]),
)

    r = requests.get('https://localhost/download', params=params, verify=False)
    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer downloads file by passing only token')
def step_imp(context):
    params = (
    
    ('token', tokens["master"]),
)

    r = requests.get('https://localhost/download', params=params, verify=False)
    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

@when('The consumer downloads file by passing multiple resource ids and a token')
def step_imp(context):
    params = {
            "id": [
                res[2],
                res[3]
                ] ,
            "token": tokens["master"]
                
            }

    r = requests.get('https://localhost/download', params=params, verify=False)
    context.response= r
    context.status_code=r.status_code
    print(context.status_code,context.response)

    
