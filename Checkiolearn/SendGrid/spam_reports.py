import sendgrid
import json
import os
import ssl
import datetime
import time
import calendar

ssl._create_default_https_context = ssl._create_unverified_context
API_KEY = 'SENDGRID_API_KEY'

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(API_KEY))


def how_spammed(str_date):
    end_time = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    start_time = end_time + datetime.timedelta(days=1)
    response = sg.client.suppression.spam_reports.get(query_params={
        'end_time': int(end_time.timestamp()),
        'start_time': int(start_time.timestamp())
    })
    data = json.loads(response.body)
    return len(data)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
    print('Check your results')
