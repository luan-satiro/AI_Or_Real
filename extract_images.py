import zipfile
from pathlib import Path

file_path = '' # Insert r-string of your file's path here

directory_real_path = '' # Insert r-string of the path of the directory you wish the unzipped files of real images to go here
directory_fake_path = '' # Insert r-string of the path of the directory you wish the unzipped files of fake images to go here

with zipfile.ZipFile(file_path, 'r') as zip_ref:
    all_files = zip_ref.namelist()
    
    # Filter by folder/category
    fake_images = [f for f in all_files if 'fake/' in f and f.endswith('.jpg')]

    real_images = [f for f in all_files if 'real/' in f and f.endswith('.jpg')]
    
    # Extract only a subset (e.g., first 100 images)
    target_dir_fake = Path(directory_fake_path) 
    
    target_dir_real = Path(directory_real_path)

    for i, file_path in enumerate(fake_images[:100]): 
        # Extract specific file
        zip_ref.extract(file_path, target_dir_fake)
        
        if (i + 1) % 10 == 0:
            print(f"Extracted {i + 1} images...")

    for i, file_path in enumerate(real_images[:100]):
        # Extract specific file
        zip_ref.extract(file_path, target_dir_real)
        
        if (i + 1) % 10 == 0:
            print(f"Extracted {i + 1} images...")