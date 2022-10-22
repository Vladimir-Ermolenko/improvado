import csv

with open('second_data.csv') as data_inp:
    csv_data = list(csv.reader(data_inp, delimiter=','))

    managers = {
        '1.0': {'deals': 0, 'first_touches': 0, 'manager_name': 'Justin Beiber'},
        '2.0': {'deals': 0, 'first_touches': 0, 'manager_name': 'Kylie Jenner'},
        '3.0': {'deals': 0, 'first_touches': 0, 'manager_name': 'Joe Biden'}
    }

    for index, row in enumerate(csv_data):
        manager_id = row[3]
        client_id = row[0]
        event_name = row[2]

        if event_name == 'first_touch':
            managers[manager_id]['first_touches'] += 1
        elif event_name == 'deal':
            prev_row = csv_data[index - 1]
            next_row = csv_data[index + 1]

            if manager_id == prev_row[3] and prev_row[0] == client_id:
                managers[manager_id]['deals'] += 1
            elif manager_id == next_row[3] and next_row[0] == client_id:
                managers[manager_id]['deals'] += 1

    for manager_data in managers.values():
        print(manager_data['manager_name'] + ': ' +
              str(round(manager_data['deals'] / manager_data['first_touches'] * 100, 2)) + ' %')
