def is_digit_power(num, power):
    digits = list(str(num))
    X = 0
    for digit in digits:
        X += int(digit)**power
    if num == X:
        return True
    return False

trues = []
for i in range(2, 1000000):
    if is_digit_power(i, 5):
        trues.append(i)

print(sum(trues))
