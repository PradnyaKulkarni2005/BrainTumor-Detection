# tests/test_loader.py
import os
from modules.input_loader import load_mri
from modules.preprocessing import extract_slices

# Path to your MRI file (update this!)
file_path = os.path.join("data", "3dsampleimg.nii")


# Load 3D MRI scan
volume = load_mri(file_path)
print("3D volume shape:", volume.shape)

# Extract slices
slices = extract_slices(volume)
print("Extracted slices:", len(slices))
print("One slice shape:", slices[0].shape)
