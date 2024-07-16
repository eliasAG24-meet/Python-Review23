import random
temps = []
avg = []
for i in range(7):
	temps.append(random.randint(26, 40))
DOTW = ['sunday', 'monday', 'tuesday', 'wednsday', 'thursday', 'friday', 'saturday']
for i in range(7):
	print(DOTW[i], ":", temps[i])
good_days = 0
for i in range(7):
	if temps[i] % 2 == 0 :
		good_days = good_days + 1
print ("good days :", good_days)

HT = max(temps)
HTD = 40
LT = min(temps)
LTD = 26
print ("lowest temp :", LT)
print ("lowest temp of day", LTD)
for i in range(7):
	avg = sum(temps) / 7
print("the avg temp is:", avg)
