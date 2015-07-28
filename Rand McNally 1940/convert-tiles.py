from glob import glob
from os.path import join, split, splitext
from subprocess import call

for zoomdir in glob('tiles/?'):
    _, zoom = split(zoomdir)
    
    for png_path in glob(join(zoomdir, '*/*.png')):
        basename, ext = splitext(png_path)
        dirname, y = split(basename)
        
        # invert y-axis
        new_y = (2**int(zoom) - 1) - int(y)
        jpg_path = '{dirname}/{new_y}.jpg'.format(**locals())
        
        print png_path, '-->', jpg_path
        call(('convert', png_path, jpg_path))
