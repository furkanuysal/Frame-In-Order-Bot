import tweepy
import os
import json

with open('Example.json', 'r') as jsonFile:
    json_data = json.load(jsonFile)

# Twitter API keys with Tweepy
consumer_key = json_data["apiKey"]
consumer_secret = json_data["apiKeySecret"]
access_token = json_data["accessToken"]
access_token_secret = json_data["accessTokenSecret"]
text_to_tweet = json_data["textToTweet"]

# Authentication for access to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)

# File to store the number of photos shared
count_file = 'count.txt'

# Directory name
directory = 'extracted_frames'

# List files in the specified directory
files = os.listdir(directory)
# Find the total number of photos by taking the number of files
total_images = len(files)

# Check the number of shared photos stored in a text file
def get_image_count():
    if not os.path.exists(count_file):
        with open(count_file, 'w') as file:
            file.write('0')
        return 0
    else:
        with open(count_file, 'r') as file:
            return int(file.read())

# Increase the number of photos stored in the file by one
def increment_image_count(count):
    with open(count_file, 'w') as file:
        file.write(str(count + 1))

# Function to share a photo to tweet
def tweet_image():
    image_count = get_image_count()
    next_image_path = f'{directory}/frame_{image_count + 1}.jpg'
    
    if os.path.exists(next_image_path):
        # Tweet metni oluşturma
        tweet_text = f"{text_to_tweet} - Frame {image_count + 1} of {total_images}"

        media = api.media_upload(next_image_path)
        media_id = media.media_id
        
        # Tweet with text and media
        client.create_tweet(text=tweet_text,media_ids=[media_id])
        
        # Increase the number of photos by one
        increment_image_count(image_count)

        print("Successful!")

# Post tweet
tweet_image()
