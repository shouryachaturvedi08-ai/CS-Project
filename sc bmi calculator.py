from minecolor import RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BLACK, BOLD, UNDERLINE, RESET


def calculator_bmi(weight, height_cm = None, height_inch = None, unit = 'kg'):


    if unit == 'lb':
        weight = weight*0.453592
    elif unit != 'kg':
        raise ValueError("WEIGHT MUST BE IN kg or lb")


    if height_cm is not None:
        height_m = height_cm / 100
    elif height_inch is not None:
        height_m = height_inch * 0.0254
    else:
        raise ValueError("HEIGHT MUST BE DEFINED")


    bmi = weight / (height_m ** 2)

    return bmi



def category_bmi(bmi , gender):



    categories = {
        'UNDERWEIGHT': { "men" : ("Weak immunity, muscles loss, fatigue" ,
                                  "High protein diet, regular meals, exercise for strength") ,
                         "women" : ("Hormonal Imbalance, Osteoporosis, Abnormal cycles" ,
                                    "Nutrient rich meals, Calcium intake, regular medical checkups") } ,

        'HEALTHY WEIGHT' : { "men" : ("Strong Metabolism, Good Stamina and Physically Fit, Risk of disease is low" ,
                                      "Maintain Balanced diet, Regular Exercise, Keep Hydrated Yourself") ,
                             "women" : ("Healthy Hormones, Strong bones, Good Fertility" ,
                                        "Maintain Balanced Diet, Yoga, Physical Exercise")  } ,
        
        'OVERWEIGHT' : { "men" : ("Heart Strain, Risk of Diabetes and BP, Sleep Issues" ,
                                  "Cardiovascular activities, Reduce sugar and oily food, Anger Control") ,
                         "women" : ("Fatigue, Hormonal Imbalance, pregnancy Complications" ,
                                    "Balanced Diet, Behavioural habits, Regular Exercise")  } ,
        
        'OBESE CATEGORY I' : { "men" : ("High blood Pressure, Type 2 Diabetes, Unhealthy Cholestrol" ,
                                          "Dietary Changes, Physical Activity, Medical Consultation") ,
                                 "women" : ("Insulin Resistance, Fertility Challenges, Joint Strain" ,
                                            "Pharmacotherapy, Physical Activity, Bariatric Surgery") } ,

        'OBESE CATEGORY II' : { "men" : ("Cardiovascular Diseases, Liver and Kidney Disease, Increased Cancer Risk" ,
                                          "Weight Loss Medication, Bariatric Surgery, Dietary Changes") ,
                                 "women" : ("Heart Disease, Liver and Gall Bladder Disease, Pregnancy Risks" ,
                                            "Weight - Loss Medication, Bariatric Surgery, Therapy") }
        }




    if bmi < 18.5:
        category = 'UNDERWEIGHT'
        color = BLUE
    elif bmi >= 18.5 and bmi < 25:
        category = 'HEALTHY WEIGHT'
        color = GREEN
    elif bmi >= 25 and bmi < 30:
        category = 'OVERWEIGHT'
        color = YELLOW
    elif bmi >= 30 and bmi < 35:
        category = 'OBESE CATEGORY I'
        color = MAGENTA
    else:
        category = 'OBESE CATEGORY II'
        color = RED



    return category, categories[category][gender], color




def table(record):


    i= ["NAME", "AGE", "GENDER", "BMI", "CATEGORY", "CONSEQUENCES", "CURE"]


    print(CYAN + "\n*************** BMI TABLE ******************" + RESET)


    for h in i:
        print(f"{h:<15}" , end = "")
        
    print()
    print("-" * 120)



    for n in record:

        if n["bmi"] < 18.5:
            color = BLUE
        elif n["bmi"] >= 18.5 and n["bmi"] < 25:
            color = GREEN
        elif n["bmi"] >= 25 and n["bmi"] < 30:
            color = YELLOW
        elif n["bmi"] >= 30 and n["bmi"] < 35:
            color = MAGENTA
        else:
            color = RED


        for h in i:
            value = n[h.lower()]
            if h == "BMI":
                print(f"{color}{value:<15.2f}{RESET}" , end = "")
            elif h == "CATEGORY":
                print(f"{color}{value:<15}{RESET}" , end = "")
            else:
                print(f"{value:<15}" , end = "")
        print()




def bmi():

    print(CYAN + "************** BMI CALCULATOR *****************" + RESET)
    record = []


    while True:

        name = input("ENTER YOUR NAME")
        age = int(input("ENTER YOUR AGE"))
        gender = input("ENTER YOUR GENDER (men/women) ").lower()
        if gender not in ('men' , 'women'):
            print(RED + "INVALID" + RESET)
            return




        print("CHOOSE WEIGHT UNIT")
        print("1- KILOGRAMS")
        print("2- POUNDS")
        weight_choice = int(input("ENTER YOUR CHOICE (1 or 2): "))
        weight = float(input("ENTER YOUR WEIGHT"))
        if weight_choice == 1:
            unit = 'kg'
        else:
            unit = 'lb'




        print("CHOOSE HEIGHT UNIT")
        print("1- CENTIMETERS")
        print("2- INCHES")
        choice = int(input(" ENTER YOUR CHOICE (1 or 2) "))



        if choice == 1:
            height_cm = float(input("ENTER YOUR HEIGHT IN CENTIMETERS"))
            bmi = calculator_bmi(weight, height_cm= height_cm, unit=unit)
        elif choice == 2:
            height_inch = float(input("ENTER YOUR HEIGHT IN INCHES"))
            bmi = calculator_bmi(weight, height_inch = height_inch, unit=unit)
        else:
            print(RED + "ERROR" + RESET)
            return



        category, (consequences, cure), color = category_bmi(bmi, gender)





        print("\n" + CYAN + "************* RESULT ***************" + RESET)
        print(f"NAME: {name}")
        print(f"AGE: {age}")
        print(f"GENDER: {gender}")
        print(f" YOUR BMI IS: {color}{bmi:.2f}{RESET} ")
        print(f" CATEGORY: {color}{category}{RESET} ")
        print(f" CONSEQUENCES: {color}{consequences}{RESET} ")
        print(f" CURE: {color}{cure}{RESET} ")



        record.append({ 'name': name,
                        'age': age,
                        'gender': gender.capitalize(),
                        'bmi': bmi,
                        'category': category,
                        'consequences': consequences,
                        'cure': cure  })




        a = input("\n WANT TO ADD ANOTHER PERSON ? (YES/NO) ")
        if a!= "YES":
            break


    table(record)



if __name__== "__main__":
    bmi()

