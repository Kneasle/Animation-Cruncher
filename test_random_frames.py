import animation_cruncher as ac
import os

root_dir = "C:\\Users\\kneas\\Documents\\Pictures\\Logos & Backdrops\\A Collective Bicycle Logo\\Over-sampled Renders"

path = os.path.join (root_dir, "Random Frames")

in_path = path + " In"
out_path = path + " Out"

cruncher = ac.Cruncher (in_path, out_path, 1)

cruncher.Crunch ()
