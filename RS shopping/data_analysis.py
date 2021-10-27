import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./data/data.csv")

data.columns = ['user_id', 'brand_id', 'action', 'month', 'day']
n_action = len(data)
n_users = data['user_id'].nunique()
n_brands = data['brand_id'].nunique()

print(f"number of action is {n_action}")
print(f"number of users is {n_users}")
print(f"number of brands is {n_brands}")

user_click_freq = data.loc[(data['action'] == 0), ['user_id', 'brand_id', 'action']].groupby(['user_id', 'brand_id']).count().reset_index()
user_click_freq.columns = ['userId', 'brand_id', 'n_click']
user_buy_freq = data.loc[(data['action'] == 1), ['user_id', 'brand_id', 'action']].groupby(['user_id', 'brand_id']).count().reset_index()
user_buy_freq.columns = ['userId', 'brand_id', 'n_buy']
user_fav_freq = data.loc[(data['action'] == 2), ['user_id', 'brand_id', 'action']].groupby(['user_id', 'brand_id']).count().reset_index()
user_fav_freq.columns = ['userId', 'brand_id', 'n_fav']
user_cart_freq = data.loc[(data['action'] == 3), ['user_id', 'brand_id', 'action']].groupby(['user_id', 'brand_id']).count().reset_index()
user_cart_freq.columns = ['userId', 'brand_id', 'n_cart']
# print(user_click_freq.head())
# print(user_buy_freq.head())
# print(user_fav_freq.head())
# print(user_cart_freq.head())

sns.set_style("darkgrid")
plt.figure(figsize=(20,15))
plt.subplot(4,1,1)
ax = sns.countplot(x="n_click", data=user_click_freq, palette="viridis")
plt.title("Distribution of number of clicks")
plt.xlim([-1, 10])
plt.subplot(4,1,2)
ax = sns.countplot(x="n_buy", data=user_buy_freq, palette="viridis")
plt.title("Distribution of number of purchases")
plt.xlim([-1, 5])
plt.subplot(4,1,3)
ax = sns.countplot(x="n_fav", data=user_fav_freq, palette="viridis")
plt.title("Distribution of number of favs")
# plt.xlim([-1, 5])
plt.subplot(4,1,4)
ax = sns.countplot(x="n_cart", data=user_cart_freq, palette="viridis")
plt.title("Distribution of number of cartings")
# plt.xlim([-1, 5])
plt.show()
