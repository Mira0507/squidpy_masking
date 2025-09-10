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



2025-08-28
----------

@Mira0507

- bugfix
    - conda env: ``env``
    - scripts: 
        - ``scripts/individual/segmentation_perm_1000_adaptive_eq.Rmd``
        - ``scripts/individual/segmentation_noperm_1000_adaptive_eq.Rmd``
        - ``scripts/individual/segmentation_perm_500_adaptive_eq.Rmd``
        - ``scripts/individual/segmentation_noperm_500_adaptive_eq.Rmd``
    - notes:
        - bugfix to the `display_merge` function
        - binarized IF signal was less uniform across the pixels with
          Otsu thresholding regardless of the utilization of scikit-image
          package
        - adaptive thresholding captured IF signal more uniformly across
          the pixels


2025-08-29
----------

@Mira0507

- generate masking data for collaborator's poster
    - conda env: ``env``
    - script: ``scripts/presentation/08292025/segmentation_noperm_crop_adaptive.Rmd``
    - notes
        - the coordinates of collaborator's crop identified manually using QuPath 
          based on the following conversion: N um in QuPath x 3.25 = M pixels 
          in Squidpy
        - images were processed as is and rotated (90 degrees, clockwise)
          only for printing masked data so masked images are aligned with those in 
          collaborator's poster


- update Snakemake pipeline (in progress)
    - conda env: ``env``
    - scripts added
        - ``scripts/snakemake/build_imagecontainer.Rmd``
    - scripts updated
        - ``scripts/snakemake/config/config.yaml``
        - ``scripts/snakemake/Snakefile``
    - notes
        - rule ``convert`` completed
        - rule ``build_imagecontainer`` in progress


2025-09-02
----------

@Mira0507

- update Snakemake pipeline (in progress)
    - conda env: ``env``
    - scripts
        - ``scripts/snakemake/Snakefile``
    - notes
        - rule ``build_imagecontainer`` added
        - duplicated chunk names corrected 
          in the ``scripts/snakemake/build_imagecontainer.Rmd``



2025-09-03
----------

@Mira0507

- update Snakemake pipeline (in progress)
    - conda env: ``env``
    - scripts
        - ``scripts/snakemake/Snakefile``
    - notes
        - ``resources`` directive update to the ``build_imagecontainer`` rule
        - ``scripts/snakemake/build_imagecontainer.Rmd`` optimization in progress
        - ``scripts/snakemake/smooth.Rmd`` added

- test processing uncropped image without Snakefile
    - conda env: ``env``
    - script: ``script/individual/segmentation_perm_adaptive.Rmd``

    .. code-block:: python

        img = sq.im.ImageContainer('path/to/converted.ome.tif', layer=lyr)

    - notes:
        - method to load input image changed to use squidpy as-is
        - added subchunkifying to simplify iterative visualization 
        - improved smoothing speed by passing the following arguments into 
          the ``sq.im.process`` function:
            - ``chunks="auto"``
            - ``lazy=True``


- ``README.md`` updated


2025-09-04
----------

@Mira0507

- build Snakemake pipeline
    - updates to ``script/snakemake/build_imagecontainer.Rmd``
        - strings specified by ``crop_height``, ``crop_width``,
          ``crop_size``, ``crop_scale`` converted into *float*
        - convert 1-indexing into 0-indexing when iteratively 
          printing images
        - ``ImageContainer`` obj updated to use Dask 
          when loading input images

        .. code-block:: python

            img = sq.im.ImageContainer(input_image, layer=lyr, lazy=True, chunks='auto')




2025-09-05
----------

@Mira0507

- build Snakemake pipeline
    - links to output image file paths corrected in 
      ``script/snakemake/build_imagecontainer.Rmd``
    - input/output paths to ``zarr`` file updated in ``Snakefile. This requires
      to be ``directory(<zarr>)``.
    - wrapper script for rule ``smooth`` update in progress
    - rule ``squidpy_segmentation`` added to ``Snakefile``, in progress
    - ``scripts/snakemake/config/helpers.R`` added

