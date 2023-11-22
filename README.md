## Introduction

This assignment aims to demonstrate proficiency in working with PySpark to analyze earthquake data. It involves reading data from a CSV file, transforming it, and performing various data analysis tasks. This readme file also answers the questions asked in the assignment pdf. 

## Requirements

- PySpark version 3.0 or later
- A local MySQL database

## Installation

### PySpark Installation

1. Install Python and Pip.
2. Install Python libraries such as PySpark, PyMySQL, Pandas and Python-dotenv using Pip:
   ```bash
   pip install pyspark pymysql pandas python-dotenv

   ```

### MySQL Installation

1. Download and install MySQL Community Server.
2. Create a MySQL database named `earthquake_db`.

## Execution

1. Clone the project repository to your local machine.
2. Navigate to the project directory.
3. Update the `.env` file with your credentials for MySQL DB.
4. Execute the `setup_script.py` script using the command: `python setup_script.py`
5. Execute the `earthquake_analysis.ipynb` python notebook using the command.

## Data Analysis

The script performs the following data analysis tasks:


### 1. How does the Day of a Week affect the number of earthquakes?
==> Saturday and Wednesday are the days where the earthquake count was highest. 
![plot1](https://github.com/ashty3899/test/assets/67702605/0f6188fe-c218-4664-94c1-4803284019e0)

### 2. What is the relation between Day of the month and Number of earthquakes that happened in a year?
==> The top 3 days where the number of earthquakes where highest are 11th, 17th, and 23rd having 900, 840, and 831 earthquakes respectively.

![Top N days of the month by earthquake count.](https://github.com/ashty3899/test/assets/67702605/e242ae5e-36ed-4eec-a8d3-c323222de495)
![Plot days of the month with the count of earthquakes each day.](https://github.com/ashty3899/test/assets/67702605/5fe4eabd-845f-4bf2-b96b-a80f3f2a6a47)

### 3. What does the average frequency of earthquakes in a month from the year 1965 to 2016 tell us?
==> It tells us that March and August have 40.46 and 38.46 as the highest avg of earthquakes by month over the years and June and February have 34.75 and 35.01 as the lowest avg of earthquakes by month over the years.
![Avg Earthquake by month over the years](https://github.com/ashty3899/test/assets/67702605/3a230e4d-4e65-4392-98d1-019c416e0973)

### 4. What is the relation between the Year and Number of earthquakes that happened in that year?
==> From the below chart we can say that the number of earthquakes has increased over the years.
![Year-wise earthquake count](https://github.com/ashty3899/test/assets/67702605/d1c234fb-e408-4af6-a6a0-e5e9abbf4dc2)

### 5. How has the earthquake magnitude on average been varied over the years?
==> The earthquake magnitude on average has varied over the years by `0.0293%`.
Below is the chart showing the percentage change of the magnitude compared to the previous year.
![magnitude change over the years](https://github.com/ashty3899/test/assets/67702605/0b455275-4b75-4e56-8906-2669fc462407)

### 6. How does year impact the standard deviation of the earthquakes?
==> It doesn't have much impact on the standard deviation of the earthquakes. It's been in the range of `0.40 to 0.45` . 
![standard deviation over years](https://github.com/ashty3899/test/assets/67702605/b475c071-53a6-4014-ba32-afaf4759f586)

### 7. Does geographic location have anything to do with earthquakes?
==> Yes, It surely does. I have plotted the latitude and longitude scatter plot. It shows that near the longitude of `130 to 160` and `-60 to -70` there are lots of dots which means the earthquakes were more frequent than in other places.
![Scatter plot by longitude and latitude](https://github.com/ashty3899/test/assets/67702605/6b670f6f-b779-46ca-b381-e204ef9da9f7)

### 8. Where do earthquakes occur very frequently?
==> We don't have any column where we can the geo location names. However, I did try to use the longitude and latitude and plotted on the world map using the Databricks Visualization feature. By looking in the map we can say that major earthquakes happened in the area of Japan, Middle Eastern Countries, the Indonesian Islands, and Central America with Columbia.
![image](https://github.com/ashty3899/test/assets/67702605/38aeec7b-2608-4090-b1b0-3f44a1887e67)

### 9. What is the relation between Magnitude, Magnitude Type, Status, and Root Mean Square of the earthquakes?
==> The average magnitude of different types of magnitudes is similar in the range of 5.8 ± 0.2. Only MH has a 6.5 magnitude.
![Avg magnitude by magnitude types.](https://github.com/ashty3899/test/assets/67702605/c4348d93-aae7-4655-afee-71d5c110819a)
The table below shows that where the status is Automatic the  Root Mean Square is `null`.
![Avg root mean square by status.](https://github.com/ashty3899/test/assets/67702605/957415af-3d28-4c12-bd71-0a8c14bc4d27)




## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashishyadav38/)

