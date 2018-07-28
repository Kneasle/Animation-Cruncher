import PIL
from .motion_blur_funcs import * 

class Cruncher:
    def __init__ (self, in_dir, out_dir, reduction_ratio = 4,
                  out_resolution = (1920, 1080), mb_func = MBGaussian):
        self.in_dir = in_dir
        self.out_dir = out_dir
        self.ratio = reduction_ratio
        self.out_resolution = resolution

    def Crunch (self):
        pass
