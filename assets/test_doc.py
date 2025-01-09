api_docs = [
    {
        "name": "Funding Milestones",
        "endpoint": "https://api.crustdata.com/data_lab/funding_milestone_timeseries/",
        "description": "Use this request to get a time-series of funding milestones with  company_id equal to any one of [637158, 674265, 674657]",
        "curl": 'curl --request POST --url https://api.crustdata.com/data_lab/funding_milestone_timeseries/ --header \'Accept: application/json, text/plain, */*\' --header \'Accept-Language: en-US,en;q=0.9\' --header \'Authorization: Token $auth_token\' --header \'Content-Type: application/json\' --header \'Origin: https://crustdata.com\' --header \'Referer: https://crustdata.com/\' --data \'{"filters":{"op":"or","conditions":[{"column":"company_id","type":"in","value":[637158,674265,674657]}]},"offset":0,"count":1000,"sorts":[]}\'',
        "response": "https://jsonhero.io/j/XDfprlYDbOvf",
    },
]
