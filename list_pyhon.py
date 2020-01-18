if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output_List = []
    for x in range(x+1):
      for y in range (y+1):
       for z in range (z+1):
        if (x + y + z != n):
         a=[]   
         a.append(x)
         a.append(y)
         a.append(z)
        #  print(a)
         output_List.append(a)
    print(output_List)       
"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, ""