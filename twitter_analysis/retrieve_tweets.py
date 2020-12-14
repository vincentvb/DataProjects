from TwitterAPI import TwitterAPI, TwitterPager, TwitterResponse
import csv
import os


def batch_tweets(twitterClient, user_name):
    '''
    Retrieves tweets for a given Twitter user and writes a corresponding csv file to disk

        Parameters:
            twitterClient (TwitterAPI): A TwitterAPI object
            user_name (string): A string of the user name that's being retrieved

        Returns:
            None
    '''

    tweets = []

    requested_tweets = api.request(
        'statuses/user_timeline',
        {'screen_name': user_name, 'count': 25, 'include_rts': False})

    tweets.extend(requested_tweets)

    oldest_current_tweet = tweets[-1]['id'] - 1

    # Due to Twitter API rules, tweets must be batched with maximum of 200 tweets per request
    total_count = 200

    while total_count < 200:
        requested_tweets = api.request(
            'statuses/user_timeline',
            {'screen_name': user_name, 'count': 200,
             'max_id': oldest_current_tweet, 'include_rts': False}
        )

        total_count += 200

        tweets.extend(requested_tweets)

        oldest_current_tweet = tweets[-1]['id'] - 1

    formatted_tweets = [[tweet['id_str'], tweet['created_at'], tweet['text']]
                        for tweet in tweets]

    with open(f'{user_name}_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(formatted_tweets)

    print(f'{user_name} tweets have completed processing')


if os.environ.get('TWITTER_API_KEY') is None:
    raise Exception("Please provide a Twitter API key before running script")
else:
    api = TwitterAPI(os.environ.get('TWITTER_API_KEY'), auth_type='oAuth2')
    for user_name in ['realDonaldTrump', 'JoeBiden']:
        batch_tweets(api, user_name)
