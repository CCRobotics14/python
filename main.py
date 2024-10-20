# Initialize the sum variable
total_sum = 0

# Loop through numbers from 1 to 999
for i in range(1, 1000):
    # Check if the number is a multiple of three
    if i % 3 == 0:
        total_sum += i

# Print the result
print("The sum of all multiples of three up to 1000 is:", total_sum)
