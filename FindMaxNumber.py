"""
1. Write code to iterate through the list and find the largest number. Remember to use the indexing we talked about - numbers[i]
2. RETURN the maximum number. Make sure to write the "return"
"""


def main(high):
    numbers = [23, 12, 56, 78, 34, 67]
    high = numbers[0]
    for i in range (0,(len(numbers)-1)):
        if high > numbers[i]:
            high = high
        elif high < numbers[i]:
            high = numbers [i]
        
        return high

print(high)
if __name__ == '__main__':
    main()
