if __name__ == '__main__':
    student_list =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]  
        student_list.append( student ) 
    number_list = sorted(list(set(map(lambda x : x[1], student_list))))   
    # print (number_list)
    second_lowest = number_list[1]
    second_lowest_ppl = []
    for student in student_list:
        if student[1] == second_lowest:
            second_lowest_ppl.append(student[0])

    sorted_list = sorted(second_lowest_ppl)     
    print('\n'.join(sorted_list))  
