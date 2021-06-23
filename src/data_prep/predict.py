import utils
from matplotlib import pyplot as plt
from numpy import arange

def get_delta(close):
    delta_close = list()

    for i in range(len(close)-1):
        delta_close.append(close[i]-close[i-1])

    return delta_close


def check_input(weights, delta_close):
    if len(weights) != len(delta_close):
        print("Lengths do not match.")
        print(len(delta_close))
        print(len(weights))
        return False

    return True


def predict(weights, delta_close):
    if not check_input(weights, delta_close):
        exit()

    summ = 0;

    for i in range(len(weights)):
        summ += weights[i]*delta_close[i]

    return summ


def chart_predict(weights, delta_close, days):
    # if not check_input(weights, delta_close):
    #     exit()

    predicted = list()
    old = list()
    old += delta_close

    for i in range(days):
        summ = predict(utils.weights, old[-len(utils.weights):])
        predicted.append(summ)
        old.append(summ)

    return predicted, old


def main():
    n = 150
    back = 70
    mode = 1
    delta_close = get_delta(utils.close_all[-n:])
    # summ = predict(utils.weights, delta_close[-len(utils.weights):])

    predicted, all = chart_predict(utils.weights, delta_close[:-back], back)

    # Simple Extrapolation
    if mode == 0:
        forward = list()
        forward += utils.close_all[-n:-back]

        for el in predicted:
            forward.append(forward[-1]+el)

        x1 = arange(len(utils.close_all[-n:]))
        x2 = arange(len(forward))

        plt.plot(x2, forward)
        plt.plot(x1, utils.close_all[-n:])

        print(predicted)

        plt.grid("both")
        plt.show()

    # Direction Extrapolation

    elif mode == 1:
        direction_correct = list()
        for i in range(len(delta_close[-back:])):
            direction_correct.append(utils.sign(delta_close[-back:][i]/predicted[i]))

        x = arange(len(direction_correct))

        plt.bar(x, direction_correct)
        plt.show()




if __name__ == '__main__':
    main()
