# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:44:18 2015

@author: tedscott
"""
import matplotlib
import pandas as pd

## Set up the two plots. blue is the human and red veloc.
fh=series(color=color.blue)
fv=series(color=color.red)

##### set up my initial conditions
xv=-40 #this is the initial location of velociraptor (you can change)
xh=0 #location of human
av=4 #acceleration of velociraptor (you can change)
ah=3 #accel of human (can change)
vvmax=25 #maximum velocity of the velociraptor (change)
vhmax=6 #max velocity of human (change)
vh=0 #starting velocity of human
vv=0 #starting velocity of velociraptor
t=0 #starting time
dt=0.1 #time step (you can play with this)

#this is the loop. It runs until the velociraptor
#catches up to the human
while xv<=xh:
  #first check if the human is at max v
  if vh>=vhmax:
    ah=0 #if yes, set accel to zero
  #check if velociraptor is at max speed
  if vv>=vvmax:
    av=0 #if yes, set accel to zero
    
  #calc new human velocity after time interval
  vh=vh+ah*dt
  
  #calc new velociraptor velocity
  vv=vv+av*dt
  
  #calc new positions
  xh=xh+vh*dt
  xv=xv+vv*dt
  
  #update time
  t=t+dt
  
  #create the graph
  fh.plot(t,xh)
  fv.plot(t,xv)

#once the loop is finished, print the final location
print(xh)