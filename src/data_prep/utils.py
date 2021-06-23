import csv

#weights = [
#        0.004566,
#        0.027907,
#        -0.009775,
#        -0.053061,
#        0.033834,
#        -0.047613,
#        0.103660,
#        -0.071858,
#        -0.002625,
#        -0.066756,
#        0.000692,
#        -0.002325,
#        0.017685,
#        -0.019228,
#        0.030732,
#        -0.007789,
#        -0.030373,
#        -0.003513,
#        0.023970,
#        0.074805
#]

weights = [
        -0.010398,
        0.043950,
        -0.002628,
        -0.058483,
        0.034655,
        -0.030784,
        0.107349,
        -0.052476,
        0.007441,
        -0.059779,
        -0.011136,
        0.004679,
        0.016168,
        0.001367,
        0.021853,
        0.003386,
        -0.023225,
        0.004376,
        0.033544,
        0.062450
]

close = [
    12497,
    12535.99,
    12327.95,
    12078.65,
    11746.77,
    11549.42,
    11683.36,
    11544.61,
    12017.19,
    12125.12,
    12629.96,
    12581.45,
    12555.19,
    12780.33,
    12809.06,
    12900.72,
    12715.84,
    12977.2,
    12993.71,
    13145.17,
    13050.92
]

def read_close():

    vals = list()
    f_vals = list()

    with open("../../data/DAX_6_11_2017_to_6_11_2020.csv") as f:
        reader = csv.reader(f)

        for line in reader:
            vals.append(line[2])

        for val in vals[1:]:
            f_vals.append(float(val))

    return f_vals

close_all = read_close()


def get_diff(close_data):

    df = list()

    for i in range(0, len(close_data)-1):
        df.append(round((close_data[i]-close_data[i+1])*100)/100)

    return df

def sign(num):
    """
    +1 when positive, -1 when negative and 0 at 0
    """

    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
