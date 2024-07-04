import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

data2 = pd.DataFrame({'human':data["whoAmI"] == "human", 'robot':data["whoAmI"] == "robot"})

#print(pd.get_dummies(data))

print(data2)
