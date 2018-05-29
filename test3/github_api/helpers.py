# coding: utf-8 



import requests 


def call_github_api():
    url = 'https://api.github.com/repos/rails/rails/events?per_page=100'
    response = requests.get(url)
    return response.json() 


def refine_data(data):
    result = {}
    for d in data:
        key = d['actor']['login']
        if not key in result:
            result[key] = {
                'TotalEvent': 0        
            }
        result[key]['TotalEvent'] += 1
        
        event_type = d['type']
        if not event_type in result[key]:
            result[key][event_type] = 0
        result[key][event_type] += 1
        
    return result

def make_response(data, sort=None):
    result = []  
    for key in data:
        temp = {
            'login': key,
            'events': data[key]
        }
        result.append(temp)
    return result

