import csv
import time
from argparse import ArgumentParser

if __name__ == '__main__':
    # ---------------------------------------------------------------------------------------------------------------
    parser = ArgumentParser()
    parser.add_argument('-f', '--first_name', required=True)
    parser.add_argument('-ln', '--last_name', required=True)
    parser.add_argument('-hs', '--hours', required=True)
    parser.add_argument('-m', '--minutes', required=True)
    parser.add_argument('-s', '--seconds', required=True)
    args = parser.parse_args()

    time_ = ['00:00:03', '00:00:02', '00:00:01']
    for i in time_:
        print(i)
        time.sleep(1)
    print('ALARM!!!')
    new_file = 'Log.csv'
    with open(new_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['First name', 'last name', 'hours', 'minutes', 'seconds'])
        writer.writerow([args.first_name, args.last_name, args.hours, args.minutes, args.seconds])
