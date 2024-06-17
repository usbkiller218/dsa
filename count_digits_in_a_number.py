#first method
def count_digits_in_numbers(number):
    temp=str(number)
    return len(temp)
import math

number=12345
count=count_digits_in_numbers(number)
print(count)
#second method
def countDigits(n):
    cnt = int(math.log10(n) + 1)
    return cnt

# Main function
if __name__ == "__main__":
    N = 12345
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)
    