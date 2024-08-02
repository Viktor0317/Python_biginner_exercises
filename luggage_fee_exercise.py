# You are going to travel to a different country, but you have some heavy luggage to transport.
# There are different fees associated with different weights of luggage.
# If the weight is over 70 pounds, then there is a 100 dollar fee. If the weight is between 50 to 70 pounds
# (including exactly 50 and 70 pounds) the fee is 50 dollars, otherwise the fee is 0 dollars.
# Create an if, elif, else statement to calculate and store the fee into a variable called fee.
# Make sure not to use multiple if statements.

weight = 75

# Write your if statement here:
if weight >= 50 and weight <= 70:
  fee = 50
elif weight > 70:
  fee = 100
else:
  fee = 0

print("The bag's weight is: " + str(weight) + " lbs.")
print("The fee for the bag is: $" + str(fee))
