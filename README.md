# Surfs Up Analysis

## Overview
The purpose of the Surfs Up Analysis was to analyze weather data for the island of Oahu in the [`hawaii.sqlite` database](https://github.com/fobordo/surfs_up/blob/main/hawaii.sqlite) to determine the feasibility of opening a "Surf n Shake" shop selling ice cream and surfboards to tourists. The goal of the analysis was to provide a strong business case to Investor W.Avy to invest in the shop by demonstrating that the weather in Oahu would be ideal for this business venture.

## Results
After filtering the Measurement table in the `hawaii.sqlite` database on temperatures for the months of June and December, the following statistics were calculated:

![June Temps Statistics](/Resources/june_temps_statistics.png)

![Dec Temps Statistics](/Resources/dec_temps_statistics.png)

The three key differences in weather between June and December were as follows:
* The average temperature in June was 74.9 degrees, while the average temperature in December was 71.04 degrees. 
* The minimum temperature in June was 64 degrees, while the minimum temperature in December was 56 degrees. 
* The maximum temperature in June was 85 degrees, while the maximum temperature in December was 83 degrees.

## Summary
The difference in average temperature between June and December showed that it is slightly less warm in Oahu in December, but only by less than 4 degrees. The difference in minimum temperature between June and December showed that the lowest temperature in December can drop 8 degrees lower than the lowest temperature in June. This is a significant difference to be considered in the ice cream/surfboard selling business, as people may not want to purchase ice cream or surfboards when it is too cold. However, it is likely that the minimum temperatures were exhibited at night, after selling hours. On the other hand, the maximum temperature between June and December differed by only 2 degrees. Since the maximum temperature would have occurred during the daytime, this suggests that the weather is likely quite consistent during the day during both months in Oahu.

To gather more weather data for June and December, the following two additional queries can be performed:
1. Calculate the summary statistics on precipitation data for the month of June in Oahu
2. Calculate the summary statistics on precipitation data for the month of December in Oahu