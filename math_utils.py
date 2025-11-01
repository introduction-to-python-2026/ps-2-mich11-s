def find_max_number(num1, num2, num3):
 if num1 > num2 and num1 > num3:
  return num1
 if num2 > num1 and num2 > num3:
  return num2
 return num3
    
def find_mean(num1, num2, num3):
    sum = num1 + num2 + num3
 return sum / 3

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
 std_start = (mean - num1) ** 2 + (mean - num2) ** 2 + (mean - num3) ** 2
 std_mid = std_start / 3
 std = std_mid ** 0.5
 return mean, std
