# ERA5-Climate-data
Python code to download ERA5 data. Original (1979-2022). Later adding 2023. 

- Python code is used to download ERA5 download [ERA5_Data_Download.py]
- R code is used to re format and re order the data. [ERA5_Hourly_Nepal.R]

# Created a grid shape file of 1342 unique values of Nepal. 

- Nepal is divided into 1342 grids and each grid contains unique id.
- We need to calculate for each 1342 grids. 

# Steps to download ERA5 data. 

- SJ has created a code that will download ERA5 data from https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_HOURLY#description from 1979-2022
- Python file : ERA5_Data_Download_1979_2022.py

# Step to download of specific year (2023)

- Change date in code respectively.
- ee.authenticate(), We need to copy token from gmail and paste in vs code initially. 
- era5_dataset = ee.ImageCollection('ECMWF/ERA5_LAND/HOURLY').filterDate('2023-01-01', '2024-01-01')
- output_path = 'ERA5_2023' (Make your own directory name ERA5_2023 and output will be in that folder.
- Install all the necesary libraries and geemap will take some time.
- Change for year in range(2023, 2024):
- Python File : ERA5_Data_Download.py

# Data Analysis of the year 2023 (27.02.2023)

- Used ERA5_2023_analysis.ipynb to merge 365 csv files from "C:\GIIS\ERA 5 Hourly 2023\Python code\Code\ERA5_2023" folder to make it one single csv format.
- Then used same code to add new columns year, month and day to make it according to csv file names like 20230101 would be year = 2023, month = 01 and day = 01.
- Used pivot table to make it in correct format.
- Added 2023 data to "E:\GIIS\ERA5 Hourly Data\Data\Orignal Data (First)\tempMax_1980_2022.csv" location to tempMax_1980_2022, tempMax_1980_2022 and precTot_1980_2022 at the end.
- Now we have to rename tempMax_1980_2022 to tempMax_1980_2023 and tempMin_1980_2023 to tempMin_1980_2023 and precTot_1980_2022 to precTot_1980_2023
