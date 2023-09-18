#
arr = [1, 2, 3, 4, 5]
max = arr[0]
min = arr[0]
for number in arr:
    if number > max:
        max = number
    elif number < min:
        min = number
print("Maximum:", max)
print("Minimum:", min)