if __name__ == '__main__':
    std = []
    for _ in range(int(input("Total Students : "))):
        name = input("Enter Student Name : ")
        score = float(input("Enter Score of Student : "))
        std.append([name,score])
    student = sorted(list(set([x[1] for x in std])))
    print(student)
    low = student[1]
    lowlist = []
    for i in std:
        if i[1]==low:
            lowlist.append(i[0])
    lowlist = sorted(lowlist)
    print(lowlist)
