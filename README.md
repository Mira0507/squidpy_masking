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

1. **Image Loading**: Load demo images using `squidpy.datasets.visium_fluo_image_crop`.

2. **Smoothing**: Apply [Gaussian smoothing](https://en.wikipedia.org/wiki/Gaussian_blur) 
with `squidpy.im.process` to reduce noise.  

3. **Segmentation**: Segment images using the following approaches
   - [Otsu thresholding](https://en.wikipedia.org/wiki/Otsu's_method)
   - [Watershed segmentation](https://en.wikipedia.org/wiki/Watershed_(image_processing))

4. **Visualization**: Compare pre/post-smoothing and pre/post-segmentation results.  

