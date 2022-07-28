# Importing the tiktok Python SDK
# Library used to fetch tik tok data (API)
from TikTokApi import TikTokApi as tiktok
import json
# Import data processing helper
from helpers import process_results
# Import pandas to create DF
import pandas as pd
# Import sys dependency to extract command line arguments
import sys

def get_data(hashtag, n_videos):

    # Get cookie data eg. s_v_web_id:"verify_163c3f592728f678bf2e6d0b3cfef043"
    verifyFp = "verify_163c3f592728f678bf2e6d0b3cfef043"

    # Setup instance, custom_verifyFp is cookie data from tiktok to scrape it (RT scraper)
    #api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

    # Get data by hashtag
    # Code for V5 of TikTokApi
    with tiktok(custom_verify_fp=verifyFp, use_test_endpoints=True) as api:

        # Fetch data with the hashtag
        trending_hash = api.hashtag(name=hashtag)

        # Fetch videos with the hashtag (raw data)
        trending  = [video.as_dict for video in trending_hash.videos(count=n_videos)]

        # Process data: Nice and clean JSON output
        flattened_data = process_results(trending)
        
        # # Export to JSON file
        # with open('export.json', 'w') as f:
        #     json.dump(flattened_data, f)

        # Convert the preprocessed data to dataframe
        df = pd.DataFrame.from_dict(flattened_data, orient='index')
        df.to_csv('tiktokdata.csv', index=False)

# Run it in the command line
if __name__ == '__main__':
    # Fist command: hashtag
    # Second command: number of videos to load
    get_data(sys.argv[1], int(sys.argv[2]))