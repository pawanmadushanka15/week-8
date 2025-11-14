def main():
    student=get_student()
    if student[0]=="padma":
        student[1]="kk"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name=input("Name: ")
    house=input("House: ")
    return {"name":name,"house":house}

if __name__=="__main__":
    main()
