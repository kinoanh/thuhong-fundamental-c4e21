height(m) = input("What is your height(m)? ")
weight(kg) = input("what is your weight(kg)? ")
height(cm) = height(m)*100
IMB = weight / height(cm)**2
if IMB < 16:
    print("Severely underweiht")
elif 16 <= IMB < 18.5:
    print("Underweight")
elif 18.5 <= IMB < 25:
    print("Normal")
elif 25 <= IMB < 30:
    print("Overweight")
else:
    print("Obese")