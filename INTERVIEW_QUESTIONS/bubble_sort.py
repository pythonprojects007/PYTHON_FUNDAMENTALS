def bubble_sort(input_list):
    for x in range(len(input_list)):
      print(x)
      for  y in range(0,len(input_list)-1-x):
         print(len(input_list),y)
         if input_list[y]>input_list[y+1]:
            temp=input_list[y]
            input_list[y]=input_list[y+1]
            input_list[y+1]=temp
    print(input_list)

input_list=[6,7,3,1,34,5,45,2,7]

bubble_sort(input_list)