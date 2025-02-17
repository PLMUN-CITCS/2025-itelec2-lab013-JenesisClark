numbers = list(range(1, 11)) # Create a list of numbers from 1 to 10
for num in numbers:
    if num == 3:
        continue  # Skip the rest of this iteration if num is 3
		        if num == 7:
        break  # Exit the loop completely if num is 7
		    print(num) # Print the number if it's not 3 and not 7