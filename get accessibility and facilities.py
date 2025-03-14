import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('stations.xml')
root = tree.getroot()

# Namespace dictionary to handle the XML namespaces
namespaces = {
    'com': 'http://nationalrail.co.uk/xml/common',
    'add': 'http://www.govtalk.gov.uk/people/AddressAndPersonalDetails',
    '': 'http://nationalrail.co.uk/xml/station'
}

# Initialize an empty list to store all stations' data
stations_data = []

# Iterate over each Station element
for station in root.findall('Station', namespaces):
    # Extract CRS code
    crs_code = station.find('CrsCode', namespaces).text
    
    # Extract facilities
    facilities = {}
    station_facilities = station.find('StationFacilities', namespaces)
    if station_facilities is not None:
        for facility in station_facilities:
            facility_name = facility.tag.split('}')[-1]  # Remove namespace
            facility_available = facility.find('com:Available', namespaces)
            if facility_available is not None:
                facilities[facility_name] = facility_available.text
            else:
                facilities[facility_name] = "Not specified"
    
    # Extract accessibility information
    accessibility = {}
    accessibility_info = station.find('Accessibility', namespaces)
    if accessibility_info is not None:
        for access in accessibility_info:
            access_name = access.tag.split('}')[-1]  # Remove namespace
            access_available = access.find('com:Available', namespaces)
            if access_available is not None:
                accessibility[access_name] = access_available.text
            else:
                accessibility[access_name] = "Not specified"
    
    # Store the extracted information in a dictionary
    station_info = {
        'CRS Code': crs_code,
        'Facilities': facilities,
        'Accessibility': accessibility
    }
    
    # Append the station information to the list
    stations_data.append(station_info)

# Convert the list of stations data to JSON format
json_data = json.dumps(stations_data, indent=4)

# Write the JSON data to a file
with open('stations_data.json', 'w') as json_file:
    json_file.write(json_data)

print("Data extraction to JSON completed!")
