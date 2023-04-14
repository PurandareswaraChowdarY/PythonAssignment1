# Python program to count the number 5 in a given list

def list_count_4(nums):
  count = 0
  for num in nums:
    if num == 5:
      count = count + 1

  return count

print(list_count_4([1, 5, 6, 7, 4]))
print(list_count_4([1, 5, 6, 4, 5, 4, 5]))