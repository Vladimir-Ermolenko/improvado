import csv
from datetime import datetime

with open('second_data.csv') as data_inp:
    csv_data = list(csv.reader(data_inp, delimiter=','))

    managers = {
        '1.0': {'deals': 0, 'first_touches_num': 0, 'first_touches_list': {}, 'sum_deal_length': 0, 'last_date': datetime(1, 1, 1, 0, 0), 'manager_name': 'Justin Beiber'},
        '2.0': {'deals': 0, 'first_touches_num': 0, 'first_touches_list': {}, 'sum_deal_length': 0, 'last_date': datetime(1, 1, 1, 0, 0), 'manager_name': 'Kylie Jenner'},
        '3.0': {'deals': 0, 'first_touches_num': 0, 'first_touches_list': {}, 'sum_deal_length': 0, 'last_date': datetime(1, 1, 1, 0, 0), 'manager_name': 'Joe Biden'}
    }

    for index, row in enumerate(csv_data):
        manager_id = row[3]
        client_id = row[0]
        event_name = row[2]
        date = datetime.strptime(row[1], '%Y-%m-%d')

        if date > managers[manager_id]['last_date']:
            managers[manager_id]['last_date'] = date

        if event_name == 'first_touch':
            managers[manager_id]['first_touches_num'] += 1
            managers[manager_id]['first_touches_list'][client_id] = date

        elif event_name == 'deal':
            prev_row = csv_data[index - 1]
            next_row = csv_data[index + 1]

            if manager_id == prev_row[3]:
                date_first_touch = datetime.strptime(prev_row[1], '%Y-%m-%d')
                delta = (date - date_first_touch).days

                if delta > 0:
                    managers[manager_id]['deals'] += 1
                    managers[manager_id]['sum_deal_length'] += delta

                else:
                    managers[manager_id]['first_touches_num'] -= 1
                    managers[manager_id]['first_touches_list'].pop(client_id)
            else:
                managers[prev_row[3]]['first_touches_num'] -= 1
                managers[prev_row[3]]['first_touches_list'].pop(client_id)

    for manager, values in managers.items():
        avg_deal_time = round(values['sum_deal_length'] / values['deals'])

        for client_id, date_first_touch in list(values['first_touches_list'].items()):
            if (values['last_date'] - date_first_touch).days < avg_deal_time:
                values['first_touches_num'] -= 1
                values['first_touches_list'].pop(client_id)

        conversion = str(round(values['deals'] / (values['first_touches_num'] + values['deals']) * 100, 2))
        print(values['manager_name'] + ': ' + conversion + ' %')
