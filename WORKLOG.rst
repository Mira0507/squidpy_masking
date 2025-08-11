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
        - I need to rerun using cropped images

- Update the script converting image from `vsi` to `tif`
    - conda env: `env`
    - script: `scripts/image_conversion.Rmd`
    - notes: 
        - script enhanced to include code scanning and selecting one series with the highest 
          resolution and multi-channel fluorescence data
        - QuPath nor Fiji cannot open the output `tif` file due to a memory shortage. This issue 
          can be resolved by re-converting to the pyrimidal `tif` format.
        - the `bfconvert` command re-ran with the following parameters added
            - `-tilex`
            - `-tiley`
            - `-pyramid-resolutions`
