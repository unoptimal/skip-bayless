from textblob import TextBlob
import csv

total_tweets = 0
lebron_tweets = 0
total_polarity = 0
total_subjectivity = 0
keywords = ['LeBron', 'LBJ', 'Bron']

with open('data.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # Skip the header row
    for row in csv_reader:
        total_tweets+=1
        tweet = row[0]
        if any(keyword in tweet for keyword in keywords):
            lebron_tweets += 1
            textblob = TextBlob(tweet)
            total_polarity += textblob.sentiment.polarity
            total_subjectivity += textblob.sentiment.subjectivity
            print("TWEET:", tweet)
            print("POLARITY:", textblob.sentiment.polarity)

    avg_polarity = total_polarity / lebron_tweets
    avg_subjectivity = total_subjectivity / lebron_tweets