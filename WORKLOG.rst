squidpy_masking
===============

2025-08-01
----------

@Mira0507

- Image masking using toy images
    - conda env: ``env``
    - script: ``script/segmentation.Rmd``
        - update: masking performed using ``sq.im.segment`` based on the following methods:
            - Otsu thresholding
            - watershed segmentation

2025-08-04
----------

@Mira0507

- Conda env updated
    - path: ``env``
    - packages: ``wget``, ``vst2tif``
    - GitHub: https://github.com/andreped/vsi2tif
    - Tutorial: https://github.com/andreped/vsi2tif/blob/main/notebooks/conversion_tutorial_macos.ipynb

    .. code-block:: bash

        # Installation
        pip install git+https://github.com/andreped/vsi2tif
        wget http://downloads.openmicroscopy.org/latest/bio-formats5.6/artifacts/bftools.zip
        unzip bftools.zip

- Update Masking script
    - conda env: ``env``
    - script: ``script/segmentation.Rmd``
    - updates
        - explore images using napari

- Script image conversion from ``vsi`` to ``tif`` (in progress)
    - conda env: ``env``
    - temp script: ``script/image_format.py``


2025-08-05
----------

@Mira0507

- Install ``bftools`` in conda env (``env``) for image conversion
    - https://docs.openmicroscopy.org/bio-formats/6.0.1/users/comlinetools/index.html
    - https://docs.openmicroscopy.org/bio-formats/6.0.1/users/comlinetools/conversion.html
- Convert ``vsi`` to ``tif``/``tiff`` image files
    - conda env: ``env``
    - script: ``script/image_format.py``


2025-08-07
----------

@Mira0507

- Start to work on work computer (MacBook M2 Pro Sequoia 15.6)
    - Build a new conda env using the ``requirements.txt`` file
    - Export as ``env.archived.yaml``

- Install ``bftools`` in ``env`` by calling ``pip install bftools``
    - GitHub repo: https://github.com/BobDotCom/bftools
    - Aim: Convert ``vst`` to ``tif`` using the ``bftools`` package
      as documented in https://bio-formats.readthedocs.io/en/stable/users/comlinetools/index.html


2025-08-08
----------

@Mira0507

- Convert ``vsi`` to ``tif`` using ``bfconvert``
    - conda env: ``env``
    - demo script: ``scripts/image_conversion.Rmd``
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
    - conda env: ``env``
    - script: ``scripts/segmentation_tif.Rmd``

2025-08-10
----------

@Mira0507

- Update ``README.md`` to include the ``Scripts`` section



2025-08-11
----------

@Mira0507

- Install ``jupyter`` in ``conda env`` using conda and export updated ``env`` to ``env.archived.yaml``

- Run image masking on converted ``tif`` image using squidpy
    - conda env: ``env``
    - scripts: 
        - ``scripts/segmentation_tif.Rmd``
        - ``scripts/segmentation_tif.ipynb``
    - notes
        - Python scripts in both ``Rmd`` and ``ipynb`` ended up being killed
        - It appears to be associated with a memory shortage on my Macbook with 32B memory
        - Images need to be cropped when running locally

- Update the script converting image from ``vsi`` to ``tif``
    - conda env: ``env``
    - script: ``scripts/image_conversion.Rmd``
    - notes: 
        - script enhanced to include code scanning and selecting one series with the highest 
          resolution and multi-channel fluorescence data 
        - the ``bfconvert`` required to rerun with the following parameters generating *pyramidal* output
            - ``-pyramid-resolutions``
            - ``-pyramid-scale`` 
        - QuPath and napari successfully read the converted `tif` file from the series with the highest 
          resolution (33874 x 33872) when the output was the pyramidal format.


2025-08-12
----------

@Mira0507

- Convert image format from ``vsi`` to ``tif`` 
    - conda env: ``env``
    - input:
        - ``images/input/Perm/Image_169.vsi``
        - ``images/input/NoPerm/Image_168.vsi``
    - scripts:
        - ``scripts/image_conversion_perm.Rmd``
        - ``scripts/image_conversion_noperm.Rmd``
    - notes:
        - analysis performed locally on work computer
        - ``scripts/image_conversion.Rmd`` deleted

- Run Squidpy segmentation on cropped TIF image
    - conda env: ``env``
    - scripts: 
        - ``scripts/segmentation_perm_500.Rmd``
        - ``scripts/segmentation_perm_1000.Rmd``
        - ``scripts/segmentation_noperm_500.Rmd``
        - ``scripts/segmentation_noperm_1000.Rmd``
    - notes
        - ran locally on work computer
        - 500 and 1000 indicate N x N dimension in pixels
        - analyzing a full image crashed
        - unnecessary files deleted
            - ``scripts/segmentation_tif.Rmd``
            - ``scripts/segmentation_tif.ipynb``

