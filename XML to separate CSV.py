import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
import os

# Load the XML file
file_path = r"E:\OneDrive\JSU\02 Areas\05 Site Monitoring\Bangladesh\Report\Baghabari\Baghabari.xml"

# Create output directory
output_dir = r"E:\OneDrive\JSU\02 Areas\05 Site Monitoring\Bangladesh\Report\Baghabari"

os.makedirs(output_dir, exist_ok=True)

tree = ET.parse(file_path)
root = tree.getroot()

# Extract namespaces
namespaces = {'ns': 'http://www.landxml.org/schema/LandXML-1.2'}

# Extract profiles information
profiles = {}
for profile in root.findall('.//ns:Profile', namespaces):
    profile_name = profile.get('name')
    surface_name = profile.find('.//ns:ProfSurf', namespaces).get('name')
    state = profile.find('.//ns:ProfSurf', namespaces).get('state')
    pnt_list_2d = profile.find('.//ns:ProfSurf/ns:PntList2D', namespaces).text.strip().split()
    
    x_points = [float(pnt_list_2d[i]) for i in range(0, len(pnt_list_2d), 2)]
    y_points = [float(pnt_list_2d[i + 1]) for i in range(0, len(pnt_list_2d), 2)]
    
    profiles[profile_name] = {
        'Surface Name': surface_name,
        'State': state,
        'X': x_points,
        'Y': y_points
    }



# Save profiles information to separate CSV files
for profile_name, data in profiles.items():
    output_file = os.path.join(output_dir, f'{profile_name}.csv')
    df = pd.DataFrame({'X': data['X'], 'Y': data['Y']})
    df.to_csv(output_file, index=False)
    print(f"Profile {profile_name} saved to {output_file}")

# Function to calculate cumulative distance and plot profiles
def plot_profile_corrected(profile_name, profile_data):
    x_coords = profile_data['X']
    y_coords = profile_data['Y']
    
    # Calculate cumulative distance for the X-axis
    distances = [0]
    for i in range(1, len(x_coords)):
        dist = sqrt((x_coords[i] - x_coords[i-1])**2 + (y_coords[i] - y_coords[i-1])**2)
        distances.append(distances[-1] + dist)
    
    plt.figure(figsize=(10, 6))
    plt.plot(distances, y_coords, label=profile_name)
    plt.xlabel('Cumulative Distance (m)', fontsize=18)
    plt.ylabel('Y Coordinate (m)', fontsize=18)
    plt.title(f'Profile: {profile_name}', fontsize=18)
    plt.legend()
    plt.grid(True)

    plot_file = os.path.join(output_dir, f'{profile_name}.png')
    plt.savefig(plot_file)  # Save the plot as a PNG file
    plt.show()
    print(f"Plot for profile {profile_name} saved to {plot_file}")

# Plot each profile in a separate graph with corrected X-axis
for profile_name, data in profiles.items():
    plot_profile_corrected(profile_name, data)