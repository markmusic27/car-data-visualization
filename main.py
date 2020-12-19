import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# LOAD DATASET / INIT SEABORN

df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")

x = "# Gears"
y = "CombMPG"

sns.set()

# SCATTER PLOT

sns.scatterplot(x=x, y=y, data=df)

# LINEAR REGRESSION PLOT

sns.lmplot(x=x, y=y, data=df)


# JOINT PLOT

sns.jointplot(x=x, y=y, data=df)

# BOX & WHISKER PLOT

sns.set(rc={"figure.figsize": (5, 15)})

ax = sns.boxplot(x=x, y=y, data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)


# SWARM PLOT

sx = sns.swarmplot(x=x, y=y, data=df)
sx.set_xticklabels(sx.get_xticklabels(), rotation=45)
