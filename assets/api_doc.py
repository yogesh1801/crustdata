api_docs = [
    {
        "name": "Job Listings",
        "endpoint": "https://api.crustdata.com/data_lab/job_listings/Table/",
        "notes": [
            "To retrieve all the jobs listings, keep iterating over the offset field in the payload.",
            "Do not increase limit beyond 100 as the result will be truncated without any ordering.",
            "For real-time fetch, use sync_from_source. Allows fetching up to 100 jobs in real-time (use background_task if all the jobs needs to be fetched). Works for 1 company per request",
            "For background processing, use background_task to fetch and update listings for up to 10 companies at a time. Updates job listings for up to 10 companies at a time in the background. Returns a task ID in the response. Use this task ID to check the status or results via the endpoint task/result/<task_id>",
        ],
        "description": "Use this request to get job listings that were last updated by the company on 1st Feb, 2024 for all companies with company_id equal to any one of [680992, 673947, 631280, 636304, 631811].",
        "parameters": {
            "filters": {
                "description": "An object containing the filter conditions.",
                "type": "object",
                "required": True,
            },
            "offset": {
                "description": "The starting point of the result set. Default value is 0.",
                "type": "integer",
                "required": True,
            },
            "limit": {
                "description": "The number of results to return in a single request. Maximum value is 100. Default value is 100.",
                "type": "integer",
                "required": True,
            },
            "sorts": {
                "description": "An array of sorting criteria.",
                "type": "array",
                "required": False,
            },
        },
        "curl": 'curl --request POST --url https://api.crustdata.com/data_lab/job_listings/Table/ --header \'Accept: application/json, text/plain, */*\' --header \'Accept-Language: en-US,en;q=0.9\' --header \'Authorization: Token $token\' --header \'Content-Type: application/json\' --header \'Origin: https://crustdata.com\' --header \'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36\' --data \'{"tickers":[],"dataset":{"name":"job_listings","id":"joblisting"},"filters":{"op":"and","conditions":[{"column":"company_id","type":"in","value":[7576,680992,673947,631280,636304,631811]},{"column":"date_updated","type":">","value":"2024-02-01"}]},"groups":[],"aggregations":[],"functions":[],"offset":0,"limit":100,"sorts":[]}\'',
    },
    {
        "name": "Funding Milestones",
        "endpoint": "https://api.crustdata.com/data_lab/funding_milestone_timeseries/",
        "description": "Use this request to get a time-series of funding milestones with  company_id equal to any one of [637158, 674265, 674657]",
        "curl": 'curl --request POST --url https://api.crustdata.com/data_lab/funding_milestone_timeseries/ --header \'Accept: application/json, text/plain, */*\' --header \'Accept-Language: en-US,en;q=0.9\' --header \'Authorization: Token $auth_token\' --header \'Content-Type: application/json\' --header \'Origin: https://crustdata.com\' --header \'Referer: https://crustdata.com/\' --data \'{"filters":{"op":"or","conditions":[{"column":"company_id","type":"in","value":[637158,674265,674657]}]},"offset":0,"count":1000,"sorts":[]}\'',
    },
    {
        "name": "Decision Makers/People Info",
        "descriptions": [
            {
                "description": "All decision makers: for a given company_id=632328",
                "decision_maker_titles": {
                    "founders": [
                        "CEO",
                        "Founder",
                        "Co-founder",
                        "Co founder",
                        "Cofounder",
                        "Co-fondateur",
                        "Fondateur",
                        "Cofondateur",
                        "Cofondatrice",
                        "Co-fondatrice",
                        "Fondatrice",
                    ],
                    "executive_officers": [
                        "Chief Executive Officer",
                        "Chief Technical Officer",
                        "Chief Technology Officer",
                        "Chief Financial Officer",
                        "Chief Marketing Officer",
                        "Chief Sales Officer",
                        "Chief Marketing and Digital Officer",
                        "Chief Market Officer",
                    ],
                    "technical_leadership": [
                        "CTO",
                        "VP Engineering",
                        "VP of Engineering",
                        "Vice President Engineering",
                        "Vice President of Engineering",
                        "Head Engineering",
                        "Head of Engineering",
                    ],
                    "marketing_leadership": [
                        "CMO",
                        "Chief Marketing Officer",
                        "Chief Marketing and Digital Officer",
                        "Chief Market Officer",
                        "VP Marketing",
                        "VP of Marketing",
                        "Vice President Marketing",
                        "Vice President of Marketing",
                    ],
                    "sales_leadership": [
                        "Chief Sales Officer",
                        "VP Sales",
                        "VP of Sales",
                        "Vice President Sales",
                        "Vice President of Sales",
                        "Vice President (Sales & Pre-Sales)",
                        "Head Sales",
                        "Head of Sales",
                    ],
                    "product_leadership": [
                        "VP Product",
                        "VP of Product",
                        "Vice President Product",
                        "Vice President of Product",
                        "Head of Product",
                        "Head Product",
                    ],
                    "software_leadership": [
                        "VP Software",
                        "VP of Software",
                        "Vice President Software",
                        "Vice President of Software",
                    ],
                    "financial_leadership": ["CFO", "Chief Financial Officer"],
                },
                "curl": 'curl --request POST --url https://api.crustdata.com/data_lab/decision_makers/ --header \'Accept: application/json, text/plain, */*\' --header \'Accept-Language: en-US,en;q=0.9\' --header \'Authorization: Token $auth_token\' --header \'Content-Type: application/json\' --header \'Origin: http://localhost:3000\' --header \'Referer: http://localhost:3000/\' --data \'{"filters":{"op": "and", "conditions": [{"column": "company_id", "type": "in", "value": [632328]}]},"offset":0,"count":100,"sorts":[]}\'',
            },
            {
                "description": "Decision makers with specific titles: for a given company_id=632328",
                "curl": 'curl --request POST --url https://api.crustdata.com/data_lab/decision_makers/ --header \'Accept: application/json, text/plain, */*\' --header \'Accept-Language: en-US,en;q=0.9\' --header \'Authorization: Token $auth_token\' --data \'{"filters":{"op":"or","conditions":[{"column":"company_id","type":"in","value":[632328]},{"column":"title","type":"in","value":["vice president","chief"]}]},"offset":0,"count":100,"sorts":[]}\'',
            },
            {
                "description": "People profiles by their LinkedIn’s “flagship_url",
                "curl": 'curl --request POST --url https://api.crustdata.com/data_lab/decision_makers/ --header \'Accept: application/json, text/plain, */*\' --header \'Accept-Language: en-US,en;q=0.9\' --header \'Authorization: Token $auth_token\' --header \'Content-Type: application/json\' --data \'{"filters":{"op":"and","conditions":[{"column":"linkedin_flagship_profile_url","type":"in","value":["https://www.linkedin.com/in/alikashani"]}]},"offset":0,"count":100,"sorts":[]}\'',
            },
            {
                "description": "People profiles by their linkedin_urn, For example, decision makers with linkedin_urn as ACwAAAVhcDEBbTdJtuc-KHsdYfPU1JAdBmHkh8I . linkedin_urn is a 30-40 character alphanumeric sequence that includes both uppercase letters and numbers",
                "curl": 'curl --request POST --url https://api.crustdata.com/data_lab/decision_makers/ --header \'Accept: application/json, text/plain, */*\' --header \'Accept-Language: en-US,en;q=0.9\' --header \'Authorization: Token $auth_token\' --header \'Content-Type: application/json\' --header \'Origin: http://localhost:3000\' --header \'Referer: http://localhost:3000/\' --data \'{"filters":{"op": "or", "conditions": [{"column": "linkedin_profile_urn", "type": "in", "value": ["ACwAAAVhcDEBbTdJtuc-KHsdYfPU1JAdBmHkh8I"]}] },"offset":0,"count":100,"sorts":[]}\'',
            },
        ],
    },
    {
        "name": "LinkedIn Employee Headcount and LinkedIn Follower Count",
        "description": "Use this request to get weekly and monthly timeseries of employee headcount as a JSON blob.You either provide with list a list of Crustdata `company_id`  or `linkedin_id` or `company_website_domain`",
        "curl": 'curl \'https://api.crustdata.com/data_lab/headcount_timeseries/\' -H \'Accept: application/json, text/plain, */*\' -H \'Accept-Language: en-US,en;q=0.9\' -H \'Authorization: Token $auth_token\' -H \'Content-Type: application/json\' -H \'Origin: https://crustdata.com\' -H \'Referer: https://crustdata.com\' --data-raw \'{"filters":{"op": "or","conditions":[{"column": "company_id","type": "=","value": 634995},{"column": "company_id","type": "=","value": 680992},{"column": "company_id","type": "=","value": 673947},{"column": "company_id","type": "=","value": 631811}]},"offset": 0,"count": 100,"sorts":[]}\' --compressed',
    },
]
