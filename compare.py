# %%

import pandas as pd
from matplotlib import pyplot as plt

# %%

data_desktop = pd.read_csv("desktop_prices.txt", header=None)
data_desktop = data_desktop[data_desktop < 400]
data_desktop = data_desktop.dropna()
# %%
data_phone = pd.read_csv("phone_prices.txt", header=None)

# %%
data_desktop
# %%
data_desktop = data_desktop.sort_values(by=0)
data_desktop
# %%
data_desktop.index
# %%
data_desktop.index = list(range(len(data_desktop)))
# %%
index2 = [len(data_desktop) / len(data_phone) * i for i in range(len(data_phone))]
# %%
data_phone = data_phone.sort_values(by=0)
data_phone.index = index2
# %%
plt.figure(figsize=(8, 6))  # Optional: Adjust figure size

plt.plot(data_phone, label="phone")

plt.plot(data_desktop, label="desktop")

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
    [data_phone.iloc[:, 0], data_desktop.iloc[:, 0]],
    tick_labels=["phone", "desktop"],
    widths=[0.7, 0.7],
)
plt.savefig("box_plot.png")

# %%
data_desktop.median()
# %%
data_phone.median()
# %%
higher = (data_phone.median() - data_desktop.median()) / data_desktop.median()
percent = f"{higher.iloc[0] * 100:.0f}%"
print(percent)
# float(higher)
# %%
from pathlib import Path  # noqa: E402

c = Path("README.md").read_text(encoding="utf8")
# %%
import re  # noqa: E402

c2 = re.sub(r"[0-9]+%", percent, c)
Path("README.md").write_text(c2)
# %%
