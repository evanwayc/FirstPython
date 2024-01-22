import csv

def read_csv(filename):
    with open(filename, encoding='UTF-8') as file_var:
        csv_reader = csv.reader(file_var)
        for line in csv_reader:
            print(line)


def write_csv(filename):
    with open(filename, 'w', encoding='UTF-8',newline='') as file_var:
        csv_writer = csv.writer(file_var)
        csv_writer.writerow(['name', 'age', 'gender'])
        csv_writer.writerow(['小明', '18', '男'])
        csv_writer.writerow(['小红', '18', '女'])

if __name__ == '__main__':
    filename='test.csv'
    read_csv(filename)
    write_csv(filename)
    read_csv(filename)
