answer = input("What do you think about 4Chan?")
if len(answer) > 200:
    print("wow, you had a lot to talk about")
elif len(answer) > 125:
    print("I didn't know you thought about it that much")
elif len(answer) > 50:
    print("I guess that's about right")
elif len(answer) > 1:
    print("fairly laconic")
else:
    print("don't want to talk huh?")