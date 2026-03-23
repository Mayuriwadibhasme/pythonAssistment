import pandas as pd
from tabulate import tabulate

data = {
    "state": ["Maharashtra", "Uttar Pradesh", "Rajasthan", "Kerala", "Punjab"],
    "area": [307713, 243286, 342239, 38863, 50362],
    "population": [123000000, 241000000, 81000000, 35000000, 30000000]
}

df = pd.DataFrame(data)
df['population_density'] = df['population'] / df['area']

print("\nComplete Information of States:\n")
print(tabulate(df, headers='keys', tablefmt='grid'))

largest_area_state = df.loc[df['area'].idxmax(), 'state']
print("\nState with Largest Area:", largest_area_state)

largest_pop_state = df.loc[df['population'].idxmax(), 'state']
print("State with Largest Population:", largest_pop_state)

print("\nPopulation Density of States:\n")
print(tabulate(df[['state','population_density']], headers='keys', tablefmt='fancy_grid'))

highest_density_state = df.loc[df['population_density'].idxmax(), 'state']
print("\nState with Highest Population Density:", highest_density_state)
