
# INFO 7374 - NYC TAXI ANALYSIS WITH WEATHER AND UBER

## Introduction

The New York City Taxi  has released a staggeringly detailed historical dataset covering over 1.1 billionindividual taxi trips in the city from January 2009 through June 2015.As the Data is huge, I have taken data from Jan 2016 to June 2016 for my analysis.Taken as a part of data How much are the earnings by each Taxi Companies , What affects the speed of the Taxi , How weather is related to the rides are the co-relations that you can infer from it .

## Prerequisites

For this analysis, I have used following libraries. You can also get them by using the following simple command. The packages were installed using the following command.

```
pip install <packagename>

```

#### Libraries Installed

    Requests
    OAuth1 from requests_oauthlib
    json
    os
    time
    glob
    Pandas
    Numpy
    Matplotlib
    Seaborn
    Textblob
    datetime
    
## Step -1 :Data Collection

#### Weather Data

![weather](https://cloud.githubusercontent.com/assets/25700292/25308539/a69dd146-2784-11e7-91bc-03cce4dc5e6d.gif)

#### Uber Data

![uber](https://cloud.githubusercontent.com/assets/25700292/25308606/8c62c53c-2786-11e7-80a7-e522ee8e7152.gif)

#### Green Taxi Data

![greentaxi](https://cloud.githubusercontent.com/assets/25700292/25308640/42f6ac00-2787-11e7-90bf-9beaa094d955.gif)

#### Yellow Taxi Data
   
![yellowtaxi](https://cloud.githubusercontent.com/assets/25700292/25308659/9d0e6a16-2787-11e7-903f-fabc69f9be5f.gif)


## Step -2 :Data Processing

#### 1.Ride Count and Fare Analysis of GreenTaxi,Uber,YellowTaxi

Step-1:Merge all GreenTaxi Files to one dataFrame and Yellow Taxi Files to another Frame

Step-2:Take Sampling records from Yellow Taxi as records are huge

Step-3:Put Uber Data in a DataFrame

Step-4:Merge all the dataframe into one DataFrame selecting only the required columns (E.g Pickup Date)

Step-5:Group the Records Based on Taxi,Month to get the count

Step-6:Group the Records Based on Taxi,Month on all the Fares Column


#### 2. Speed Co-relation between No of Rides per hour and Distance

Step-1:Merge all GreenTaxi Files to one dataFrame

Step-2:Choose the columns PickupDate,DropDate,Distance

Step-3:Calculate speed column using the formula Speed=(Distance/(DropDate-PickUpDate)

Step-4:Remove the records with 0.0 values as some speeds are negligible due to traffic

Step-5:Group the Records By Speed of the Ride and Take the percentile speed change with respect to total Trips

Step-6:Group the Records By Speed of the Ride and Take the percentile Distance covered with respect to total Trips


#### 3. Average Tip Range for the Drivers and Peak Hours where more Tips were Given

Step-1:Merge all GreenTaxi Files to one dataFrame and Take a Sample of 20,000 records

Step-2:Calculate the Tip Percentage of each Ride from the Columns Tip_Amount and Total_Amount

Step-3:Partition the data into bins based on Tip Percentage Ranges and group by the Bins

        Bin Ranges={"No Tip", '1 to 5','5 to 10','10 to 15','15 to 20','20 to 25','25 to 30'}
        
Step-4:Plot the graph with co-relation between bins,Percentage,No of Rides

Step-5:Calculate the Hour and Weekday for each Ride from the Dataframe along with Average Tip Given

Step-6:The output of the step-5 is pivotted for my convenience to plot HeatMap


#### 4. Green Taxi Rides Comparison with Weather Changes

Step-1:Merge all GreenTaxi Files to one dataFrame.

Step-2:Put the Weather Dataset in a DataFrame between the Months where GreenTaxi Records were Taken

Step-3:Group the Records of GreenTaxi based on pickupDate

Step-4:Merge Weather and GreenTaxi based on Date 

Step-5:Use Numpy Bins to calculate count of rides based on the Precipitation Ranges

        Percipitation Bins={0.0, 1.0, 2.0, 3.0}
        
Step-6:Use Numpy Bins to calculate count of rides based on the Snow Ranges

        Snow Bins={0.0,5.0,10.0,15.0,20.0,25.0}
        
#### 5. Pick ups and Drops Based on location in NYC

Step-1:Merge all GreenTaxi Files to one dataFrame and Take a Sample of 20,000 records

Step-2:Calculate the PickupHour and DropHour from PickupDate column and DropDate column.

Step-3:Google Maps API is used to calculate locations from Latitude and Longitude

        URL-https://maps.googleapis.com/maps/api/geocode/json
        
Step-4:Group the Data by Drop Time and Drop Location.

Step-5:Group the Data by Pickup Time and PickUp Location.











