import schedule
import time
from hashtags import hashtags


def post():
    print('Creating Post')


schedule.every(3).seconds.do(post)

while True:
    schedule.run_pending()
    time.sleep(1)