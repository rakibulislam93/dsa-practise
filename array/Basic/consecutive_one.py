
# prices = [1, 1, 0, 1, 1, 1]
prices = [1, 0, 1, 1, 0, 1]
mx = 0
count = 0
for i in range(len(prices)):
    
    if prices[i] == 1:
        count +=1
        mx = max(mx,count) 
    else:
        count = 0

print(mx)