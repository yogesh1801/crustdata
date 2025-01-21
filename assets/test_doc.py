api_docs = [
    {
        "name": "Funding Milestones",
        "endpoint": "https://api.crustdata.com/data_lab/funding_milestone_timeseries/",
        "description": "Use this request to get a time-series of funding milestones with company_id equal to any one of [637158, 674265, 674657]",
        "curl": '''curl --request POST --url https://api.crustdata.com/data_lab/funding_milestone_timeseries/ --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language: en-US,en;q=0.9' --header 'Authorization: Token $auth_token' --header 'Content-Type': 'application/json' --header 'Origin': 'https://crustdata.com' --header 'Referer': 'https://crustdata.com/' --data '{"filters":{"op":"or","conditions":[{"column":"company_id","type":"in","value":[637158,674265,674657]}]},"offset":0,"count":1000,"sorts":[]}' ''',
        "python": '''import requests
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Token $auth_token',
    'Content-Type': 'application/json',
    'Origin': 'https://crustdata.com',
    'Referer': 'https://crustdata.com',
}
json_data = {
    'filters': {
        'op': 'or',
        'conditions': [
            {'column': 'company_id', 'type': 'in', 'value': [637158, 674265, 674657]},
        ],
    },
    'offset': 0,
    'count': 1000,
    'sorts': [],
}
response = requests.post('https://api.crustdata.com/data_lab/funding_milestone_timeseries/', headers=headers, json=json_data)
print(response.text)''',
        "response": "https://jsonhero.io/j/XDfprlYDbOvf",
    },
    {
        "name": "Decision Makers/People Info",
        "endpoint": "https://api.crustdata.com/data_lab/decision_makers/",
        "description": "This request retrieves decision maker data for a given company. It allows filtering based on titles, LinkedIn profile URLs, and more.",
        "curl": '''curl --request POST --url https://api.crustdata.com/data_lab/decision_makers/ --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language: en-US,en;q=0.9' --header 'Authorization: Token $auth_token' --header 'Content-Type': 'application/json' --header 'Origin': 'http://localhost:3000' --header 'Referer': 'http://localhost:3000/' --data '{"filters":{"op": "and", "conditions": [{"column": "company_id", "type": "in", "value": [632328]}]},"offset":0,"count":100,"sorts":[]}' ''',
        "python": '''import requests
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Token $auth_token',
    'Content-Type': 'application/json',
    'Origin': 'http://localhost:3000',
    'Referer': 'http://localhost:3000',
}
json_data = {
    'filters': {
        'op': 'and',
        'conditions': [
            {'column': 'company_id', 'type': 'in', 'value': [632328]},
        ],
    },
    'offset': 0,
    'count': 100,
    'sorts': [],
}
response = requests.post('https://api.crustdata.com/data_lab/decision_makers/', headers=headers, json=json_data)
print(response.text)''',
        "response": "https://jsonhero.io/j/QSAlhbuflhie",
    },
    {
        "name": "LinkedIn Employee Headcount and LinkedIn Follower Count",
        "endpoint": "https://api.crustdata.com/data_lab/headcount_timeseries/",
        "description": "Use this request to get weekly and monthly time series of employee headcount as a JSON blob.",
        "curl": '''curl 'https://api.crustdata.com/data_lab/headcount_timeseries/' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.9' -H 'Authorization: Token $auth_token' -H 'Content-Type': 'application/json' -H 'Origin': 'https://crustdata.com' -H 'Referer': 'https://crustdata.com' --data-raw '{"filters":{"op":"or","conditions":[{"column":"company_id","type":"=","value":634995},{"column":"company_id","type":"=","value":680992},{"column":"company_id","type":"=","value":673947},{"column":"company_id","type":"=","value":631811}]},"offset":0,"count":100,"sorts":[]}' ''',
        "python": '''import requests
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Token $auth_token',
    'Content-Type': 'application/json',
    'Origin': 'https://crustdata.com',
    'Referer': 'https://crustdata.com',
}
json_data = {
    'filters': {
        'op': 'or',
        'conditions': [
            {'column': 'company_id', 'type': '=', 'value': 634995},
            {'column': 'company_id', 'type': '=', 'value': 680992},
            {'column': 'company_id', 'type': '=', 'value': 673947},
            {'column': 'company_id', 'type': '=', 'value': 631811},
        ],
    },
    'offset': 0,
    'count': 100,
    'sorts': [],
}
response = requests.post('https://api.crustdata.com/data_lab/headcount_timeseries/', headers=headers, json=json_data)
print(response.text)''',
        "response": "https://jsonhero.io/j/bd2OKMSu8ZQ0/editor"
    },
    {
        "name": "Glassdoor Profile Metrics",
        "endpoint": "https://api.crustdata.com/data_lab/glassdoor_profile_metric/Table/",
        "description": "Use this request to get the rating of a company on Glassdoor.",
        "curl": '''curl --request POST --url https://api.crustdata.com/data_lab/glassdoor_profile_metric/Table/ --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language': 'en-US,en;q=0.9' --header 'Authorization: Token $token' --header 'Content-Type': 'application/json' --header 'Origin': 'https://crustdata.com' --data '{"tickers":[],"dataset":{"name":"glassdoor_profile_metric","id":"glassdoorprofilemetric"},"filters":{"op":"and","conditions":[{"column":"company_id","type":"in","value":[680992,673947,631280,636304,631811],"allow_null":false}]},"groups":[],"aggregations":[],"functions":[],"offset":0,"count":100,"sorts":[]}' ''',
        "python": '''import requests
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Token $token',
    'Content-Type': 'application/json',
    'Origin': 'https://crustdata.com',
}
json_data = {
    'tickers': [],
    'dataset': {'name': 'glassdoor_profile_metric', 'id': 'glassdoorprofilemetric'},
    'filters': {
        'op': 'and',
        'conditions': [
            {'column': 'company_id', 'type': 'in', 'value': [680992, 673947, 631280, 636304, 631811], 'allow_null': False},
        ],
    },
    'offset': 0,
    'count': 100,
    'sorts': [],
}
response = requests.post('https://api.crustdata.com/data_lab/glassdoor_profile_metric/Table/', headers=headers, json=json_data)
print(response.text)''',
        "response": "https://jsonhero.io/j/SdGsOnEIJ33x/editor"
    },
    {
        "name": "G2 Profile Metrics",
        "endpoint": "https://api.crustdata.com/data_lab/g2_profile_metric/",
        "description": "Get company G2 profile data for reviews and scores on G2.",
        "curl": '''curl --request POST --url https://api.crustdata.com/data_lab/g2_profile_metric/ --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language': 'en-US,en;q=0.9' --header 'Authorization': 'Token $auth_token' --header 'Content-Type': 'application/json' --header 'Origin': 'https://crustdata.com' --data '{"filters":{"op":"or","conditions":[{"column":"company_id","type":"in","value":[637158,674265,674657]}]},"offset":0,"count":1000,"sorts":[]}' ''',
        "python": '''import requests
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Token $auth_token',
    'Content-Type': 'application/json',
    'Origin': 'https://crustdata.com',
    'Referer': 'https://crustdata.com',
}
json_data = {
    'filters': {
        'op': 'or',
        'conditions': [
            {'column': 'company_id', 'type': 'in', 'value': [637158, 674265, 674657]},
        ],
    },
    'offset': 0,
    'count': 1000,
    'sorts': [],
}
response = requests.post('https://api.crustdata.com/data_lab/g2_profile_metric/', headers=headers, json=json_data)
print(response.text)''',
        "response": "https://jsonhero.io/j/aGHvIu7d9k6N",
    },
    {
        "name": "Web Traffic",
        "endpoint": "https://api.crustdata.com/data_lab/web_traffic/",
        "description": "Use this request to get the weekly and monthly time series of web traffic for a company. The data is retrieved in a JSON blob.",
        "curl": '''curl --request POST --url https://api.crustdata.com/data_lab/web_traffic/ --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language: en-US,en;q=0.9' --header 'Authorization: Token $auth_token' --header 'Content-Type': 'application/json' --header 'Origin': 'https://crustdata.com' --header 'Referer': 'https://crustdata.com' --data '{"filters":{"op":"or","conditions":[{"column":"company_id","type":"in","value":[637158,674265,674657]}]},"offset":0,"count":1000,"sorts":[]}' ''',
        "python": '''import requests
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Token $auth_token',
    'Content-Type': 'application/json',
    'Origin': 'https://crustdata.com',
    'Referer': 'https://crustdata.com',
}
json_data = {
    'filters': {
        'op': 'or',
        'conditions': [
            {'column': 'company_id', 'type': 'in', 'value': [637158, 674265, 674657]},
        ],
    },
    'offset': 0,
    'count': 1000,
    'sorts': [],
}
response = requests.post('https://api.crustdata.com/data_lab/web_traffic/', headers=headers, json=json_data)
print(response.text)''',
        "response": "https://jsonhero.io/j/aGHvIu7d9k6N",
    },
    {
        "name": "Investor Portfolio",
        "endpoint": "https://api.crustdata.com/data_lab/investor_portfolio/",
        "description": "Use this request to get the portfolio details of an investor, either by UUID or name.",
        "curl": '''curl --request GET --url https://api.crustdata.com/data_lab/investor_portfolio/ --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language: en-US,en;q=0.9' --header 'Authorization: Token $auth_token' --data '{"investor_uuid": "UUID_placeholder"}' ''',
        "python": '''import requests
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Token $auth_token',
}
params = {
    'investor_uuid': 'UUID_placeholder',  # Replace with actual UUID or name
}
response = requests.get('https://api.crustdata.com/data_lab/investor_portfolio/', headers=headers, params=params)
print(response.text)''',
        "response": "https://jsonhero.io/j/bZ2YSQljvYwB",
    },
    {
        "name": "Investor Portfolio by Name",
        "endpoint": "https://api.crustdata.com/data_lab/investor_portfolio_by_name/",
        "description": "This request fetches investor portfolio data by the investor's name.",
        "curl": '''curl --request GET --url https://api.crustdata.com/data_lab/investor_portfolio_by_name/ --header 'Accept: application/json, text/plain, */*' --header 'Accept-Language: en-US,en;q=0.9' --header 'Authorization: Token $auth_token' --data '{"investor_name": "Investor Name"}' ''',
        "python": '''import requests
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Token $auth_token',
}
params = {
    'investor_name': 'Investor Name',  # Replace with actual investor name
}
response = requests.get('https://api.crustdata.com/data_lab/investor_portfolio_by_name/', headers=headers, params=params)
print(response.text)''',
        "response": "https://jsonhero.io/j/5yIb8n1xYv3D",
    }
]
