# Electricity consumption #Week 3: Assignment: Electricity Consumption Data Analysis with NumPy Problem Statement You are provided with electricity consumption data (in kWh) for a household measured daily over 4 months (120 days). The daily consumption values range between 200 kWh (minimum) and 600 kWh (maximum). Your task is to simulate the dataset using NumPy and perform an in-depth analysis of the household’s electricity consumption.

# Tasks (Do all 10)

# Generate the Dataset Use numpy.random.randint() to simulate 120 daily consumption values between 200 and 600 kWh. Store the data in a NumPy array called consumption.

# Basic Statistics Calculate the mean, median, minimum, maximum, and standard deviation of daily consumption.

# Identify Extremes Find the day number(s) with the highest and lowest consumption.

# Monthly Splitting Divide the dataset into 4 months (30 days each). Store each month’s data in a separate NumPy array.

# Monthly Analysis For each month: calculate the total consumption and average daily consumption.

# Weekly Analysis Reshape or split the data into weeks of 7 days (ignore the extra 4 days at the end). Compute the weekly totals and weekly averages.

# Overall Consumption Trend Calculate the cumulative consumption across the 120 days. Display the first 10 values of the cumulative sum.

# Anomaly Detection Define anomalies as days where consumption is 2 standard deviations above or below the mean. Identify the day numbers that are anomalies.

