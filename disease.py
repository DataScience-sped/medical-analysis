import folium
import pandas as pd

# Sample data for locations and diseases
locations_data = {
    'Name': ['Hospital A', 'Nursing Home B', 'Hospital C', 'Nursing Home D', 'Hospital B', 'Hospital D', 'Nursing Home E', 'Nursing Home X', 'Nursing Home M', 'Hospital Z'],
    'Latitude': [40.7128, 21.8975, 65.4356, 33.6521, 75.6857, 29.8796, 4.56231, 68.8792, 71.589, 54.6897],
    'Longitude': [-74.0060, -63.0981, -49.5163, -21.5647, -75.4562, -42.6789, -25.5631, -53.1458, -61.3287, -1.69871],
    'Type': ['Hospital', 'Nursing Home', 'Hospital', 'Nursing Home', 'Hospital', 'Hospital', 'Nursing Home', 'Nursing Home', 'Nursing Home', 'Hospital']
}
disease_data = {
    'Disease': ['Flu', 'Cold', 'Diabetes', 'Heart Disease', 'Cancer', 'Dengue', 'Corona', 'Normal Injury', 'Psychological Imbalance', 'Trauma'],
    'Latitude': [40.7128, 21.8975, 65.4356, 33.6521, 75.6857, 29.8796, 4.56231, 68.8792, 71.589, 54.6897],
    'Longitude': [-74.0060, -63.0981, -49.5163, -21.5647, -75.4562, -42.6789, -25.5631, -53.1458, -61.3287, -1.69871],
    'Affected': [100, 50, 30, 45, 18, 63, 93, 33, 17, 77]
}

# Create DataFrames
locations_df = pd.DataFrame(locations_data)
diseases_df = pd.DataFrame(disease_data)

# Create a map centered around a specific location
map_center = [4.00000, -76.00000]
disease_map = folium.Map(location=map_center, zoom_start=14)

# Function to assign colors based on disease
def get_color(disease):
    colors = {
        'Flu': 'blue',
        'Cold': 'green',
        'Diabetes': 'orange',
        'Heart Disease': 'red',
        'Cancer': 'violet',
        'Dengue': 'purple',
        'Corona': 'yellow',
        'Normal Injury': 'brown',
        'Psychological Imbalance': 'indigo',
        'Trauma': 'gray'
    }
    return colors.get(disease, 'white')

# Add hospitals and nursing homes to the map
for _, row in locations_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Name'],
        icon=folium.Icon(color='purple' if row['Type'] == 'Hospital' else 'lightblue')
    ).add_to(disease_map)

# Add diseases to the map with color coding
for _, row in diseases_df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['Affected'] / 10,
        color=get_color(row['Disease']),
        fill=True,
        fill_opacity=0.6,
        popup=f"{row['Disease']} - Affected: {row['Affected']}"
    ).add_to(disease_map)

# Create a legend
legend_html = """
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 150px; height: auto; 
            background-color: white; 
            border: 2px solid grey; 
            z-index: 9999; 
            font-size: 14px;
            padding: 10px; 
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);">
    <b>Disease Legend</b><br>
    <i style="color: blue;">&#9679;</i> Flu<br>
    <i style="color: green;">&#9679;</i> Cold<br>
    <i style="color: orange;">&#9679;</i> Diabetes<br>
    <i style="color: red;">&#9679;</i> Heart Disease<br>
    <i style="color: violet;">&#9679;</i> Cancer<br>
    <i style="color: purple;">&#9679;</i> Dengue<br>
    <i style="color: yellow;">&#9679;</i> Corona<br>
    <i style="color: brown;">&#9679;</i> Normal Injury<br>
    <i style="color: indigo;">&#9679;</i> Psychological Imbalance<br>
    <i style="color: gray;">&#9679;</i> Trauma<br>
</div>
"""

# Add the legend to the map using a custom HTML element
disease_map.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
disease_map.save('disease_analysis_map.html')

# HTML for the home page with medical images
html_home = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Analysis</title>
    <link rel="stylesheet" href="path/to/styles.css">
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            background-color: #f0f8ff; /* Light blue background */
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #2c3e50; /* Dark blue color for the title */
            margin-top: 50px;
        }
        .container {
            margin: 30px auto;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px; /* Space between images */
        }
        img {
            width: 200px;
            height: auto;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .link {
            display: inline-block;
            margin: 30px;
            text-decoration: none;
            color: white;
            background-color: #3498db; /* Blue button */
            padding: 15px 25px;
            border-radius: 5px;
            font-size: 18px;
            transition: background-color 0.3s;
        }
        .link:hover {
            background-color: #2980b9; /* Darker blue on hover */
        }
    </style>
</head>
<body>
    <h1>Medical Analysis</h1>
    <div class="container">
        <img src="images/nursing home.jpg" alt="Nursing Home" title="Nursing Home">
        <img src="images/hospital.jpg" alt="Hospital" title="Hospital">
        <img src="images/disease.png" alt="Disease" title="Disease">
        <img src="images/health.png" alt="Health" title="Health">
    </div>
    <a class="link" href="disease_analysis_map.html">View Disease Analysis Map</a>
</body>
</html>
"""

# Save the home page to an HTML file
with open('index.html', 'w') as f:
    f.write(html_home)

print("HTML files created: index.html and disease_analysis_map.html")
