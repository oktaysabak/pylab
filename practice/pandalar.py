import pandas as pd

#dataframe için uygun bir kütüphane

dictionary = {"name":["ali", "ahmet", "oktay"],"age":[13,14,15],"salary":[100,200,300]}

dataframe1 = pd.DataFrame(dictionary)

head = dataframe1.head(7)
tail = dataframe1.tail(2)
