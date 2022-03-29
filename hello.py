#!/usr/bin/python
import subprocess
from paraview import simple

print(help(simple))

print("Hello, World!");

'''
nrrdFilepath="/tmp/test";
resampledFilePath="/tmp/test.down";
subprocess.call(['unu', 'resample', '-i', nrrdFilepath, '-o', resampledFilePath, '-s', 'x0.5', 'x0.5', 'x0.5'])
'''