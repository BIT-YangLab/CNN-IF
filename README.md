# Interpretable_Encoding_model_Framework
Code of article "A Convolutional Neural Network Interpretable Framework for Human Ventral Visual Pathway Representation"
# Introduction
We propose a convolutional neural network interpretable framework (CNN-IF) aimed at providing a transparent interpretable encoding model for the ventral visual pathway.

The method is built on the framework of the feature-weighted receptive field (fwrf), an encoding model designed to balance expressiveness, interpretability, and scalability, which can encode the voxel-wise response of voxels in the human brain.

The weighted matrix is extracted from the trained encoding model to convert the layer-by-layer feature maps into voxel maps, so as to conduct the layer-wise Network Dissection along the ventral visual pathway.
# Download
* Clone the code of Network Dissection Lite from GitHub
```
    git clone https://github.com/CSAILVision/NetDissect-Lite
    cd NetDissect-Lite
```
* Acquire the NSD data for the encoding model from：
```
    http://naturalscenesdataset.org
```
