nums = [1, 2, 3, 5, 6]
expected_sum = 0
for i in range(nums[0], nums[-1] + 1):
    expected_sum = expected_sum + i
actual_sum = 0
for n in nums:
    actual_sum = actual_sum + n
missing = expected_sum - actual_sum

print("Missing number =", missing)
