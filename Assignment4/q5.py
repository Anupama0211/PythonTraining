"""
We have a list of mobile numbers. We need to sort those numbers in ascending order
and then we need to print them in the standard format of (+91 xxxx xxx xxx). Create
a function which performs sorting on mobile numbers and create a decorator which
will convert these mobiles into standard format.

Sample Input: - [07895460981, 9711231230, 919711540230]
Sample Output: - [+91 7895 460 981, +91 9711 231 230, +91 9711 540 230]

"""


def decorate_mobile_numbers(func):
    def standardize_mobile_numbers(mobile_numbers):
        for i in range(len(mobile_numbers)):
            if (len(mobile_numbers[i]) == 12):
                mobile_numbers[i] = mobile_numbers[i][2:12]
            elif (len(mobile_numbers[i]) == 11):
                mobile_numbers[i] = mobile_numbers[i][1:11]
            mobile_numbers[i] = "+91 " \
                                + " " + mobile_numbers[i][0:4] \
                                + " " + mobile_numbers[i][4:7] \
                                + " " + mobile_numbers[i][7:10]

        return func(mobile_numbers)

    return standardize_mobile_numbers


@decorate_mobile_numbers
def sort_mobile_numbers(mobile_numbers):
    return sorted(mobile_numbers)


print(sort_mobile_numbers(["07895460981", "9711231230", "919711540230"]))
