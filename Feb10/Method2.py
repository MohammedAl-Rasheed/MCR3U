print("Hello this program basically detects what is a better plan for you between the two list below")
print("Unlimited: 45$, unlimited GB")
print("By the Gig: 14$ per GB")
print("input your average GigaBytes per month")
n = float(input())
if n > 45/14:
    print("Unlimited plan is better in your case")
if n < 45/14:
    print("By the Gig plan is better in your case")