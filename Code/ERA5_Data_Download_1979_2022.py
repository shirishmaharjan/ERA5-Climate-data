import ee
import geemap
import multiprocessing
import logging
import time
from datetime import datetime
import os
from colorama import Fore, Back
from retry import retry

ee.Initialize(opt_url='https://earthengine-highvolume.googleapis.com')
start_time = time.time()
output_path = 'grid_output_before_1980'
points_fc = ee.FeatureCollection('projects/ee-joshisur231/assets/climatic_data_points')

print(Fore.BLUE + f'Started at..........{datetime.fromtimestamp(start_time)}')


era5_dataset = ee.ImageCollection('ECMWF/ERA5_LAND/HOURLY').filterDate('1950-01-01', '2023-01-01')

@retry(tries=10, delay=1, backoff=2)
def process_date(date_chunk):
    for myDate in date_chunk:
        try:
            nepal_date = str(myDate.format('YYYYMMdd', timeZone='Asia/Thimphu').getInfo())
            print(Back.BLUE + f"..........Started for {nepal_date}..........")
            filtered_date_dataset = era5_dataset.filterDate(myDate, myDate.advance(1, 'day'))
            tempMin = filtered_date_dataset.select('temperature_2m').reduce(ee.Reducer.min()).rename('tempMin')
            tempMax = filtered_date_dataset.select('temperature_2m').reduce(ee.Reducer.max()).rename('tempMax')
            precTot = filtered_date_dataset.select('total_precipitation_hourly').reduce(ee.Reducer.sum()).rename('precTot')

            multiband_image = tempMin.addBands(tempMax).addBands(precTot)

            geemap.extract_values_to_points(in_fc=points_fc, image=multiband_image, out_fc= os.path.join(output_path, nepal_date+'.csv'), scale=11132)
            print(Back.GREEN + f"..........Finished for {nepal_date}..........")
        
        except Exception as e:
            print(Back.RED + f"..........Failed for {nepal_date}..........")

            with open('error_log.txt', 'a') as error_log:
                error_log.write(f"Failed for {nepal_date}: {str(e)}\n")

if __name__ == "__main__":
    logging.basicConfig()
    results = []

    num_processes = multiprocessing.cpu_count()
    leap_years = [
        1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 
        1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 
        1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

    dateList = []
    for year in range(1979, 2022):
        for month in range(1, 13):
            if month in [4, 6, 9, 11]:
                max_day = 30
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                max_day = 31
            elif month == 2 and year in leap_years:
                max_day = 29
            else:
                max_day = 28
            
            for day in range(1, max_day + 1):
                current_date = ee.Date.fromYMD(year, month, day).advance(-6, 'hour')
                dateList.append(current_date)
    
    chunk_size = len(dateList) // num_processes

    date_chunks = [dateList[i:i + chunk_size] for i in range(0, len(dateList), chunk_size)]

    with multiprocessing.Pool(processes=num_processes) as pool:

        pool.map(process_date, date_chunks)
    
    end_time = time.time()
    print(Back.GREEN + f'Completed.......{datetime.fromtimestamp(end_time)}|||||Completed in {end_time-start_time} sec')
    
