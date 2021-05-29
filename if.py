sentence="Mayo College, Ajmer"
search=input("enter the sentence you want to search: ").lower()
if search in sentence.lower():
    print(f"{search} found")
else:
    print("search word not present")   