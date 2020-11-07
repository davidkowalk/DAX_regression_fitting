import csv
import utils

def vis(df):

    from matplotlib import pyplot as plt
    from numpy import arange

    x = arange(len(df))

    df.reverse()

    plt.plot(x,df)
    plt.grid(axis = "y")
    plt.show()

def main():

    close_data = list()

    with open("../../data/DAX_6_11_2017_to_6_11_2020.csv", "r", encoding = "utf8") as f:
        reader = csv.reader(f);

        first_line = True

        for line in reader:
            if first_line:
                print(f"Cols: {line}")
                first_line = False
            else:
                close_data.append(float(line[2]))

    df = utils.get_diff(close_data)

    # Average df

    summ = 0

    for p in df:
        summ += p

    print(summ/len(df))

    #for p in df:
    #    print(p)

    print(df)

    vis(df)

if __name__ == '__main__':
    main()
