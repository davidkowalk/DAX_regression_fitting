import csv
import utils
from utils import weights
from predict import predict

def test(diff, i):
    summ = 0
    success = 0
    for j in range(len(weights)):
        summ += diff[i+j+1]*weights[j]

    return utils.sign(summ) == utils.sign(diff[i])

def main():

    sheet = list()

    with open("../../data/DAX_6_11_2017_to_6_11_2020.csv", encoding = "utf8") as file:
        reader = csv.reader(file)

        for line in reader:
            sheet.append(line)


    close = list()

    for i in range(1, len(sheet)):
        close.append(float(sheet[i][2]))

    diff = utils.get_diff(close)

    # print(diff)

    success = 0
    for i in range(len(diff)-len(weights)):
        if test(diff, i):
            success += 1

    print(success/(len(diff)-len(weights)))



if __name__ == '__main__':
    main()
