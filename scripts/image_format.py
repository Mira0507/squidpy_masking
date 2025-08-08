import numpy as np
import matplotlib.pyplot as plt
import squidpy as sq
import napari
import os
import subprocess
import time


outdir = "../images/output"
os.makedirs(outdir, exist_ok=True)

cachedir = "image_format_cache"

im0 = "../images/input/NoPerm/Image_169.vsi"
im1 = "../images/input/Perm/Image_168.vsi"

cmd = f"bfconvert -noflat -compression LZW -overwrite -cache -cache-dir {cachedir} {im0} {outdir}/converted_169.ome.tif"

def run_runtime(): 
    start_time = time.time()
    subprocess.run(cmd, shell=True)
    end_time = time.time()
    run_time_sec = end_time - start_time
    run_time_min = run_time_sec / 60
    print(f"Runtime: {run_time_sec} seconds ({run_time_min} minutes).")

run_runtime()

# In [36]: print(cmd)
# bfconvert -noflat -compression LZW -overwrite -cache -cache-dir image_format_cache ../images/input/NoPerm/Image_169.v
# si ../images/output/converted_169.ome.tif



