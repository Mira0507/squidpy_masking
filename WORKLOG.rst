squidpy_masking
===============

2025-08-01
----------

@Mira0507

- Image masking using toy images
    - conda env: `env`
    - script: `script/segmentation.Rmd`
        - update: masking performed using `sq.im.segment` based on the following methods:
            - Otsu thresholding
            - watershed segmentation

2025-08-04
----------

@Mira0507

- Conda env updated
    - path: `env`
    - packages: `wget`, `vst2tif`
    - GitHub: https://github.com/andreped/vsi2tif
    - Tutorial: https://github.com/andreped/vsi2tif/blob/main/notebooks/conversion_tutorial_macos.ipynb

    .. code-block:: bash

        # Installation
        pip install git+https://github.com/andreped/vsi2tif
        wget http://downloads.openmicroscopy.org/latest/bio-formats5.6/artifacts/bftools.zip
        unzip bftools.zip

- Update Masking script
    - conda env: `env`
    - script: `script/segmentation.Rmd`
    - updates
        - explore images using napari

- Script image conversion from `vsi` to `tif` (in progress)
    - conda env: `env`
    - temp script: `script/image_format.py`


2025-08-05
----------

@Mira0507

- Install `bftools` in conda env (`env`) for image conversion
    - https://docs.openmicroscopy.org/bio-formats/6.0.1/users/comlinetools/index.html
    - https://docs.openmicroscopy.org/bio-formats/6.0.1/users/comlinetools/conversion.html
- Convert `vsi` to `tif`/`tiff` image files
    - conda env: `env`
    - script: `script/image_format.py`


2025-08-07
----------

@Mira0507

- Start to work on work computer (MacBook M2 Pro Sequoia 15.6)
    - Build a new conda env using the `requirements.txt` file
    - Export as `env.archived.yaml`

- Install `bftools` in `env` by calling `pip install bftools`
    - GitHub repo: https://github.com/BobDotCom/bftools
    - Aim: Convert `vst` to `tif` using the `bftools` package
      as documented in https://bio-formats.readthedocs.io/en/stable/users/comlinetools/index.html


2025-08-08
----------

@Mira0507

- Convert `vsi` to `tif` using `bfconvert`
    - conda env: `env`
    - demo script: `scripts/image_conversion.Rmd`
    - key commands

    .. code-block:: bash

        # Explore input image metadata
        showinf ../images/input/NoPerm/Image_169.vsi &> image_conversion/input_metadata.txt

        # Series of interest from the input_metadata.txt
        ## Series #14 :
        ##  Image count = 5
        ##  RGB = false (1) 
        ##  Interleaved = false
        ##  Indexed = false (false color)
        ##  Width = 33874
        ##  Height = 33872
        ##  SizeZ = 1
        ##  SizeT = 1
        ##  SizeC = 5
        ##  Tile size = 512 x 512
        ##  Thumbnail size = 128 x 127
        ##  Endianness = motorola (big)
        ##  Dimension order = XYCZT (uncertain)
        ##  Pixel type = uint16
        ##  Valid bits per pixel = 16
        ##  Metadata complete = true
        ##  Thumbnail series = false
        ##  -----
        ##  Plane #0 <=> Z 0, C 0, T 0
        ##  Plane #2 <=> Z 0, C 2, T 0
        ##  Plane #4 <=> Z 0, C 4, T 0

        # Convert the series of interest to TIF
        bfconvert -compression LZW \
            -overwrite \
            -series 14 \
            ../images/input/NoPerm/Image_169.vsi \
            image_conversion/converted_169.ome.tif

    - notes
        - Pick one series with multi-channel and the highest resolution from input metadata
        - QuPath couldn't open the converted TIF file due to memory shortage. Instead, Napari worked!
        - The output TIF file showed 5 channels on the Napari viewer.

- Perform image masking on the converted TIF file (in progress)
    - conda env: `env`
    - script: `scripts/segmentation_tif.Rmd`

2025-08-10
----------

@Mira0507

- Update `README.md` to include the `Scripts` section



2025-08-11
----------

@Mira0507

- Install `jupyter` in `conda env` using conda and export updated `env` to `env.archived.yaml`

- Run image masking on converted `tif` image using squidpy
    - conda env: `env`
    - scripts: 
        - `scripts/segmentation_tif.Rmd`
        - `scripts/segmentation_tif.ipynb`
    - notes
        - Python scripts in both `Rmd` and `ipynb` ended up being killed
        - It appears to be associated with a memory shortage on my Macbook with 32B memory
        - Images need to be cropped when running locally

- Update the script converting image from `vsi` to `tif`
    - conda env: `env`
    - script: `scripts/image_conversion.Rmd`
    - notes: 
        - script enhanced to include code scanning and selecting one series with the highest 
          resolution and multi-channel fluorescence data 
        - the `bfconvert` required to rerun with the following parameters generating *pyramidal* output
            - `-pyramid-resolutions`
            - `-pyramid-scale` 
        - QuPath and napari successfully read the converted `tif` file from the series with the highest 
          resolution (33874 x 33872) when the output was the pyramidal format.


2025-08-12
----------

@Mira0507

- Convert image format from `vsi` to `tif` 
    - conda env: `env`
    - input:
        - `images/input/Perm/Image_169.vsi`
        - `images/input/NoPerm/Image_168.vsi`
    - scripts:
        - `scripts/image_conversion_perm.Rmd`
        - `scripts/image_conversion_noperm.Rmd`
    - notes:
        - analysis performed locally on work computer
        - `scripts/image_conversion.Rmd` deleted

- Run Squidpy segmentation on cropped TIF image
    - conda env: `env`
    - scripts: 
        - `scripts/segmentation_perm_500.Rmd`
        - `scripts/segmentation_perm_1000.Rmd`
        - `scripts/segmentation_noperm_500.Rmd`
        - `scripts/segmentation_noperm_1000.Rmd`
    - notes
        - ran locally on work computer
        - 500 and 1000 indicate N x N dimension in pixels
        - analyzing a full image crashed
        - unnecessary files deleted
            - `scripts/segmentation_tif.Rmd`
            - `scripts/segmentation_tif.ipynb`

- Transfer the working directory to HPC. 
    - re-build the conda environment using `requirements.txt`
    - add `bftools` to the `requirements.txt` instead of using `pip`
    - update `env.archived.yaml` on HPC
    - rerun analyses 
        - conda env: `env`
        - scripts
            - `scripts/image_conversion_perm.Rmd`
            - `scripts/image_conversion_noperm.Rmd`
            - `scripts/segmentation_perm_500.Rmd`
            - `scripts/segmentation_perm_1000.Rmd`


2025-08-13
----------

@Mira0507

- rerun analyses on HPC
    - conda env: `env`
    - scripts
        `scripts/segmentation_noperm_1000.Rmd`
        `scripts/segmentation_noperm_500.Rmd`

- run segmentation without cropping
    - conda env: `env`
    - script: `scripts/segmentation_perm.Rmd`
    - notes
        - 200G exceeded 200G memory
        - we can put this on hold while focus on improving cropped images

- add a step to merge binarized signals (in progress)
    - conda env: `env`
    - script: `scripts/segmentation_perm_500.Rmd`


2025-08-14
----------

@Mira0507

- merge binarized signals 
    - conda env: `env`
    - script: `scripts/segmentation_perm_500.Rmd`
    - script: `scripts/segmentation_perm_1000.Rmd`
    - notes:
        - output images saved
        - channels of interest
            - merge 1: DAPI + TDP43
            - merge 2: IBA1 + MAP2 + ALDH1L1
