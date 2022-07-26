from google_play_scraper import app
result = app(
    'kr.co.millie.millieshelf',
    lang='ko', # defaults to 'en'
    country='kr' # defaults to 'us'
)

from google_play_scraper import Sort, reviews_all
result = reviews_all(
    'kr.co.millie.millieshelf', #crawling target id
    sleep_milliseconds=10, # defaults to 0
    lang='ko', # defaults to 'en' 'ko'
    country='kr', # defaults to 'us' 'kr'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=None # defaults to None(means all score)
)

print(result)

import pandas as pd
result = pd.DataFrame(result)
result.to_excel('밀리의서재.xlsx', engine='xlsxwriter')
