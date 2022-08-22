# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 12, 2021
# Programming Assignment #19

followers = int(input("Enter amount of social media followers: "))

if followers < 0:
    tier = "Error"
elif followers < 1000:
    tier = "Hyper Influencer"
elif 1000 < followers < 10000:
    tier = "Nano Influencer"
elif 10000 < followers < 100000:
    tier = "Micro Influencer"
elif 100000 < followers < 500000:
    tier = "Mid-Tier Influencer"
elif 500000 < followers < 1000000:
    tier = "Macro-Influencer"
else:
    tier = "Celebrity Influencer"

print("Your influencer tier is:", tier)