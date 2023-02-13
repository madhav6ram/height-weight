import matplotlib.pyplot as plt


# Implemented using least squares regression method
def linear_regression(x, y, opt, var, n):
    sum_x = sum(height)
    sum_y = sum(weight)
    sum_x_sq = sum([i ** 2 for i in height])
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])

    slope = (n * sum_xy - (sum_x * sum_y)) / (n * sum_x_sq - (sum_x ** 2))
    y_intercept = (sum_y - slope * sum_x) / n

    # y = mx+c
    # return weight
    if opt == "w":
        y1 = (slope * var) + y_intercept
        return y1
    # return height
    else:
        x1 = (var - y_intercept) / slope
        return x1


# (Partial) List of height and weight of males that are "overweight" (BMI = 3)
# Source: https://www.kaggle.com/datasets/yersever/500-person-gender-height-weight-bodymassindex
height = [149, 189, 174, 190, 161, 164, 149, 148, 194, 194, 195, 140, 192, 188, 165]
weight = [61, 104, 90, 95, 72, 75, 66, 60, 108, 106, 98, 52, 101, 100, 80]

data_count = len(height)  # number of elements in the dataset

option = input("find weight(w) or height(h)? ")
if option == "w":
    val = float(input("Enter value of height: "))
    print("The value of weight is: ")
else:
    val = float(input("Enter value of weight: "))
    print("The value of height is: ")


print(linear_regression(height, weight, option, val, data_count))

plt.scatter(weight, height)
plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.title("Weight v Height distribution of males (BMI=3)")
plt.show()
