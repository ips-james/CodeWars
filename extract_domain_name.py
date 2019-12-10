# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For
# example:
#
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

import re


def domain_name(url):
    title_search = re.search(r'(http)?(s)?(://)?(www.)?([-\w]*).([-\w]{2,3})', url, re.IGNORECASE)
    return title_search.group(5)


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("www.xakep.ru"))