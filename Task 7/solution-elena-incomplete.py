from matplotlib import pyplot as plt
import numpy as np

from data import fetch_sdss_filter, fetch_vega_spectrum

fig, ax1 = plt.subplots()

#----------------------------------------------------------------------
# Fetch and plot the Vega spectrum

# The function fetch_vega_spectrum returns a ndarry with the wavelengths and fluxes in Jy
data_Vega = fetch_vega_spectrum('ugriz')

wave_Vega = data_Vega[0] # array of wavelength in angstroms
Fnu_Vega = data_Vega[1] # array of fluxes in Jy

# I normalize the flux dividing it by the maximum (as I see that in the original.pdf 
# figure the maximum is at 1.0)
Fnorm_Vega = Fnu_Vega/max(Fnu_Vega)

# The function fetch_sdss_filter returns an array of shape (5, Nlam) with the following rows:
    # first row: wavelength in angstroms
    # second row: sensitivity to point source, airmass 1.3
    # third row: sensitivity to extended source, airmass 1.3
    # fourth row: sensitivity to extended source, airmass 0.0
    # fifth row: assumed atmospheric extinction, airmass 1.0
#data_filters = 


# Title
plt.title('SDSS Filters and Reference Spectrum')

# I set the limits of the axes
plt.xlim(3000, 11000) #common x axis
plt.xlabel(r'Wavelength ($\AA$)')

#First y axis (left)
ax1.set_ylim(0., 1.) 
ax1.set_ylabel('Normalised flux')
ax1.plot(wave_Vega, Fnorm_Vega, 'k', label='Vega')

#ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis (Matplotlib documentation)
#ax2.set_ylabel('Filter transmission')

plt.legend()


plt.show()
