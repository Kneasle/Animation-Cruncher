import animation_cruncher as ac
import os

root_dir = "C:\\Users\\kneas\\Documents\\Pictures\\Logos & Backdrops\\A Collective Bicycle Logo\\Over-sampled Renders"
dirs = ["Blob", "Fade Out", "Text", "Wheels Anim"]

for i in dirs:
    path = os.path.join (root_dir, i)

    in_path = path + " In"
    out_path = path + " Out"

    cruncher = ac.Cruncher (in_path, out_path)

    cruncher.Crunch ()


