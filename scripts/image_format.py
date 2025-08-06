import numpy as np
import matplotlib.pyplot as plt
import squidpy as sq
import napari
import os
import subprocess


outdir = "../images/converted"
os.makedirs(outdir, exist_ok=True)

bfc = "../bftools/bfconvert"
qupath = "../bftools/bfconvert"

im0 = "../images/NoPerm_RNAseInhib_20250512/Image_169.vsi"
im1 = "../images/Perm_RNAseInhib_20250512/Image_168.vsi"
im2 = "../images/NoPerm_RNAseInhib_20250512/tiffzoom/Image_02.vsi"
im3 = "../images/Perm_RNAseInhib_20250512/tiffzoom/Image_01.vsi"

img_dic = {'im0' : {'in': im0}, 'im1' : {'in' : im1}, 'im2' : {'in' : im2}, 'im3' : {'in' : im3}}

for key, value in img_dic.items():
    value['out'] = f"{outdir}/{key}.tif" 

input_image = 'im0'
cmd = ["vsi2tif -i", img_dic[input_image]['in'], "-o", img_dic[input_image]['out'], "-b", bfc]
cmd = " ".join(cmd)
subprocess.run(cmd, shell=True)

input_image = 'im1'
cmd = ["vsi2tif -i", img_dic[input_image]['in'], "-o", img_dic[input_image]['out'], "-b", bfc]
cmd = " ".join(cmd)
subprocess.run(cmd, shell=True)

input_image = 'im2'
cmd = ["vsi2tif -i", img_dic[input_image]['in'], "-o", img_dic[input_image]['out'], "-b", bfc]
cmd = " ".join(cmd)
subprocess.run(cmd, shell=True)

input_image = 'im3'
cmd = ["vsi2tif -i", img_dic[input_image]['in'], "-o", img_dic[input_image]['out'], "-b", bfc]
cmd = " ".join(cmd)
subprocess.run(cmd, shell=True)




if not os.path.exists(img_dic[input_image]['out']):
    subprocess.run(, shell=True)
