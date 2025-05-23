# def is_even(num):
#     res=num%2
#     if res!=0:
#         return False
#     return True

# num= int(input("Enter any Number to check is Even or Not: "))
# print(is_even(num))

# def is_even(num):
#     return num%2==0

# print(is_even(143))


# # Slug String with default Arguments

def do_sug(url,sep="-"):
    return url.strip().replace(" ", sep).lower()

print(do_sug("    I am lakhan what is this    ","*"))

# def count_vowels(pharse):
#     count=0
#     for index in pharse:
#         if index in "aeiou":
#             count+=1
#     return count

# print(count_vowels("Lakhan alsjdkhsaiiufckvvkdgwiefgweuigt3uyhdvVCJGWEUIOF"))