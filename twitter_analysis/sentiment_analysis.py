from google.cloud import language_v1
import pandas as pd
import re
import pickle
import matplotlib.pyplot as plt

client = language_v1.LanguageServiceClient()

plt.style.use('fivethirtyeight')


def plotAccount(user_name):
    '''
    Reads tweets for a given Twitter username from disk, sends the message content to Google's API, and plots the results

        Parameters:
            user_name (string): A string of the user name that's being retrieved

        Returns:
            None
    '''
    data = pd.read_csv(f'{user_name}_tweets.csv')

    sentimentScore = []
    sentimentMagnitude = []

    for message in data['text']:
        # Filter out url's in tweets
        filteredMessage = re.sub(r'http\S+', '', message)
        # If tweet only contained url, don't perform sentiment analysis
        if len(filteredMessage) == 0:
            sentimentScore.append(float("NaN"))
            sentimentMagnitude.append(float("NaN"))
        else:
            document = {'content': filteredMessage,
                        'type_': 'PLAIN_TEXT', 'language': 'en'}
            response = client.analyze_sentiment(
                request={'document': document,
                         'encoding_type': language_v1.EncodingType.UTF8}
            )
            sentimentScore.append(response.document_sentiment.score)
            sentimentMagnitude.append(response.document_sentiment.magnitude)

    data['sentiment_score'] = sentimentScore
    data['sentiment_magnitude'] = sentimentMagnitude

    data['formatted_date'] = pd.to_datetime(data['created_at'])
    grouped_data = data.groupby(
        by=data['formatted_date'].dt.week).mean().tail(12)

    plt.plot(grouped_data.index, grouped_data['sentiment_score'])
    plt.plot(grouped_data.index,
             grouped_data['sentiment_magnitude'])
    plt.legend(['Sentiment', 'Magnitude'], loc='upper right')


for name in ['JoeBiden', 'realDonaldTrump']:
    plotAccount(name)

plt.xlabel('Weeks Until Election')
plt.ylabel('Score (Between -1 and 1)')
plt.title('Sentiment Score Analysis')
plt.xticks(rotation=45)
plt.legend(['Biden', 'Trump'], loc='upper right')
plt.show()
