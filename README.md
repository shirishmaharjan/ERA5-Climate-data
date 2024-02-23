# ERA5-Climate-data
Python code to download ERA5 data. Original (1979-2022). Later adding 2023. 

# Created a grid shape file of 1342 unique values of Nepal. 

- Nepal is divided into 1342 grids and each grid contains unique id.
- We need to calculate for each 1342 grids. 

# Steps to download ERA5 data. 

- SJ has created a code that will download ERA5 data from https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_HOURLY#description from 1979-2022
- Python file : ERA5_Data_Download_1979_2022.py

# Step to download of specific year (2023)

- Change date in code respectively.
- era5_dataset = ee.ImageCollection('ECMWF/ERA5_LAND/HOURLY').filterDate('2023-01-01', '2024-01-01')
- output_path = 'ERA5_2023' (Make your own directory name ERA5_2023 and output will be in that folder.
- Install all the necesary libraries and geemap will take some time.
- Change for year in range(2023, 2024):
- Python File : ERA5_Data_Download.py
