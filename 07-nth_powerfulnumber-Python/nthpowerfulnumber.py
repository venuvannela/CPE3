# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isprime(n):
	if(n==2 or n==3):
		return True
	if(n<2 or n%2==0):
		return False

	if(n>3):
		for i in range(3, n):
			if(n%i==0):
				return False
		return True

def ispowerful(n):
	n = abs(n)
	if(n==1):
		return True
	for i in range(2,n+1):	
		if(n%i==0 and isprime(i) and n%(i**2)!=0):
			return False
	else:		
		return True
			
def nthpowerfulnumber(n):
	count=1
	num=2
	if(n==0):
		return 1
	while(count<=n):
		if(ispowerful(num)):
			count=count+1
		num=num+1
	return num-1