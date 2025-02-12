import bpy
import os
import numpy as np

# Define the output folder for STL exports
output_folder = ""  # Change this path

# Ensure the base output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Select the objects to modify
pillar = bpy.data.objects.get("Pillar")  # Change to the actual pillar object name
base = bpy.data.objects.get("Base")  # Change to the actual base object name

if pillar is None or base is None:
    print("Error: One or both objects not found!")
else:
    # Define parameter ranges
    param1_values = np.arange(1.3, 2.9, 0.1)  # Period scaling for base (X-axis)
    param2_values = np.arange(0.6, 2.6, 0.1)  # Height scaling for pillar (Z-axis)
    

    for scale_factor_period in param1_values:
        z = 0.8
        for scale_factor_height in param2_values:
            # Modify object scales
            base.scale.x = scale_factor_period  # Scale base in X
            pillar.scale.z = scale_factor_height  # Scale pillar in Z
            pillar.location.z = z

            # Create a folder for each period value
            period_folder = os.path.join(output_folder, f"p={scale_factor_period:.1f}/")
            if not os.path.exists(period_folder):
                os.makedirs(period_folder)

            # Generate STL filename and path
            file_name = f"h={scale_factor_height:.1f}.stl"
            file_path = os.path.join(period_folder, file_name)

            # Ensure objects are selected for export
            bpy.ops.object.select_all(action='DESELECT')  # Deselect all
            pillar.select_set(True)  # Select pillar
            base.select_set(True)  # Select base

            # Export as STL
            bpy.ops.export_mesh.stl(filepath=file_path, use_selection=True)
            print(f"Exported: {file_path}")
            z += 0.05
