# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 08:55:23 2021

@author: abc
"""

"""

BLOCK MATCHING 3D FILTERING (BM3D) FOR DENOISING


"""

import cv2
from skimage import io, img_as_float
import bm3d

#read our image and convert it into floating point value
noisy_img = img_as_float(io.imread("BSE_25sigma_noisy.jpg", as_gray=True))

#define BM3D fillter
BM3D_denoised = bm3d.bm3d(noisy_img, sigma_psd = 0.2, stage_arg=bm3d.BM3DStages.ALL_STAGES)

#show our images
cv2.imshow("Original image", noisy_img)
cv2.imshow("Denoised image using BM3D filter", BM3D_denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()


