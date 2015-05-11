"""
Mock analysis of data that outputs a png figure and a json file
"""

import json
import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.ylabel("speed")
plt.xlabel("time")
plt.title("sample mesurements")
plt.savefig("result_plot.png", bbox_inches="tight")


results = {"foo": 33.53, "bar": 43}

supplementary_results = {"foo_std":94,"bar_std":100}

with open("results.json", "w") as outfile:
    json.dump(results, outfile)

with open("supplementary_results.json", "w") as outfile:
    json.dump(supplementary_results, outfile)