'''
    This file contains the template for Assignment1.  For testing it, I will place it
    in a different directory, call the function <minimum_allowable_attendance>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

def binary_search(low_bound, high_bound, num_days, groups_arr, past_avg, output_file):
    days_arr = [0]*int(num_days)

    average = int((low_bound+high_bound)/2) + (int(low_bound+high_bound)%2>0)
    count = 0


    #base Case: checks if the average is the same as the past average which means its down to the last two number
    #we know it rounds up so we have to test the average-1 and if that one works then that is the lowest working number, if it does not then the past average is the lowest working number
    if(average == past_avg):
        average = average-1
        for i in range(0, int(num_days)):

            #for j in range(i, len(groups_arr)):
            while(days_arr[i] <= average and count < len(groups_arr)):
 
                if(days_arr[i]+groups_arr[count] <= average):
                    days_arr[i] = days_arr[i]+groups_arr[count]
                    count = count +1
                else:
                    break
        if(count != len(groups_arr)):
            output_file.write(str(past_avg))
            return
        else:
            output_file.write(str(average))
            return
            

    count = 0

    

    
    #fill test days array to see if the average is too high or too low

    for i in range(0, int(num_days)):

        #for j in range(i, len(groups_arr)):
        while(days_arr[i] <= average and count < len(groups_arr)):
 
            if(days_arr[i]+groups_arr[count] <= average):
                days_arr[i] = days_arr[i]+groups_arr[count]
                count = count +1
            else:
                break
            

    #check to see if average is too high or too low. If count != # of groups then it is too small. run recursion with new updated half
    if(count != len(groups_arr)):
        binary_search(average+1, high_bound, num_days, groups_arr, average, output_file)
    else:
        binary_search(low_bound, average, num_days, groups_arr, average, output_file)




def minimum_allowable_attendance(input_file_path, output_file_path):
    '''
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    '''
    #open files into varablies to be read and manipulated
    input_file = open(input_file_path, "r")
    output_file = open(output_file_path, "r+")
    output_file.truncate(0)

    #setup variables
    num_days = []
    groups_arr = []
    i = 0

    for line in input_file:
        if i == 0:
            num_days = line
            i = i+1

        if i != 0:
            groups_arr = line.split(",")
    groups_arr = [int(i) for i in groups_arr]
    
    num_visiters = sum(groups_arr)
    low_bound = max(groups_arr)

        

    
    binary_search(low_bound,num_visiters,num_days,groups_arr, 0, output_file)

    #close files
    input_file.close()
    output_file.close()

'''
    To test your function, you can uncomment the following command with the the input/output
    files paths that you want to read from/write to.
'''
minimum_allowable_attendance('input1.txt', 'output.txt')




