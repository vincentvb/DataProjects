# Twitter Analysis

This project compares the tweets of Donald Trump and Joe Biden by retrieving their tweets using the [TwitterAPI](https://github.com/geduldig/TwitterAPI) client, performs sentiment analysis on them by leveraging Google's [natural language processing client](https://github.com/googleapis/python-language), and outputs multiple charts comparing the results

### Setting up Environment

Ensure you have Python3 and pip installed:

```
brew install python
```

Install project dependencies:

```
pip install -r requirements.txt
```

Follow steps to register with [Twitter's API](https://developer.twitter.com/en/docs/twitter-api/v1) and retrieve an API key. Note: registering with twitter can take a couple of days)

Once you have a proper key, set it as an environment variable:

```
export TWITTER_API_KEY="*place API key here*"
```

Create a [Google Cloud project](https://cloud.google.com/natural-language/docs/quickstart-client-libraries), enable the Google Natural Language API, and download your JSON API key

Once you've downloaded your API key, set the path to it as an environment variable:

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/file/here"
```

### Running the Scripts

After your environment is properly set up, you'll want to run a script that first retrieves all tweets:

```
python retrieve_tweets.py
```

You can then run a script to perform a sentiment analysis on the tweets. The data will be plotted onto charts displayed on your screen:

```
python sentiment_analysis.py
```




