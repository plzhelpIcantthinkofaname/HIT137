import pandas as pd  
import os  
  
# Define the seasons and their corresponding months  
seasons = {  
   'Summer': ['December', 'January', 'February'],  
   'Autumn': ['March', 'April', 'May'],  
   'Winter': ['June', 'July', 'August'],  
   'Spring': ['September', 'October', 'November']  
}  
  
# Create a dictionary to store the temperatures for each place  
place_temps = {}  
  
# Iterate over all CSV files in the folder  
for filename in os.listdir():  
   if filename.endswith(".csv"):  
      # Read the CSV file  
      df = pd.read_csv(filename)  
  
      # Get the place names  
      places = df.iloc[:, 0]  
  
      # Iterate over each place  
      for index, place in enumerate(places):  
         # Calculate the average temperature for each season  
         season_temps = {}  
         for season, months in seasons.items():  
            temps = []  
            for month in months:  
               if month in df.columns:  
                  temps.append(df.iloc[index][df.columns.tolist().index(month)])  
            season_temps[season] = temps  
  
         # Add the temperatures to the place_temps dictionary  
         if place in place_temps:  
            for season, temp_list in season_temps.items():  
               place_temps[place][season].extend(temp_list)  
         else:  
            place_temps[place] = {season: temp_list for season, temp_list in season_temps.items()}  
  
# Create a new DataFrame to store the results  
result_df = pd.DataFrame(columns=['Place', 'Summer', 'Autumn', 'Winter', 'Spring'])  
  
# Calculate the average temperature for each season and place  
for place, temps in place_temps.items():  
   season_avgs = {}  
   for season, temp_list in temps.items():  
      if len(temp_list) > 0:  
        season_avgs[season] = sum(temp_list) / len(temp_list)  
      else:  
        season_avgs[season] = 0  
   result_df = pd.concat([result_df, pd.DataFrame({'Place': [place], 'Summer': [season_avgs['Summer']], 'Autumn': [season_avgs['Autumn']], 'Winter': [season_avgs['Winter']], 'Spring': [season_avgs['Spring']]})], ignore_index=True)  
  
# Save the result DataFrame to a new CSV file  
result_df.to_csv('seasonal_temps.csv', index=False)  

# Create a new DataFrame to store the top 5 stations with the largest temperature range
temp_ranges = []
for place, temps in place_temps.items():
    all_temps = [temp for temp_list in temps.values() for temp in temp_list]
    temp_range = max(all_temps) - min(all_temps)
    temp_ranges.append({'Place': place, 'Temperature Range': temp_range})

temp_range_df = pd.DataFrame(temp_ranges)
top_5_temp_range_df = temp_range_df.nlargest(5, 'Temperature Range')
top_5_temp_range_df.to_csv('top_5_temp_range.csv', index=False)

# Create a new DataFrame to store the 5 stations with the highest temperature and 5 stations with the lowest
all_temps = []
for place, temps in place_temps.items():
    for season, temp_list in temps.items():
        for temp in temp_list:
            all_temps.append({'Place': place, 'Temperature': temp})

all_temps_df = pd.DataFrame(all_temps)

# Get the top 5 highest temperatures for each place
top_5_highest_temp_df = all_temps_df.loc[all_temps_df.groupby('Place')['Temperature'].idxmax()]
top_5_highest_temp_df = top_5_highest_temp_df.nlargest(5, 'Temperature')[['Place', 'Temperature']]

# Get the bottom 5 lowest temperatures for each place
bottom_5_lowest_temp_df = all_temps_df.loc[all_temps_df.groupby('Place')['Temperature'].idxmin()]
bottom_5_lowest_temp_df = bottom_5_lowest_temp_df.nsmallest(5, 'Temperature')[['Place', 'Temperature']]

# If there are less than 5 unique places, get the remaining places from the original data
if len(top_5_highest_temp_df) < 5:
    remaining_places = all_temps_df[~all_temps_df['Place'].isin(top_5_highest_temp_df['Place'])]
    remaining_places = remaining_places.nlargest(5 - len(top_5_highest_temp_df), 'Temperature')[['Place', 'Temperature']]
    top_5_highest_temp_df = pd.concat([top_5_highest_temp_df, remaining_places])

if len(bottom_5_lowest_temp_df) < 5:
    remaining_places = all_temps_df[~all_temps_df['Place'].isin(bottom_5_lowest_temp_df['Place'])]
    remaining_places = remaining_places.nsmallest(5 - len(bottom_5_lowest_temp_df), 'Temperature')[['Place', 'Temperature']]
    bottom_5_lowest_temp_df = pd.concat([bottom_5_lowest_temp_df, remaining_places])

top_bottom_temp_df = pd.concat([top_5_highest_temp_df, bottom_5_lowest_temp_df])
top_bottom_temp_df.to_csv('top_bottom_5_temps.csv', index=False)
