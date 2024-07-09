urdu_marks = int(input("enter urdu marks out of 100: "))
english_marks = int(input("enter english marks out of 100: "))
math_marks = int(input("enter math marks out of 100: "))
islamiat_marks = int(input("enter islamiat marks out of 100: "))
science_marks = int(input("enter science marks out of 100: "))

total_marks = 500
obtain_marks = urdu_marks + english_marks + math_marks + islamiat_marks + science_marks

percentage = obtain_marks/total_marks*100

if(percentage>=80):
    print("A+ grade")
elif(percentage>=70):
    print("A grade")
elif(percentage>=60):
    print("B grade")
elif(percentage>=50):
    print("C grade")
elif(percentage>=40):
    print("D grade")
elif(percentage>=33):
    print("failed")