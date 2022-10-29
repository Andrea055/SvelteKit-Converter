import glob
import os
import shutil

files = glob.glob("*")

for f in files:
    if(f != "update.py"):
        os.mkdir(f.replace(".svelte", ""))
        shutil.move(f, f.replace(".svelte", "") + "/+page.svelte")
