# Question 2 :
#
# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
#
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
#
# Expected Output Example:
#
# Attempt 1: Response 500
#
# Attempt 2: Response 200
#
# ✅ Test Passed


attempt = 1
max_attempt = 3
response = None

while attempt <= max_attempt:
    response = int(input("Enter the Response"))
    if response == 200:
        print("✅ Test Passed")
        break
    else:
        attempt = attempt + 1

if response != 200:
    print("❌ Test Failed after 3 attempts.")