- Transfer the working directory to HPC. 
    - re-build the conda environment using ``requirements.txt``
    - add ``bftools`` to the ``requirements.txt`` instead of using ``pip``
    - update ``env.archived.yaml`` on HPC
    - rerun analyses 
        - conda env: ``env``
        - scripts
            - ``scripts/image_conversion_perm.Rmd``
            - ``scripts/image_conversion_noperm.Rmd``
            - ``scripts/segmentation_perm_500.Rmd``
            - ``scripts/segmentation_perm_1000.Rmd``


2025-08-13
----------

@Mira0507

- rerun analyses on HPC
    - conda env: ``env``
    - scripts
        ``scripts/segmentation_noperm_1000.Rmd``
        ``scripts/segmentation_noperm_500.Rmd``

- run segmentation without cropping
    - conda env: ``env``
    - script: ``scripts/segmentation_perm.Rmd``
    - notes
        - 200G exceeded 200G memory
        - we can put this on hold while focus on improving cropped images

- add a step to merge binarized signals (in progress)
    - conda env: ``env``
    - script: ``scripts/segmentation_perm_500.Rmd``


2025-08-14
----------

@Mira0507

- merge binarized signals 
    - conda env: ``env``
    - scripts: 
        - ``scripts/segmentation_perm_500.Rmd``
        - ``scripts/segmentation_perm_1000.Rmd``
    - notes:
        - output images saved
        - channels of interest
            - merge 1: DAPI + TDP43
            - merge 2: IBA1 + MAP2 + ALDH1L1
            - merge 3: TDP43 + MAP2

2025-08-15
----------

@Mira0507

- merge binarized signals
    - conda env: ``env``
    - scripts: 
        - ``scripts/segmentation_perm_500.Rmd``
        - ``scripts/segmentation_perm_1000.Rmd``
        - ``scripts/segmentation_noperm_500.Rmd``
        - ``scripts/segmentation_noperm_1000.Rmd``
    - notes:
        - pseudocolor palette upated
        - only the lower half of each masking was captured, presumably 
          due to dimming effect in the upper part of each image 
        - it's unclear what part of image processing resulted in dimming
          the upper part 
        _ I need to try adaptive thresholding separately


2025-08-18
----------

@Mira0507

- testing adaptive thresholding
    - conda env: ``env``
    - scripts
        - adaptive thresholding on raw images: 
          ``scripts/segmentation_perm_1000_adaptive.Rmd``
        - adaptive thresholding on equalized images: 
          ``scripts/segmentation_perm_1000_adaptive_eq.Rmd``
    - notes:
        - adaptive thresholding was performed using the ``skimage.filters.threshold_local`` 
          function 
        - erosion was performed, on top of adaptive thresholding, using 
          the ``skimage.morphology.binary_erosion`` function
        - image equalization performed to enhance contrast, using 
          the ``skimage.exposure.equalize_adapthist`` function
        - adaptive thresholding resulted in masking zero pixels on equalized images
        - erosion was helpful to remove noisy specks
        - decided to proceed without equalization for now

- apply adaptive thresholding
    - conda env: ``env``
    - scripts
        - ``scripts/segmentation_perm_1000_adaptive.Rmd``
        - ``scripts/segmentation_perm_500_adaptive.Rmd``
        - ``scripts/segmentation_noperm_1000_adaptive.Rmd``
        - ``scripts/segmentation_noperm_500_adaptive.Rmd``


2025-08-19
----------

@Mira0507

- update ``README.md``

- prep snakemake environment 
    - ``snakemake<9`` installed in ``env``
    - ``scripts/WRAPPER_SLURM`` added
    - config added
        - ``scripts/config/sampletable.txt`` (tab-separated file)
        - ``scripts/config/config.yaml``
    - writing ``Snakefile`` in progress


2025-08-20
----------

@Mira0507

- add ``snakemake-executor-plugin-cluster-generic`` to conda env (``env``)
    - this is required to avoid the following error when running 
      with the `v8 profile 
      <https://github.com/NIH-HPC/snakemake_profile/tree/snakemake8>`_

    .. code-block:: bash

        # snakemake --dry-run --profile $SNAKEMAKE_PROFILE_V8
        snakemake: error: argument --executor/-e: invalid choice: 'cluster-generic' (choose from 'local', 'dryrun', 'touch')

    - Refer to https://github.com/NIH-HPC/snakemake_profile/pull/4/commits/005dfaa174552cbc9b300d4c87c3a5a75540e4b8
      for more info

- write ``Snakefile``
    - rule ``convert`` added
    - wrapper script ``scripts/wrapper_rmd/image_conversion.rmd`` scripting in progress


