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

