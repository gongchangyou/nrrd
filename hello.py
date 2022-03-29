#!/usr/bin/python
import subprocess
from paraview import simple

print(help(simple))

print("Hello, World!");

'''
nrrdFilepath="/tmp/tracker-extract-files.125";
downsampledFilePath="/tmp/tracker-extract-files.125.down";
subprocess.call(['unu', 'resample', '-i', nrrdFilepath, '-o', downsampledFilePath, '-s', 'x0.5', 'x0.5', 'x0.5'])
'''