word=input("Enter a word \n")
lowercase=word.lower()
vowel_dic={}
for i in "aeiou":
    count=lowercase.count(i)
    vowel_dic[i]=count
for i ,j in vowel_dic.items():
    print(f"{i} : {j}")    