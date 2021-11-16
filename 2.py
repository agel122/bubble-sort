def bubble_sort(my_data):
    try:
        criteria_to_finish = True
        while criteria_to_finish:
            for i in range(len(my_data) - 1):
                current_el = my_data[i]
                if my_data[i+1]<my_data[i]:
                    my_data[i] = my_data[i+1]
                    my_data[i+1] = current_el
                    criteria_to_finish = False
            if criteria_to_finish:
                return my_data
                break
            criteria_to_finish = True
    except TypeError:
        print('you try to sort immutable object')
    
my_list = [1, 3, 4, 2, 5, 11, 10, 0, 11, 5]
my_string = 'abcfd'
print(bubble_sort(my_list))
print(bubble_sort(my_string))



    
    
