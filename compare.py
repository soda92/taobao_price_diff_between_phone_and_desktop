# %%

import pandas as pd
from matplotlib import pyplot as plt

# %%

data_desktop = pd.read_csv("desktop_prices.txt", header=None)
# %%
data_phone = pd.read_csv("phone_prices.txt", header=None)

# %%
plt.figure(figsize=(8, 6))  # Optional: Adjust figure size


plt.plot(data_desktop, label="desktop")

plt.plot(data_phone, label="phone")

plt.show()
plt.savefig("line_plot.png")
# %%

plt.plot(data_desktop)
# %%

plt.plot(data_phone)
# %%


data_desktop.describe()
# %%

data_phone.describe()
# %%


plt.figure(figsize=(8, 6))


plt.boxplot([data_desktop.iloc[:,0], data_phone.iloc[:,0]], labels=['desktop', 'phone'])
plt.savefig("box_plot.png")

# %%
data_desktop.mean()


# %%
data_phone.mean()
# %%
data_phone.mean() - data_desktop.mean()
# %%
higher = (data_phone.mean() - data_desktop.mean())/data_desktop.mean()
# float(higher)
# %%
print(f"phone prices are higher than desktop for {higher.iloc[0]*100:.0f}% percent.")
# %%
