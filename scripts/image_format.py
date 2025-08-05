import numpy as np
import matplotlib.pyplot as plt
import squidpy as sq
import napari
import os
import subprocess


outdir = "../images/converted"
os.makedirs(outdir, exist_ok=True)

bfc = "../bftools/bfconvert"

im0 = "../images/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1_Perm+RNAseInhib/Image_168.vsi"
im1 = "../images/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1_Perm+RNAseInhib/tiffzoom/Image_01.vsi"
im2 = "../images/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1_Perm+RNAseInhib/tiffzoom/Image_02.vsi"

img_dic = {'im0' : {'in': im0}, 'im1' : {'in' : im1}, 'im2' : {'in' : im2}}

for key, value in img_dic.items():
    value['out'] = f"{outdir}/{key}.tif" 

In [33]: print(img_dic)
{'im0': 
 {'in': '../images/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1_Perm+RNAseInhib/Image_168.vsi', 'out': '../images/converted/im0.tif'}, 
 'im1': {'in': '../images/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1_Perm+RNAseInhib/tiffzoom/Image_01.vsi', 'out': '../images/converted/im1.tif'}, 
 'im2': {'in': '../images/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1/2025_05_12_121824A_MCTX_FFPE_IBA1_TDP43_MAP2_ALDH1L1_Perm+RNAseInhib/tiffzoom/Image_02.vsi', 'out': '../images/converted/im2.tif'}}

input_image = 'im1'
cmd0 = ["vsi2tif -i", img_dic[input_image]['in'], "-o", img_dic[input_image]['out'], "-b", bfc]
if not os.path.exists(img_dic[input_image]['out']):
    subprocess.run(" ".join(cmd0), shell=True)
