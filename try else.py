a=10
print(a)
try:
	a=20
	print(14/0)
	print(a)
except:
	print("In exception block")
	print(a)
	raise Exception("Exception is reised") # used to raise error and stopping program
else:
	#print(a)print(a)
	print("In else block") # executed when except is not executed
finally:
	print("In finally block") # it always execute

'''try:
	print(14/1)
except:
	print("In exception block")
finally:
	print("In finally block") # it always execute'''

