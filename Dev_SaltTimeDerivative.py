# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:14:53 2020

@author: Jasen
"""
import os
os.chdir('/Users/Jasen/Documents/GitHub/Exact_Budget/')

from netCDF4 import Dataset as nc4

#files
FilePath = '/home/cae/runs/jasen/wc15.a01.b03.hourlywindWT.windmcurrent.diags/out/'
HistFile = FilePath + 'ocean_hist_2014_0006.nc'
AvgFile = FilePath + 'ocean_avg_2014_0006.nc'
DiagFile = FilePath + 'ocean_dia_2014_0006.nc'
GrdFile = '/home/ablowe/runs/ncfiles/grids/wc15.a01.b03_grd.nc'

#????
#to conserve memory should I define indices of desired CV instead of loading
#the full field, then applying mask?
#Another option would be to load the full field, apply mask, and discard full field
#????

#load salt_rate from diagnostic file
Diag = nc4(DiagFile, 'r')
salt_rate = Diag.variables['salt_rate'][:]

#from average file, load salt and vertical thickness
Avg = nc4(AvgFile, 'r')
salt = Avg.variables['salt'][:]

#vertical thickness from depth of w points
##need to edit set_depth to include Vstretching = 4 (sperical)
##then compute diff depth at w points

