'''
This code is written on 8 August 2022.
This serves as a template for Fig. 3 in the manuscript submitted.
The exact codes should be on the Workstation computer in quiclab, the access to which was revoked.
Thus it is a template to recreate the same and in no way an exact reproduction of the results.
This is simplified in order to state the essence. 

The code consists of three parts
(a) sampling of the points to generate the profile
(b) Converting to weak value
(c) plotting
'''


# (A)
'''
The first part need data  files that contains, say the coincidence rate as function of detector position. 
Let's say there are r repetitions of the same.
So we have a matrix C with element C[p,r] representing coincidence at position p for the repetition r 
'''
import pandas as pd
import numpy as np


# C = pd.read_csv("THE DATA FILE") 

def sampleProfile(C):
    p, r = np.shape(C)
    gC = [C[np.random.randint(0,r), i] for i in range(p)]
    return np.array(gC)

'''
The above function takes the matrix C and generates a profile by randomly sampling with any repeatition and 
then iterating over the entire profile. 
'''



# (B)

# Finding the centre/centroid


def centroid(x, y):
    return np.sum(x*np.power(y, 1))/np.sum(np.power(y, 1))

# Here x would be the position array and y is the whaat is returned by the sample profile
# Instead of centroid, Fig3 has centre  obtained from gaussian fit, but that can be easily implemented.
# 
#
# 

'''
So basically, now you have center of one recreated gaussian. One needs to repeat that many times, say 10**4 times to get a distribution of centroids/centres
'''

C0 = [centroid(pos, sampleProfile(C)) for i in range(10**4)]


# Here C0 is an example, where the file is for 0 post  selection angle. Similary you would have C45 and C90.

# The weak value is computed as 

wV = (C0-C45) / np.mean(C90-C45)

# Note that the denominator is averaged to prevent skewing

# Now wV is a disstribution of 10**4 centres. We would have two of them , along X and Y. Lets call them wX and wY and last part is plot them.


# C PLOTTING

'''
The plotting consists of three parts, a scatter plot of x and y
histogram of distribution along x and y
The third portion is regarding showing the errors which can be done with patches.
Other decorations like fitting etc can be plotted, but here describing the skeleton.
'''

fig= plt.figure()

gs = fig.add_gridspec(5,5)

px = fig.add_subplot(gs[4:5,:]) # plot x reserves say about 20% for histoggram
py = fig.add_subplot(gs[:,0:1]) # plot y reserves say about 20% for histoggram

pxy = fig.add_subplot(gs[:,:], sharex=px, sharey = py)
# pxy, the scatter plot shares the same axes.


# Histograms
px.hist(wX,orientation = 'vertical')
py.hist(wY,orientation ='horizontal')
pxy.scatter(wX, wY)

# You may draw gaussian fits on both
# Rest are decorations with patches and error bars
