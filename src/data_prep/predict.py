import utils

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
