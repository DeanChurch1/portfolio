

test=input("What are your test scores")
test2=input("What are your test scores")
test3=input("What are your test scores")
test4=input("What are your test scores")
test5=input("What are your test scores")
test6=input("What are your test scores")
test7=input("What are your test scores")
test8=input("What are your test scores")
test9=input("What are your test scores")
test10=input("What are your test scores")
test=float(test)
test2=float(test2)
test3=float(test3)
test4=float(test4)
test5=float(test5)
test6=float(test6)
test7=float(test7)
test8=float(test8)
test9=float(test9)
test10=float(test10)


#avgscore=float(avgscore)
avgscore=(test+test2+test3+test4+test5+test6+test7+test8+test9+test10)/10
print(avgscore)

if avgscore>=90:
    print("You have an A")
elif avgscore>=80:
    print("You have a B")
elif avgscore>=70:
    print("You have a C")
    print("get your grades up")
elif avgscore>=60:
    print("you have a D")
    print("get your grades up")
elif avgscore>=50:
    print("You have an F")
    print("get your grades up")
elif avgscore<=50:
    print("you have a F")
    print("get your grades up")
