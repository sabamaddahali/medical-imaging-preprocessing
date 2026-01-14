import os
import numpy as np
import SimpleITK as sitk
import matplotlib.pyplot as plt
import shutil

# Utility functions

def apply_windowing(image_array, window_min=-100, window_max=100):
    """
    Clip image intensities to a specified window range.
    """
    return np.clip(image_array, window_min, window_max)


def plot_histogram(image_array, output_path):
    """
    Plot and save histogram of pixel intensities.
    """
    plt.figure()
    plt.hist(image_array.flatten(), bins=50, color='c', edgecolor='black')
    plt.title("Histogram of Pixel Intensities")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.savefig(output_path)
    plt.close()


def determine_plane(direction, threshold=0.5):
    """
    Determine imaging plane from DICOM direction cosines.
    """
    direction = np.abs(np.array(direction))

    if np.all(direction[[0, 4, 8]] > threshold):
        return "axial"
    elif np.all(direction[[1, 5, 3]] > threshold):
        return "sagittal"
    elif np.all(direction[[2, 3, 7]] > threshold):
        return "coronal"
    else:
        return "unknown"


# Main processing function

def process_dicom_directory(base_dir, output_dir):
    """
    Walk through a directory of DICOM files, organize them,
    apply windowing, and save histograms.
    """

    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.lower().endswith(".dcm"):
                continue

            file_path = os.path.join(root, file)

            try:
                ds = sitk.ReadImage(file_path)
                image_array = sitk.GetArrayFromImage(ds)

                # Use anonymized identifiers
                patient_id = "Patient_Anon"
                study_id = "Study_Anon"

                plane = determine_plane(ds.GetDirection())

                target_dir = os.path.join(output_dir, patient_id, study_id, plane)
                os.makedirs(target_dir, exist_ok=True)

                target_file = os.path.join(target_dir, file)
                shutil.copy2(file_path, target_file)

                # Apply windowing + histogram
                windowed = apply_windowing(image_array)
                hist_path = target_file.replace(".dcm", "_histogram.png")
                plot_histogram(windowed, hist_path)

                print(f"Processed {file}")

            except Exception as e:
                print(f"Failed on {file_path}: {e}")
