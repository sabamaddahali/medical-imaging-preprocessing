# Medical Imaging Preprocessing Pipeline

This repository demonstrates a Python-based preprocessing workflow for
medical imaging data, designed to support downstream machine learning
applications such as automated brain CT annotation.

The pipeline focuses on **data organization, intensity windowing, and
histogram-based analysis**, which are common preprocessing steps in
medical imaging and AI workflows.

---

## Motivation

Medical imaging datasets (e.g., CT scans in DICOM format) are often large,
heterogeneous, and inconsistently organized. Before training machine
learning models, data must be:

- systematically organized
- normalized or windowed
- inspected for intensity distributions
- validated for consistency

This project addresses those needs by providing a modular preprocessing
pipeline that prepares imaging data for ML-based analysis.

---

## Features

- Recursive traversal of DICOM directories
- Imaging plane detection (axial, sagittal, coronal) using direction cosines
- Intensity windowing (HU-style clipping)
- Histogram generation for pixel intensity analysis
- Structured output directory organization
- Robust error handling for large datasets

---

## Pipeline Overview

1. Walk through a base directory containing DICOM files  
2. Read image data using SimpleITK  
3. Determine the imaging plane from orientation metadata  
4. Organize files into a structured directory hierarchy  
5. Apply intensity windowing  
6. Generate and save histogram visualizations  

---

## Privacy and Data Ethics

**Important Note on Data Privacy**

This repository **does not include any real medical data**.

- All identifiers in this code are **synthetic or anonymized**
- No patient IDs, accession numbers, or protected metadata are extracted
- Example paths and outputs are placeholders only

The logic in this repository was developed during a research internship
supporting medical imaging workflows. The public version is intentionally
sanitized to preserve patient privacy and research confidentiality.

---

## Technologies Used

- Python 3
- NumPy
- SimpleITK
- Matplotlib
- OS / filesystem utilities

---

## File Structure

