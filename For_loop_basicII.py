#1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
arr = [-1, 34,  -3, 37, 16, -25, -5, 87]
def newArr(arr):
    for i in range(0, len(arr), 1):
        if (arr[i] > 0):
            arr[i] = "big"
    return arr
print(newArr(arr))


#2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
arr = [1, 6, -4, -2, -7, -2]
def countPos(arr):
    arr[-1] = abs(arr[-1])
    arr.append(arr[-1])
    arr.pop()
    return(arr)
print(countPos(arr))

#3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list. Example: sum_total([1,2,3,4]) should return 10 Example: sum_total([6,3,-2]) should return 7
arr = [11,-2,34,48, 37, -21]
def arrSum(arr):
    sum = 0
    for i in range (0, len(arr)):
        sum = sum + arr[i]
    return sum
print(arrSum(arr))

#4. Average - Create a function that takes a list and returns the average of all the values.x Example: average([1,2,3,4]) should return 2.5
arr = [10, 54, 37, 21, 28, 2]
def arrAvg(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    return sum/len(arr)
print(arrAvg(arr))

#5. Length - Create a function that takes a list and returns the length of the list. Example: length([37,2,1,-9]) should return 4 Example: length([]) should return 0
arr = ["Danielle", 34, "Christopher",  37, 2010, 11]
def lenList(arr):
    index = 0
    for i in range (0, len(arr)):
        index = i
        # print(i)
        # print(index)
    return index + 1
print(lenList(arr))

arr = [37, 2, 1, -9]
def lenList(arr):
    index = 0
    for i in range (0, len(arr)):
        index = index + i
    return index-2
print(lenList(arr))

#6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False. Example: minimum([37,2,1,-9]) should return -9 Example: minimum([]) should return False

arr = [37, 2, 1, -9]
arr2 = []
def minValue(arr):
    for i in range (0, len(arr)):
        if (arr[i] < 0):
            print(arr[i])
    x = noMinValue(arr)
    print(x)
def noMinValue(arr):
    for i in range (0, len(arr)):
        if (len(arr2) == 0):
            return False
print(minValue(arr))

#7. Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False. Example: maximum([37,2,1,-9]) should return 37 Example: maximum([]) should return False
arr = [37, 2, 1, -9]
arr2 = []
def maxValue(arr):
    max = 0
    tempNum = 0
    for i in range (0, len(arr)):
        if (arr[i] > 0):
            tempNum = arr[i]
        if (tempNum > max):
            max = tempNum
            print(max)
    x = noMaxValue(arr)
    print(x)
def noMaxValue(arr):
    for i in range (0, len(arr)):
        if (len(arr2) == 0):
            return False
print(maxValue(arr))


#8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list. Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
arr = [37, 2, 1, -9, -12]
def ultimateArr(arr):
    sum = 0
    avg = 0
    maximum = 0
    length = 0 
    for i in range (0, len(arr)):
        if(arr[i] > 0):
            if (maximum < arr[i]):
                maximum = arr[i]
            sum = sum + arr[i]
            avg = avg + arr[i]
            arr[i] < 0
            length = length + i
    return (f"Sum : {sum}, Average : {avg/len(arr)}, Minmum : {arr[i]}, Maximum : {maximum}, Length : {length + 2}")
print(ultimateArr(arr))

#9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.) Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
arr_list = [37, 2, 1, -9, -12, 5, 34, 37]
def reverseList(arr_list):
    print(list(reversed(arr_list)))
print(reverseList(arr_list))