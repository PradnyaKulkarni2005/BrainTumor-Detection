# modules/preprocessing.py
import numpy as np
# extract middle slices from 3D MRI volume
def extract_slices(volume: np.ndarray, slice_fraction: float = 0.6):
    """
    Extract the middle portion of an MRI scan (to avoid noisy edges).

    Args:
        volume (np.ndarray): 3D MRI volume (H, W, D)
        slice_fraction (float): % of middle slices to keep (default 60%)

    Returns:
        list of 2D NumPy arrays
    """
    # determine slice indices
    depth = volume.shape[-1]
    start = int(depth * (1 - slice_fraction) / 2)
    end = int(depth * (1 + slice_fraction) / 2)
    # slice the volume
    slices = [volume[:, :, i] for i in range(start, end)]
    return slices
