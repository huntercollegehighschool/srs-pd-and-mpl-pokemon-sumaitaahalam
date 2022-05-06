"""
Below is some code that takes in Pokemon data from all 8 generations released so far. You can run the code. Be sure to read through the descriptions and the code.
"""

import pandas as pd
import matplotlib.pyplot as plt

pokedex = pd.read_csv("pokedex.csv", index_col=1)

"""
Below is some code that first calculates how many of each type of Pokemon currently exists. Note that a Pokemon like Bulbasaur has two types, Grass and Poison, so we want that to accounted for in both the Grass and the Poison counts.
"""
type1count = pokedex['type_1'].value_counts()
type2count = pokedex['type_2'].value_counts()

typecount = (type1count + type2count).sort_values(ascending=False)

"""
1. Print what's in the typecount variable so that we can see a table (series) of how many of each type there are.

What is the most abundant type of Pokemon?

"""


"""
2. Let's use matplotlib to create a bar chart that shows visually how many of each type there are. Use and run the code below.
fig = plt.figure(figsize=(6, 3))
typecount.plot.bar()
plt.show()
"""


"""
Each Pokemon has 6 different stats: HP, ATTACK, DEFENSE, SPECIAL ATTACK, SPECIAL DEFENSE, and SPEED. Those stats added together is their TOTAL POINTS, which is already a column in the pokedex dataframe. The code below calculate the average total points for each type of Pokemon.
"""
tp1 = pokedex[['type_1', 'total_points']].groupby('type_1').agg(['size', 'mean'])
tp2 = pokedex[['type_2', 'total_points']].groupby('type_2').agg(['size', 'mean'])
totalpoints = (tp1['total_points']['mean']*tp1['total_points']['size'] + tp2['total_points']['mean']*tp2['total_points']['size'])/(tp1['total_points']['size']+tp2['total_points']['size'])  # uses a weighted average since averages had to be calculated using data from two different columns

"""
3. Print totalpoints and see what appears on the console.

What type appears to have the lowest total points?

What type appears to have the highest total points?

"""



"""
4. Like you did in #2, display a bar chart that shows the type and average total points.
"""




"""
5. There's a thing in Pokemon called legendary Pokemon (like Mewtwo), mythical Pokemon (like Mew), and mega evolved Pokemon (like Mega Charizard) who's stats tend to be ridiculously high. The code below is the beginning of removing those pokemon from the dataframe. The dataframe also contains columns 'is_mythical' and 'is_mega' which denote mythical and mega evolved pokemon. Modify the code below so that all the pokemon in the aforementioned categories are removed from the dataframe.
"""
nonspecial = pokedex[(pokedex['is_legendary']==0) & (pokedex['is_sub_legendary']==0)]

"""
6. Print the nonspecial pokedex. Does it even the playing field?
"""



"""
7. Using what you just did on the original pokedex (with legendaries), try to figure out which type of Pokemon has the highest of each stat.
"""

"""
Highest Average HP:
Highest Average Attack:
Highest Average Defense:
Highest Average Special Attack:
Highest Average Special Defense:
Highest Average Speed:
"""