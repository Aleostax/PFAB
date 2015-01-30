a = input("type your Test 1 score:\t")
b = input("Test 2 score:\t")
c = input("Test 3 score:\t")
d = input("Test 4 score:\t")

def average(a,b,c,d):
	return ((a+b+c+d)/4)
	

gradeNum = average(a,b,c,d)
if gradeNum >= 90:
	print gradeNum,"You got an A"
elif gradeNum >= 80:
	print gradeNum,"You got a B"
elif gradeNum >= 70:
	print gradeNum,"You passed"
else:
	print gradeNum, "You failed, see you in Summer School."