2025-08-21
----------

@Mira0507

- write ``Snakefile``
    - rule ``convert`` updated
    - wrapper script ``scripts/wrapper_rmd/image_conversion.Rmd`` updated 

- update ``README.md``


2025-08-22
----------

@Mira0507

- reorganize directory structure
    - ``scripts/*.Rmd`` files moved into the ``scripts/individual`` directory

    .. code-block:: bash

        $ ls scripts/individual | grep Rmd
        image_conversion_noperm.Rmd
        image_conversion_perm.Rmd
        segmentation_noperm_1000_adaptive.Rmd
        segmentation_noperm_1000.Rmd
        segmentation_noperm_500_adaptive.Rmd
        segmentation_noperm_500.Rmd
        segmentation_perm_1000_adaptive_eq.Rmd
        segmentation_perm_1000_adaptive.Rmd
        segmentation_perm_1000.Rmd
        segmentation_perm_500_adaptive.Rmd
        segmentation_perm_500.Rmd
        segmentation_perm.Rmd
        segmentation.Rmd

    - rerun the moved scripts in the ``scripts/individual`` directory
    - move files for snakemake into the ``scripts/snakemake`` directory

    .. code-block:: bash

        $ tree scripts/snakemake/
        scripts/snakemake/
        ├── config
        │   ├── config.yaml
        │   └── sampletable.txt
        ├── image_conversion.Rmd
        ├── Snakefile
        └── WRAPPER_SLURM

- run snakemake converting ``vsi`` to ``tif``
    - conda env: ``env``
    - working directory: ``scripts/snakemake``
    - output

    .. code-block:: bash

        $ tree images/converted/
        images/converted/
        ├── noperm
        │   ├── converted.ome.tif
        │   ├── image_conversion.html
        │   ├── input_metadata.txt
        │   └── output_metadata.txt
        └── perm
            ├── converted.ome.tif
            ├── image_conversion.html
            ├── input_metadata.txt
            └── output_metadata.txt


2025-08-25
----------

@Mira0507

- Validate the effect of adaptive equalization
    - conda env: ``env``
    - script: ``scripts/individual/segmentation_perm_1000_adaptive_eq.Rmd``
    - notes:
        - ``offset`` adjusted to 0
        - noise pixels that are not from IF staining are captured
        - adaptive equalization will not be used in the current analysis

- Validate the effect of erosion
    - conda env: ``env``
    - scripts: 
        - ``scripts/individual/segmentation_perm_1000_adaptive.Rmd``
        - ``scripts/individual/segmentation_perm_500_adaptive.Rmd``
    - notes:
        - the same channel merged with and without erosion across the channels
        - this was performed to ensure that erosion does not end up losing
          significant pixels



2025-08-26
----------

@Mira0507

- Snakemake bugfix
    - conda env: ``env``
    - script: ``scripts/snakemake/image_conversion.Rmd``
    - notes:
        - variables ``ser`` and ``to_pyramidal`` set to ``None`` and ``True`` 
          were not correctly read in the ``image_conversion.Rmd`` script
        - ``to_variable`` changed from ``True``/``False`` to ``"Y"``/``"N"`` 
        - ``ser`` changed from ``None`` to ``"None"``
        - test run succeeded for both perm and noperm samples

- rerun masking using snakemake-converted TIF images
    - conda env: ``env``
    - scripts:
        - ``scripts/individual/segmentation_perm_1000_adaptive.Rmd``
        - ``scripts/individual/segmentation_perm_500_adaptive.Rmd``
        - ``scripts/individual/segmentation_noperm_1000_adaptive.Rmd``
        - ``scripts/individual/segmentation_noperm_500_adaptive.Rmd``


2025-08-27
----------

@Mira0507

- Snakemake DAG added
    .. code-block:: bash

        $ cd scripts/snakemake
        $ snakemake --dag --profile none | dot -Tpng > dag.png
        $ mv dag.png config/.

- validate the effect of adaptive equalization
    - conda env: ``env``
    - script: ``scripts/individual/segmentation_perm_1000_adaptive_eq.Rmd``
    - notes
        - disabling watershed segmentation with ``sq.im.segment`` function did not
          improve in removing noise nor making the binarization more uniform across
          the pixels
        - tried with the Otsu thresholding using ``scikit-image`` package. 
          this global thresholding ended up masking the image less uniform 
          compared to adaptive thresholding.
        - merging masked signals 
            - Otsu thresholding without erosion
            - adaptive thresholding with erosion


- run masking without cropping input images (in progress)
    - conda env: ``env``
    - script: ``scripts/individual/segmentation_perm.Rmd``
    - notes:
        - 47% progress for 6 hours
        - need to modularize and parallelize using Snakemake

