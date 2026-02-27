import glob
import os
import pandas as pd
import random

def copy_iu_data(selected_files, source_dir, target_dir):
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    for file in selected_files:
         os.system(f'cp {os.path.join(source_dir, file)} {target_dir}')

if __name__ == "__main__":
    cohorts = ["Black_cohort", "White_cohort"]
    files_count = 50

    for cohort in cohorts:
        source_dir = f"data/hari_BC/patches/{cohort}"
        files = glob.glob(os.path.join(source_dir, '*'))
        random.shuffle(files)

        selected_files = files[:files_count]
        selected_files = [os.path.basename(file) for file in selected_files]

        source_dir = f"data/hari_BC/patches/{cohort}"
        target_dir = f"SAMPath/hari_BC/img/"
        copy_iu_data(selected_files, source_dir, target_dir)

        source_dir = f"data/hari_BC/otsu/epi_mask_no_bg/{cohort}"
        target_dir = f"SAMPath/hari_BC/otsu_epi_mask/"
        copy_iu_data(selected_files, source_dir, target_dir)

        source_dir = f"data/hari_BC/bg_mask/{cohort}"
        target_dir = f"SAMPath/hari_BC/bg_mask/"
        copy_iu_data(selected_files, source_dir, target_dir)