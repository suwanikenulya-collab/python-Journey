#python credit card validator program
#1. remove any - or ''
# add all digits in the odd places from right to left
#double every second digit from right to left
#    (if result is a two-digit number, add the to-digit number together to get a single digit)
#sum the totals of steps 2 and 3
#if sum is divided by 10 its valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

#step 1
card_number= input("Enter a credit card number: ")
card_number = card_number.replace("-", "")
card_number= card_number.replace(" ", "")
card_number= card_number[::-1]

#step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)

#step 3
for x in card_number[1::2]:
    x=int(x)*2
    if x>=10:
        sum_even_digits+= (1+ (x%10))
    else:
        sum_even_digits+= x

total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print("valid")
else:
    print("invalid")


