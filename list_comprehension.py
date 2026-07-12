#  PYTHON LIST COMPREHENSION

#  normalize the domains into standard format
domains = ["www.google.com", 
           "openai.com",
           "localhost",
           "WWW.DATAWITHBARAA.COM"]

cleaned = [
    d.lower().replace("www.", "")
    for d in domains
    if "." in d
]
print(cleaned)

#  Note: in comprehensions, filtering data is optional
#  only filtering: using only the variable name means no transformation



