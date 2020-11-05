import csv
import time
import fileinput
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

    list_ = [i for i in range(int(args.seconds))]
    for i in reversed(list_):
        print(f'{args.hours}:{args.minutes}:{i + 1}')
        time.sleep(1)
    print('ALARM!!!')
    new_file = 'Log.csv'
    key_ = ['First name', 'last name', 'hours', 'minutes', 'seconds']
    with open(new_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(key_)
        writer.writerow([args.first_name, args.last_name, args.hours, args.minutes, args.seconds])

