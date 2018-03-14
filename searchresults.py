from googlesearch import *
new_file = open("search_results.txt","w+")
query = input("Search something!\n")
for i in search(query, tld='com', lang='en', num=5, stop=1, pause=2):
    print(i)
    new_file.write(i)
new_file.close()
