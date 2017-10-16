grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_sum(scores):
    total = 0
    for i in scores:
        total += i
    return total


print ("total:",(grades_sum(grades)))


def grades_average(grades_input):
    x = float(len(grades_input))
    average = grades_sum(grades_input) / x
    return average


print ("average:",(grades_average(grades)))

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for i in scores:
    variance += (average - i) ** 2
  v = variance / len(scores)
  return v

print ("variance:",(grades_variance(grades)))

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print ("Standard Deviation:" , grades_std_deviation(variance))
