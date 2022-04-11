import pandas as pd

icecream = ["kaas","kaass","chocola","kaaschocola"]
icecream_s = pd.Series(icecream)
# print(pd.Series(icecream))

webster = {"aarvark":"an animal",
           "banana":"a delicious fruit"}
# print(pd.Series(webster))

# print(icecream_s.values)
# print(icecream_s.index)
# print(icecream_s.dtype)

prices = [2.99, 4.45, 1.36]
pricesS = pd.Series(prices)
# print(pricesS.sum())
# print(pricesS.product())
# print(pricesS.mean())

df = pd.read_csv("D:/CodingProjects/LoN/2012-2016_merged_output_groups_sonochiro.csv", usecols=['rank'], squeeze=True)
print(df)