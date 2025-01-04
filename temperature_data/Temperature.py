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
  
      # Get the place name  
      place = df.iloc[0, 0]  
  
      # Calculate the average temperature for each season  
      season_temps = {}  
      for season, months in seasons.items():  
        temps = []  
        for month in months:  
           if month in df.columns:  
              temps.append(df.iloc[0][df.columns.tolist().index(month)])  
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