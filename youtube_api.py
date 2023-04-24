from googleapiclient.discovery import build
import requests

class CallYoutubeAPI:

    def call_yt_api(self, username):
        __key = 'AIzaSyDBHExH77HarJQDG5x84BH2zhqn7ADibTg'
        youtube = build('youtube', 'v3', developerKey=__key)
        request = youtube.channels().list(
            part = 'statistics',
            forUsername = username
        )
        response = request.execute()
        if 'items' in response.keys():
            viewcount = response['items'][0]['statistics']['viewCount']
            return int(viewcount)
        else:
            return "Error"

class CompareWithYoutuber:
    def __init__(self):
        self.channel_to_compare = None
        self.youtuber_views = 0
        self.your_views = 0

    def grab_channel_views(self):
        self.channel_to_compare = input('Enter the exact channel id of the youtuber you want to compare yourself with: ')
        self.youtuber_views = CallYoutubeAPI.call_yt_api(self, self.channel_to_compare)
        if self.youtuber_views == "Error":
            print("Could not retrieve viewcount. Please try a different channel.")
            self.grab_channel_views()

    def comparison(self):
        self.your_views = int(input('Enter the total number of your channel views: '))
        difference_in_views = self.youtuber_views - self.your_views
        print(f"The difference between {self.channel_to_compare}'s channel and your channel is {difference_in_views} views.")

'''
CREDITS:
Grabbing the API from YOUTUBE was executed by watching Corey Schafer's video https://www.youtube.com/watch?v=th5_9woFJmk&ab_channel=CoreySchafer
'''

# my_api = CompareWithYoutuber()
# my_api.grab_channel_views()
