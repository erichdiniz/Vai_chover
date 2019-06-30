import netCDF4
import xarray
import matplotlib.mlab as plt
import os
import ipaddress
import pandas as pd



def get_rain_data(lat, lon):
    print(os.getcwd())
    xr = xarray.open_dataset('Weather/MAIR_19-02-19.nc')
    xr_sel = xr.sel(lat=lat, lon=lon, method='nearest')
    df = xr_sel['data'].to_dataframe()['data']
    df.index = df.index.strftime('%Y-%m-%d').to_list()
    D = df.to_dict()
    plt.bar(range(len(D)), list(D.values()), align='center')
    plt.xticks(range(len(D)), list(D.keys()))
    # # for python 2.x:
    # plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
    # plt.xticks(range(len(D)), D.keys())  # in python 2.x
    return plt.show()


#xarray.inter method linear cube


def get_rain_quantity(lat, lon):
    xr = xarray.open_dataset('Weather/MAIR_19-01-13.nc')
    data = xr['data'].sel(lat=lat, lon=lon, method='nearest')
    df = data.to_dataframe()
    df.index = df.index.strftime('%Y-%m-%d').to_list()
    d = df.loc[:,'data'].to_dict()
    return d


def get_rain_interpolation(lat, lon):
    xr = xarray.open_dataset('Weather/MAIR_19-02-19.nc')
    data = xr['data'].interp(lat=lat, lon=lon, method='linear')
    df = data.to_dataframe()
    df.index = df.index.strftime('%Y-%m-%d').to_list()
    d = df.loc[:,'data'].to_dict()
    return d


def get_ip_from_range():
    start_ip = ipaddress.IPv4Address('45.4.20.0')
    end_ip = ipaddress.IPv4Address('45.4.23.255')
    for ip_int in range(int(start_ip), int(end_ip)):
        print(ipaddress.IPv4Address(ip_int))


def noise_reduction():
    xr = xarray.open_dataset('Weather/MAIR_19-01-13.nc')
    xr2 = xr.values()




# print (5,126**28)
#
# print(5,126**5007)
# 564.621.236.424.054.294.758.255.082.478.017.602.525.396.733.389.099.421.925.376 kg
# 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000
