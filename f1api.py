from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

session = fastf1.get_session(2019, 'Monza', 'Race')

session.load()
# compound_laps = session.laps()
# print(compound_laps)

compounds = session.laps.pick_compounds("SOFT")
count_nan = compounds["LapTime"].isna().sum()
cleaned_compounds = compounds.dropna()
print(compounds.groupby("Driver"))

x = compounds["LapNumber"][:5]
y = compounds["LapTime"][:5]
plt.plot(x, y)  # Use 'lap_times' for the data

# Customize the plot
plt.xlabel('Lap')
plt.ylabel('Lap Time')
plt.grid(True)  # Add grid lines for better readabil

# Display the plot
plt.show()