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
![earthquakes by day of the week](https://github.com/ashty3899/earthquake_analysis/assets/67702605/7b0cc9a4-f2ed-467c-94cc-57e35370c025)

### 2. What is the relation between Day of the month and Number of earthquakes that happened in a year?
==> The top 3 days where the number of earthquakes where highest are 11th, 17th, and 23rd having 900, 840, and 831 earthquakes respectively.

![Top N days of the month by earthquake count.](https://github.com/ashty3899/earthquake_analysis/assets/67702605/26c8927b-e159-4aa0-b02d-1c5f42ed09b0)
![Plot days of the month with the count of earthquakes each day.](https://github.com/ashty3899/earthquake_analysis/assets/67702605/ac5eb5a7-9f6c-4b6b-8b28-42e35b6f734d)


### 3. What does the average frequency of earthquakes in a month from the year 1965 to 2016 tell us?
==> It tells us that March and August have 40.46 and 38.46 as the highest avg of earthquakes by month over the years and June and February have 34.75 and 35.01 as the lowest avg of earthquakes by month over the years.
![Avg Earthquake by month over the years](https://github.com/ashty3899/earthquake_analysis/assets/67702605/ee11e0f6-5c89-4690-86eb-d3c7ac4acba1)

### 4. What is the relation between the Year and Number of earthquakes that happened in that year?
==> From the below chart we can say that the number of earthquakes has increased over the years.
![Year-wise earthquake count](https://github.com/ashty3899/earthquake_analysis/assets/67702605/6d82826d-f049-4929-a8eb-17c9bd4e241e)

### 5. How has the earthquake magnitude on average been varied over the years?
==> The earthquake magnitude on average has varied over the years by `0.0293%`.
Below is the chart showing the percentage change of the magnitude compared to the previous year.
![magnitude change over the years](https://github.com/ashty3899/earthquake_analysis/assets/67702605/8e937023-78ed-4bf1-bccb-69309915de2d)


### 6. How does year impact the standard deviation of the earthquakes?
==> It doesn't have much impact on the standard deviation of the earthquakes. It's been in the range of `0.40 to 0.45` . 
![standard deviation over years](https://github.com/ashty3899/earthquake_analysis/assets/67702605/27246318-17e0-4e19-9ecc-b0523fae2fca)


### 7. Does geographic location have anything to do with earthquakes?
==> Yes, It surely does. I have plotted the latitude and longitude scatter plot. It shows that near the longitude of `130 to 160` and `-60 to -70` there are lots of dots which means the earthquakes were more frequent than in other places.
![Scatter plot by longitude and latitude](https://github.com/ashty3899/earthquake_analysis/assets/67702605/ff1b6aab-aa5d-4cce-847a-3ee96f8b74e6)


### 8. Where do earthquakes occur very frequently?
==> We don't have any column where we can the geo location names. However, I did try to use the longitude and latitude and plotted on the world map using the Databricks Visualization feature. By looking in the map we can say that major earthquakes happened in the area of Japan, Middle Eastern Countries, the Indonesian Islands, and Central America with Columbia.
![earthquakes on map](https://github.com/ashty3899/earthquake_analysis/assets/67702605/74092c15-d72f-4ad6-8446-b74d6a1ff007)



### 9. What is the relation between Magnitude, Magnitude Type, Status, and Root Mean Square of the earthquakes?
==> The average magnitude of different types of magnitudes is similar in the range of 5.8 ± 0.2. Only MH has a 6.5 magnitude.
![Avg magnitude by magnitude types.](https://github.com/ashty3899/earthquake_analysis/assets/67702605/07cfacb2-6ecf-42a4-922b-a1f5b4c0496d)
The table below shows that where the status is Automatic the  Root Mean Square is `null`.
![Avg root mean square by status.](https://github.com/ashty3899/earthquake_analysis/assets/67702605/ad108fee-9208-47a1-aa6e-0fe8b185baa4)




## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashishyadav38/)

