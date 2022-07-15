CS_1 = ["Computer architecture", "Algorithm and data structures", "Mathematics for computer science",
        "Operating system", "Computer networking", "Database", "Languages and compilers", "Disturbed systems"]
Electrical_1 = ["Basic electrical engineering", "Objective electrical technology",
                "Principles of electrical engineering", "The textbook of electrical engineering",
                "Fundamentals of electrical engineering", "Electrical engineering materials",
                "Handbook of electrical engineering", "Electrical engineering fundamentals"]
Food_1 = ["Food facts and principles", "Food process and engineering technology", "Food production operations",
          "Handbook of food processing", "Objective food science", "Fundamentals of food and notations", "Food science",
          "Food safety and quality control"]
Mechanical_1 = ["A textbook of fluid mechanics and hydraulic machines", "A textbook of machine design",
                "Theory of machines", "The feynman lectures on physics", "Hand book of mechanical engineering",
                "Engineering machines", "Fundamentals of fluid mechanics", "Image of mechatronics"]
Civil_1 = ["Basic of civil engineering", "Soil mechanics and foundations", "The tower and the bridge",
           "The civil engineering handbook", "Building construction", "Essentials of bridge engineering",
           "Civil engineer's reference book", "Introduction to civil engineering system"]

Student_name_1 = []

CS_2 = ["Computer fundamentals", "Basic of computer science", "Computer fundamentals and programming in C",
        "Computer science in java", "Python programming", "Human computer interaction", "Computer science illuminated",
        "Dictionary of computer science"]
Electrical_2 = ["American electrician's handbook", "Practical electrical engineering",
                "Why study electrical engineering", "Software tools for simulation of electrical engineering",
                "Electrical machines", "Electrical transformers", "Competency in marine electrical engineering",
                 "Electrical engineering"]
Food_2 = ["Food science and engineering", "Genius foods", "Basic principles of functional food science", "Future foods",
          "Essential of food science", "Food safety", "Food science and nutrition",
          "Food science research and technology"]
Mechanical_2 = ["Textbook of mechanics", "Mechanical engineering for makers", "Elements of mechanical engineering",
                "Mechanical engineering design", "Mechanical engineering", "Basic of mechanical engineering",
                "Fundamentals of  mechanical engineering", "Introduction to mechanical engineering"]
Civil_2 = ["Material for civil and construction engineers", "Experimental vibration analysis for civil structures",
           "Bearing power of soils", "The civil engineering ", "Civil drafting technology", "Applied hydrogiology",
           "Fundamentals of sustainability in civil engineering", "Construction project scheduling and control"]

Student_name_2 = []

def Diploma_books():
    depart = input("Enter your trade(CS,Electrical,Food,Mechanical,Civil): ")
    if depart == "CS":
        book = input("Enter the book you want: ")
        for a in CS_1:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_1.append(name)
                print(Student_name_1)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            CS_1.append(book)
            print("This book is added to the list")
            print(CS_1)
            choose()

    elif depart == "Electrical":
        book = input("Enter the book you want: ")
        for a in Electrical_1:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_1.append(name)
                print(Student_name_1)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            Electrical_1.append(book)
            print("This book is added to the list")
            print(Electrical_1)
            choose()

    elif depart == "Food":
        book = input("Enter the book you want: ")
        for a in Food_1:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_1.append(name)
                print(Student_name_1)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            Food_1.append(book)
            print("This book is added to the list")
            print(Food_1)
            choose()

    elif depart == "Mechanical":
        book = input("Enter the book you want: ")
        for a in Mechanical_1:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_1.append(name)
                print(Student_name_1)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            Mechanical_1.append(book)
            print("This book is added to the list")
            print(Mechanical_1)
            choose()

    elif depart == "Civil":
        book = input("Enter the book you want: ")
        for a in Civil_1:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_1.append(name)
                print(Student_name_1)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            Civil_1.append(book)
            print("This book is added to the list")
            print(Civil_1)
            choose()

    else:
        print("Please enter the correct information")
        Diploma_books()

def Degree_books():
    depart = input("Enter the trade(CS,Electrical,Food,Mechanical,Civil): ")
    if depart == "CS":
        book = input("Enter the book you want: ")
        for a in CS_2:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_2.append(name)
                print(Student_name_2)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            CS_2.append(book)
            print("This book is added to the list")
            print(CS_2)
            choose()
            
    elif depart == "Electrical":
        book = input("Enter the book you want: ")
        for a in Electrical_2:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_2.append(name)
                print(Student_name_2)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            Electrical_2.append(book)
            print("This book is added to the list")
            print(Electrical_2)
            choose()

    elif depart == "Food":
        book = input("Enter the book you want: ")
        for a in Food_2:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_2.append(name)
                print(Student_name_2)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            Food_2.append(book)
            print("This book is added to the list")
            print(Food_2)
            choose()

    elif depart == "Mechanical":
        book = input("Enter the book you want: ")
        for a in Mechanical_2:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_2.append(name)
                print(Student_name_2)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            Mechanical_2.append(book)
            print("This book is added to the list")
            print(Mechanical_2)
            choose()

    elif depart == "Civil":
        book = input("Enter the book you want: ")
        for a in Civil_2:
            if a == book:
                print("Book is available")
                name = input("Enter your name: ")
                Student_name_2.append(name)
                print(Student_name_2)
                print("You can lend this book")
                choose()
        else:
            print("Book is not available")
            Civil_2.append(book)
            print("This book is added to the list")
            print(Civil_2)
            choose()

    else:
        print("Please enter the correct information")
        depart = input("Enter your trade(CS,Electrical,Food,Mechanical,Civil): ")


def choose():
    dep = input("Would you like to lend the books(y/n): ")

    if(dep == "y"):
        batch = input("Enter your batch(Diploma,Degree): ")
        if (batch == "Diploma"):
            print("You can get books for diploma students here:)\n")
            Diploma_books()
            
        elif (batch == "Degree"):
            print("You can get books for degree students here:)\n")
            Degree_books()
        else:
            print("Please enter the correct information")
            choose()

    elif (dep == "n"):
      print("Thanks for visiting")
      exit()


    else:
      print("Please enter correct information")
      choose()



def greetings():
    print("Thanks for visiting")
    exit()


print("Hi Student")
choose()