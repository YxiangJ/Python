import sendgrid
import json
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
API_KEY = 'SENDGRID_API_KEY'

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(API_KEY))


def best_country(str_date):
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date
    })
    stats = json.loads(response.body)
    max_data = max(stats[0]['stats'],
                   key=lambda a: a['metrics']['unique_clicks'])
    return (max_data['name'])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
    print('Check your results')
