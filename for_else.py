successful = False
for i in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    # else is executed if 'for' loop is not broken by a break
    print("Failed 3 times")
