def length():
    def mtokm():
        m=float(input("Enter the distance in meter:"))
        km=m/1000
        print("The distance of",m,"meter in Kilometer is:",km,"km")
    def mtoin():
        m=float(input("Enter the distance in meter:"))
        inc=m*39.3700787
        print("The distance of",m,"meter in Inches is:",inc,"inhes")
    def mtof():
        m=float(input("Enter the distance in meter:"))
        feet=m*3.2808399
        print("the distance of",m,"meter in Feet is:",feet,"feet")
    def mtocm():
        m=float(input("Enter the distance in meter:"))
        cm=m*100
        print("The distance of",m,"meter in Centimeter is:",cm,"cm")
    def kmtom():
        km=float(input("Enter the distance in kilometer:"))
        m=km*1000
        print("The distance of",km,"kilometer in meter is:",m,"m")
    def kmtoin():
        km=float(input("Enter the distance in kilometer:"))
        inc=km*39370.0787
        print("The distance of",km,"kilometer in Inches is:",inc,"inches")
    def kmtof():
        km = float(input("Enter the distance in kilometer:"))
        feet=km*3280.8399
        print("The distance of",km,"kilometer in Feet is:",feet,"feet")
    def kmtocm():
        km = float(input("Enter the distance in kilometer:"))
        cm=km*100000
        print("The distance of",km,"kilometer in Centimeter is:",cm,"cm")
    def ftom():
        f=float(input("Enter the distance in feet:"))
        m=f/3.2808399
        print("The distance of",f,"feet in Meter is:",m,"m")
    def ftoin():
        f = float(input("Enter the distance in feet:"))
        inc=f*12
        print("The distance of",f,"feet in Inches is:",inc,"inches")
    def ftocm():
        f = float(input("Enter the distance in feet:"))
        cm=f*30.48
        print("The distance of",f,"feet in Centimeter is:",cm,"cm")
    def intof():
        inc=float(input("Enter the distance in inches:"))
        f=inc*0.0833
        print("The distance of",inc,"inches in Feet is:",inc,"inches")
    def intocm():
        inc = float(input("Enter the distance in inches:"))
        cm=inc*2.54
        print("The distance of",inc,"inches in Centimeter is:",cm,"cm")
    def intom():
        inc = float(input("Enter the distance in inches:"))
        m=inc*0.0254
        print("The distance of",inc,"inches in Meter is:",inc,"inches")
    def cmtom():
        cm=float(input("Enter the distance in centimeter:"))
        m=cm/100
        print("The distance of",cm,"centimeter in Metr is:",m,"m")
    def cmtoin():
        cm = float(input("Enter the distance in centimeter:"))
        inc=cm/2.54
        print("The distance of",cm,"centimeter in Inches is:",inc,"inches")
    def cmtof():
        cm = float(input("Enter the distance in centimeter:"))
        f=cm/30.48
        print("The distance of",cm,"centimeter in Feet is:",f,"feet")
    print("Choose from one of the options to find the distance:")
    print("1.Meter")
    print("2.Km")
    print("3.Feet")
    print("4.Inches")
    print("5.Cm")
    print("6.Exit")
    choice = input("Enter your choice:")

    if choice == 'meter' or choice == '1' or choice == 'Meter':
        print("Choose from one of the following options to convert Meter into:")
        print("1.Meter to Km")
        print("2.Meter to Inches")
        print("3.Meter to Feet")
        print("4.Meter to Cm")
        choice1=int(input("Enter your choice:"))
        if choice1>=5:
            print("Invalid input!!!")
        if choice1==1:
            mtokm()
        elif choice1==2:
            mtoin()
        elif choice1==3:
            mtof()
        elif choice1==4:
            mtocm()
        length()
    elif choice == 'km' or choice == '2' or choice == 'Km':
        print("Choose from one of the following options to convert Kilometer into:")
        print("1.Km to Meter")
        print("2.Km to Inches")
        print("3.Km to Feet")
        print("4.Km to Cm")
        choice2=int(input("Enter your choice:"))
        if choice2>=5:
            print("Invalid input!!!")
        if choice2==1:
            kmtom()
        elif choice2==2:
            kmtoin()
        elif choice2==3:
            kmtof()
        elif choice==4:
            kmtocm()
        length()
    elif choice == 'feet' or choice == '3' or choice == 'Feet':
        print("Choose from one of the following options to convert Feet into:")
        print("1.Feet to Meter")
        print("2.Feet to Inches.")
        print("3.Feet to Cm")
        choice3=int(input("Enter your choice:"))
        if choice3>=4:
            print("Invalid input!!!")
        if choice3==1:
            ftom()
        elif choice3==2:
            ftoin()
        elif choice3==3:
            ftocm()
        length()
    elif choice == 'inches' or choice == '4' or choice == 'Inches':
        print("Choose from one of the following options to convert Inches into:")
        print("1.Inches to Feet")
        print("2.Inches to Cm")
        print("3.Inches to Meter")
        choice4=int(input("Enter your choice:"))
        if choice4>=4:
            print("Invalid input!!!")
        if choice4==1:
            intof()
        elif choice4==2:
            intocm()
        elif choice4==3:
            intom()
        length()
    elif choice == 'cm' or choice == '5' or choice == 'Cm':
        print("Choose from one of the following options to convert Centimeter into:")
        print("1.Cm to Meter")
        print("2.Cm to Inches")
        print("3.Cm to Feet")
        choice5=int(input("Enter your choice:"))
        if choice5>=4:
            print("Invalid input!!!")
        if choice5==1:
            cmtom()
        elif choice5==2:
            cmtoin()
        elif choice5==3:
            cmtof()
        length()
    elif choice=='6':
        print("Exiting!!!!")
        exit()
    if choice>'6':
        print("Invalid input!!!")
        print("Do you want to try again??")
        y = str(input("Type 'yes' or 'no':"))
        if y=='yes' or y=='Yes' or y=='Y' or y=='y':
            length()
        elif y=='no' or 'No':
            print("Exitingg!!")
            exit()
        else:
            exit()
length()




