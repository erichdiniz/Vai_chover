import netCDF4
import xarray
import matplotlib.mlab as plt
import os
import ipaddress
import pandas as pd
xr = xarray.open_dataset('/Users/erichdiniz/Desktop/Repositorio/VaiChover/flask_back-end/Weather/MAIR_19-02-19.nc')

# print(xr)


def get_rain_data(lat, lon):
    print(os.getcwd())
    xr = xarray.open_dataset('Weather/MAIR_19-02-19.nc')
    xr_sel = xr.sel(lat=lat, lon=lon, method='nearest')
    # df = xr_sel['data'].to_dataframe()['data']
    # df.index = df.index.strftime('%Y-%m-%d').to_list()
    xr_sel.plot()


    # # for python 2.x:
    # plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
    # plt.xticks(range(len(D)), D.keys())  # in python 2.x


    # plt.show()

get_rain_data(-23, -46)