- batch submission bug with Snakemake v8

    - dry-run shows ``threads`` set to 6

    .. code-block:: bash

        $ snakemake -n --profile path/to/snakemake_profile_v8

        host: cn2294
        Building DAG of jobs...
        Job stats:
        job        count
        -------  -------
        all            1
        convert        2
        total          3


        [Fri Sep  5 10:30:38 2025]
        rule convert:
            input: ../images/input/Perm/Image_168.vsi, image_conversion.Rmd
            output: ../images/converted_test/perm/converted.ome.tif, ../images/converted_test/perm/image_conversion.html
            jobid: 1
            reason: Missing output files: ../images/converted_test/perm/converted.ome.tif
            wildcards: outputdir=../images/converted_test, name=perm
            threads: 6
            resources: tmpdir=<TBD>, mem_mb=40960, mem_mib=39063, disk_mb=20480, disk_mib=19532, runtime=360


        [Fri Sep  5 10:30:38 2025]
        rule convert:
            input: ../images/input/NoPerm/Image_169.vsi, image_conversion.Rmd
            output: ../images/converted_test/noperm/converted.ome.tif, ../images/converted_test/noperm/image_conversion.html
            jobid: 2
            reason: Missing output files: ../images/converted_test/noperm/converted.ome.tif
            wildcards: outputdir=../images/converted_test, name=noperm
            threads: 6
            resources: tmpdir=<TBD>, mem_mb=40960, mem_mib=39063, disk_mb=20480, disk_mib=19532, runtime=360


        [Fri Sep  5 10:30:38 2025]
        rule all:
            input: ../images/converted_test/perm/converted.ome.tif, ../images/converted_test/noperm/converted.ome.tif
            jobid: 0
            reason: Input files updated by another job: ../images/converted_test/perm/converted.ome.tif, ../images/converted_test/noperm/converted.ome.tif
            resources: tmpdir=<TBD>

        Job stats:
        job        count
        -------  -------
        all            1
        convert        2
        total          3

        Reasons:
            (check individual jobs above for details)
            input files updated by another job:
                all
            output files have to be generated:
                convert

        This was a dry-run (flag -n). The order of jobs does not reflect the order of execution.

    - batch submissions allocate only 2 CPUs

    .. code-block:: bash

        User   JobId     JobName     Part         St  Reason  Runtime     Walltime     Nodes  CPUs   Memory  Dependency  Nodelist
        ===========================================================================================================================
        user  66730066  s.convert.  norm         R                 1:48      6:00:00      1      2   40 GB              cn0054
        user  66730075  s.convert.  norm         R                 1:48      6:00:00      1      2   40 GB              cn4319

    - notes
        - snakemake versions

        .. code-block:: bash

            $ cat env.archived.yaml | grep snakemake
              - snakemake=8.30.0=hdfd78af_0
              - snakemake-executor-plugin-cluster-generic=1.0.9=pyhdfd78af_0
              - snakemake-interface-common=1.21.0=pyhdfd78af_0
              - snakemake-interface-executor-plugins=9.3.9=pyhdfd78af_0
              - snakemake-interface-report-plugins=1.2.0=pyhdfd78af_0
              - snakemake-interface-storage-plugins=3.5.0=pyhdfd78af_0
              - snakemake-minimal=8.30.0=pyhdfd78af_0

        - snakemake profile: https://github.com/NIH-HPC/snakemake_profile/tree/snakemake8
        - this issue is not seen when running Snakemake v7.7.0 with the old snakemake 
          profile (https://github.com/NIH-HPC/snakemake_profile/tree/main). 
        - this issue is not seen when running on an interactive node
        - it appears that this issue is related to Snakemake v8 or snakemake_profile_v8. 
          I'm reaching out to HPC.
        - figured out that updating Snakemake to newer versions can resolve this 
          issue. reinstalling Snakemake v8.8.0 resolved it.

- conda env updates: ``requirements.txt`` and ``env.archived.yaml`` updated to fix
  Snakemake version to v8.8.0


2025-09-08
----------

@Mira0507

- build Snakemake pipeline
    - conda env: ``env``
    - updates
        - rule ``squidpy_segmentation`` completed
        - ``scripts/snakemake/squidpy_segmentation`` bugfix
            - ``"None"`` converted into ``None``
            - dask arrays across the IF channels, generated by squidpy segmentation,
              were stacked into a single layer labeled *"image_sqseg"*, instead of 
              remaining as individual layers per channel
        - rule ``adaptive_thresholding`` in progress 
        - ``scripts/snakemake/adaptive_thresholding.Rmd`` draft added


2025-09-09
----------

@Mira0507

- build singularity container from conda env
    - reference defs: 
        - https://github.com/NIH-CARD/scMAVERICS/blob/162a0fe615589069051fa38a0081f90ecd4cbf33/envs/single_cell_cpu.def
        - https://github.com/NIH-CARD/scVIRGILS/blob/main/single_cell_basic.def
    - documentation: 
      https://github.com/NIH-CARD/card-unified-workflow/blob/main/anaconda2singularity.md#use-sylabs-remotely-to-build-image
    - definition file: ``squidpy_masking.def``
    - image file: ``squidpy_masking.sif``
    - pushed to https://quay.io/repository/miradt/squidpy_masking
    - how to pull

    .. code-block::

        # Load apptainer
        module load apptainer

        # Pull the container
        apptainer pull oras://quay.io/miradt/squidpy_masking

- build Snakemake pipeline
    - conda env: ``env``
    - updates
        - output of rule ``adaptive_thresholding`` added to rule ``all``
        - ``scripts/snakemake/adaptive_thresholding.Rmd`` in progress


2025-09-10
----------

@Mira0507

- build Snakemake pipeline
    - conda env: ``env``
    - updates
        - ``offset`` and ``block_size`` parameters added to rule ``adaptive_thresholding``
        - bugfix to rule ``squidpy_segmentation`` in progress
            - fluorescence intensities between adjacent chunks are discontinuous 
            - seems to be related to using dask array

- exploring the intensity distribution over squidpy-segmented arrays
    - conda env: ``env``
    - script: ``scripts/individual/segmentation_perm_500.Rmd``
    - notes:
        - A question raised: does squidpy's segmentation results in binarized images?
        - TODOs
            - plot intensities across the pixels and channels before segmentation
            - plot intensities across the pixels and channels after segmentation
