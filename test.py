# my_post = [
#     {"title":"title of post 1", "content": "content of post 1", "id":1},
#     {"title": "favorite foods", "content": "I like pizza", "id":2}
# ]
#
# def delete_post(Id):
#     for index, post in enumerate(my_post):
#         if post['id'] == Id:
#             del my_post[index]
#             break
#         else:
#             print(f"id: {Id} does not exist")
#             break
#     return my_post
#
# print(delete_post(5))
#
# g = "n ame"
#
# def under_score(text):
#     new_str = " "
#     for char in text:
#         if char != " ":
#             new_str += "_"
#         else:
#             new_str += " "
#     return new_str
#
# print(under_score(g))

# app/main.py
# import sys
# print("sys.path:", sys.path)
#
# from fastapi import FastAPI
# import psycopg2
#
# app = FastAPI()
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
# print("psycopg2 version:", psycopg2.__version__)

# def smallest_values(a):
#     values = [x for x in a if x > 0]
#     # values.sort()
#
#     missing_values = 1
#     while missing_values in values:
#         missing_values += 1
#     return missing_values
#
# num_list = [1,2,-1,0,-3,7,9]
# another_list = [-1, -3]
#
# print(smallest_values(another_list))


# from collections import Counter
#
#
# def solution(S):
#     # Count the occurrences of each digit
#     digit_count = Counter(S)
#
#     # Variables to store parts of the palindrome
#     left_half = []
#     middle = ""
#
#     # Find the left half and middle digit
#     for digit in sorted(digit_count.keys(), reverse=True):
#         count = digit_count[digit]
#         if count % 2 == 1:
#             # If count is odd, consider one as a middle element if there's no middle yet
#             if middle == "" or digit > middle:
#                 middle = digit
#             # Use the rest to form the left half
#             count -= 1
#         # Add half of the remaining digits to the left half
#         left_half.extend([digit] * (count // 2))
#
#     # Form the largest palindromic number
#     left_half = sorted(left_half, reverse=True)
#     palindrome = "".join(left_half) + middle + "".join(left_half[::-1])
#
#     return palindrome
#
#
# # Test the function with the given examples
# print(solution("39878"))  # Output: "898"
# print(solution("00900"))  # Output: "9"
# print(solution("0000"))  # Output: "0"
# print(solution("54321"))  # Output: "5"


from collections import Counter


# def solution(S):
#     digit_count = Counter(S)
#
#     left_half = []
#     middle = ""
#
#     for digit in sorted(digit_count.keys(), reverse=True):
#         count = digit_count[digit]
#         if count % 2 == 1:
#             if middle == "" or digit > middle:
#                 middle = digit
#             count -= 1
#         left_half.extend([digit] * (count // 2))
#
#     left_half = sorted(left_half, reverse=True)
#     palindrome = "".join(left_half) + middle + "".join(left_half[::-1])
#
#     if palindrome == "":
#         return "0"
#
#     return palindrome.lstrip("0") or "0"
#
#
# # Test the function with the given examples
# print(solution("39878"))  # Output: "898"
# print(solution("00900"))  # Output: "9"
# print(solution("0000"))  # Output: "0"
# print(solution("54321"))  # Output: "5"


from collections import Counter


def solution(S):
    # Count the occurrences of each digit
    digit_count = Counter(S)

    # Variables to store parts of the palindrome
    left_half = []
    middle = ""

    # Find the left half and middle digit
    for digit in sorted(digit_count.keys(), reverse=True):
        count = digit_count[digit]
        if count % 2 == 1:
            # If count is odd, consider one as a middle element if there's no middle yet
            if middle == "" or digit > middle:
                middle = digit
            # Use the rest to form the left half
            count -= 1
        # Add half of the remaining digits to the left half
        left_half.extend([digit] * (count // 2))

    # Form the largest palindromic number
    left_half = sorted(left_half, reverse=True)
    palindrome = "".join(left_half) + middle + "".join(left_half[::-1])

    # Remove leading zeros except for the case where the result is a single zero
    if palindrome.lstrip("0") == "":
        return "0"
    return palindrome.lstrip("0")


# Test the function with the given examples
print(solution("39878"))  # Output: "898"
print(solution("00900"))  # Output: "9"
print(solution("0000"))  # Output: "0"
print(solution("54321"))  # Output: "5"






