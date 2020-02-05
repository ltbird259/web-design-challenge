import pandas as pd
#couldn't get the relative path to work.
data = pd.read_csv("C:/Users/lbird/Documents/bcs/Homework/11html css/web-design-challenge/web/cities.csv")

print(data.head(5))

html = data.to_html()

file=open("htmltxt.txt","w")

file.write(html)