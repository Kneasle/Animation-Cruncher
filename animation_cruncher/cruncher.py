from .motion_blur_funcs import * 
import os, math
from PIL import Image, ImageChops

class Cruncher:
    def __init__ (self, in_dir, out_dir, reduction_ratio = 4,
                  out_resolution = (1920, 1080), mb_func = MBGaussian):
        self.in_dir = in_dir
        self.out_dir = out_dir
        self.ratio = reduction_ratio
        self.out_resolution = out_resolution
        self.mb_func = mb_func

    def Crunch (self):
        # get input images
        all_files = os.listdir (self.in_dir)

        # group them frame by frame
        groups = [[] for i in range (math.ceil (len (all_files) / self.ratio))]

        for i in range (len (all_files)):
            groups [math.floor (i / self.ratio)].append (all_files [i])

        if not os.path.exists (self.out_dir):
            os.mkdir (self.out_dir)

        # get motion blur function
        for ind, files in enumerate (groups):
            mb_array = GetArray (self.mb_func, len (files))

            final_image = Image.new ("RGBA", self.out_resolution)

            sum_so_far = 0

            for x in range (len (files)):
                image = Image.open (os.path.join (self.in_dir, files [x]))

                image = image.resize (self.out_resolution, Image.BICUBIC)
                
                value = mb_array [x]

                final_image = Image.blend (image, final_image, sum_so_far / (value + sum_so_far))

                sum_so_far += value

            string = "0" * (4 - len (str (ind))) + str (ind)
            final_image.save (os.path.join (self.out_dir, string + ".png"), "png")

            print (string + "/" + str (len (groups)))
