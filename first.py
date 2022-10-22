import csv

metric_keywords = [
    'click',
    'visit',
    'rate',
    'cost',
    'spend',
    'visit',
    'duration',
    'time',
    'download',
    'attrition',
    'cpa',
    'cpc'
    'roi',
    'cta',
    'ctr',
    'subscriber',
    'engagement',
    'reach',
    'impression',
    'follower',
    'mention',
    'discrepancy',
    'number',
    'conversion',
    'action',
    'purchase'
    'cart'
    'count',
    'unique',
    'avg',
    'quartile',
    'install',
    'revenue',
    'distribution',
    'speed',
    'session',
    'pages'
]

out_keywords = [
    'suspended',
    'policy',
    'android',
    'tag',
    'timestamp',
    ' id'
    '_id',
]

total_row_num = 31421

with open('first_data.csv') as data_inp:
    csv_data = csv.reader(data_inp, delimiter=',')

    counter = 0
    for row in csv_data:
        for field in row[2:]:

            field = field.lower()
            if any(map(field.__contains__, metric_keywords)) and not any(map(field.__contains__, out_keywords)):
                counter += 1
                break

    print(round(counter / total_row_num * 100), '%')
