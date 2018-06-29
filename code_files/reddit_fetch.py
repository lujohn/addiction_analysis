import requests
def get_reddit_data(start_timestamp, end_timestamp, subreddit='redditorsinrecovery', content_type='comment'):
    URL = 'https://api.pushshift.io/reddit/search/'
    URL = os.path.join(URL, content_type)
    
    params = {'subreddit': subreddit,
              'after': start_timestamp,
              'before': end_timestamp,
              'size': 200,
              'sort': 'asc'
             }
    r = requests.get(url=URL, params=params)
    json_content = json.loads(r.content.decode())
    data = json_content['data']
    df = pd.DataFrame.from_dict(data)
    while (True):
        last_ts = df['created_utc'].iloc[-1]
        params['after'] = last_ts
        try:
            r = requests.get(url=URL, params=params)
        except SSLError:
            continue
            
        json_content = json.loads(r.content.decode())
        data = json_content['data']
        if not data:
            break

        # Store new batch in dataframe
        df2 = pd.DataFrame.from_dict(data)

        # join with old dataframe
        df = pd.concat([df, df2])
        
    return df