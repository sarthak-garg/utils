# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:07:49 2018

@author: GargSart
"""

# Make the necessary imports
import os
import json
import xml.etree.ElementTree as ET

# Define the required paths
input_dir = "..\Help"
output_dir = "..\Output"

# Create the output dir if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate through each XML help file in the Help dir
for file in os.listdir(input_dir):
    if file.endswith(".xml"):  
        file_path = os.path.join(input_dir, file)   
        
        # Parse the XML and get its content
        root = ET.parse(file_path).getroot()   
        file_content = ""
        for node in root.iter():
            if node.text is not None:
                node_text = node.text
                node_text = node_text.replace('\n', ' ')
                node_text = node_text.replace('"', '')
                file_content += node_text
                
        # Convert the file content to JSON
        data = {}
        data["id"] = file
        data["text"] = file_content
        json_content = json.dumps(data)
        
        # Create the output file
        file_name = os.path.splitext(os.path.basename(file))[0] + ".json"
        output_path = os.path.join(output_dir, file_name)
        output_file = open(output_path, "w", encoding='utf-8')
        
        # Write content to the output file
        output_file.write(json_content)
        output_file.close()