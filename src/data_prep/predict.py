weights = [
        0.004566,
        0.027907,
        -0.009775,
        -0.053061,
        0.033834,
        -0.047613,
        0.103660,
        -0.071858,
        -0.002625,
        -0.066756,
        0.000692,
        -0.002325,
        0.017685,
        -0.019228,
        0.030732,
        -0.007789,
        -0.030373,
        -0.003513,
        0.023970,
        0.074805
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

def get_delta(close):
    delta_close = list()

    for i in range(len(close)-1):
        delta_close.append(close[i]-close[i-1])

    return delta_close

def predict(weights, delta_close):
    if len(weights) != len(delta_close):
        print("Lengths do not match.")
        print(len(delta_close))
        exit()

    summ = 0;

    for i in range(len(weights)):
        summ += weights[i]*delta_close[i]

    return summ

def main():
    delta_close = get_delta(close)
    summ = predict(weights, delta_close)

    print(summ)

if __name__ == '__main__':
    main()
