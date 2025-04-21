# %%

import pandas as pd
from matplotlib import pyplot as plt

# %%

data_desktop = pd.read_csv("desktop_prices.txt", header=None)
data_desktop = data_desktop[data_desktop < 400]
data_desktop = data_desktop.dropna()
# %%
data_phone = pd.read_csv("phone_prices.txt", header=None)

#%%
data_desktop
#%%
data_desktop = data_desktop.sort_values(by=0)
data_desktop
#%%
data_desktop.index
#%%
data_desktop.index = list(range(len(data_desktop)))
# %%
data_phone = data_phone.sort_values(by=0)
data_phone.index = list(range(len(data_phone)))
# %%
plt.figure(figsize=(8, 6))  # Optional: Adjust figure size


plt.plot(data_desktop, linestyle="--", label="desktop")

plt.plot(data_phone, linestyle="-", label="phone")
plt.legend()

plt.savefig("line_plot.png")
plt.show()
# %%
data_desktop.describe()
# %%

data_phone.describe()
# %%


plt.figure(figsize=(3, 6))


plt.boxplot(
    [data_desktop.iloc[:, 0], data_phone.iloc[:, 0]],
    tick_labels=["desktop", "phone"],
    widths=[0.7, 0.7],
)
plt.savefig("box_plot.png")

# %%
data_desktop.mean()


# %%
data_phone.mean()
# %%
data_phone.mean() - data_desktop.mean()
# %%
higher = (data_phone.mean() - data_desktop.mean()) / data_desktop.mean()
# float(higher)
# %%
print(f"phone prices are higher than desktop for {higher.iloc[0] * 100:.0f}% percent.")
# %%
