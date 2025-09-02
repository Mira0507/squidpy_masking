# squidpy_masking

This repository is designed to demonstrate fluorescence image masking
for Visium analysis using the 
[squidpy (Palla, Spitzer et al., 2022)](https://www.nature.com/articles/s41592-021-01358-2) 
package in Python.

## Package installation

Packages were installed using the [Conda](https://docs.conda.io/en/latest/) package manager.
For more detailed information about packages and versions, refer to 
the `env.archived.yaml` file.

## Workflow

1. **Image Loading**

- Scenario 1: Loading demo images using `squidpy.datasets.visium_fluo_image_crop`.
- Scenario 2: Loading `tif` and `tiff` images converted from the `vsi` format, 
taken using the Olympus VS200 scanner.

2. **Smoothing**: Apply [Gaussian smoothing](https://en.wikipedia.org/wiki/Gaussian_blur) 
with `squidpy.im.process` to reduce noise.  

3. **Segmentation**: Segment images using the following approaches
   - [Otsu thresholding](https://en.wikipedia.org/wiki/Otsu's_method)
   - [Watershed segmentation](https://en.wikipedia.org/wiki/Watershed_(image_processing))
   - [Adaptive thresholding](https://scikit-image.org/docs/0.25.x/auto_examples/applications/plot_thresholding_guide.html#local-thresholding)

4. (Optional) **Additional processing**:
   - [Adaptive equalization](https://en.wikipedia.org/wiki/Adaptive_histogram_equalization)
   - [Erosion](https://en.wikipedia.org/wiki/Erosion_(morphology))

5. **Visualization**: Compare pre/post-smoothing and pre/post-segmentation results.  

6. **Channel merge**: Merge channels of interest


## Scripts

### Individual demo scripts

- `scripts/individual/segmentation.Rmd`: Masking demo fluorescence images from 
`squidpy.datasets.visium_fluo_image_crop`.
- `scripts/individual/image_conversion_<sample>.Rmd`: Converting user images from `vsi` to `tif` 
using the `bftools` package.
- `scripts/individual/segmentation_<sample>_<dimension>.Rmd`: masking `tif` fluorescence images 
using Squidpy’s default segmentation workflow (Otsu thresholding and Watershed 
segmentation) with different cropping dimensions
- `scripts/individual/segmentation_<sample>_dimension>_adaptive.Rmd`: masking `tif` fluorescence
images using adaptive thresholding and erosion with different cropping dimensions
- `scripts/individual/segmentation_<sample>_dimension>_adaptive_eq.Rmd`: input image 
preprocessed with adaptive equalization before smoothing

### Snakemake converting `vsi` to `tif`

- `scripts/snakemake/Snakefile`: Running Snakemake pipeline to convert `vsi` to `tif`
- `scripts/snakemake/config/config.yaml`: Configuring Snakemake
- `scripts/snakemake/config/sampletable.txt`: 
Specifying sample names and corresponding input image paths
- `scripts/snakemake/image_conversion.Rmd`: 
Wrapper script running `bftools` for image conversion
- `scripts/snakemake/build_imagecontainer.Rmd`: 
Wrapper script building an `ImageConainer` object of Squidpy from the `tif` image

![Workflow](scripts/snakemake/config/dag.png)
