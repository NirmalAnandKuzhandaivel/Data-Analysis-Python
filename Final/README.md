
# INFO 7374 - NYC TAXI ANALYSIS WITH WEATHER AND UBER

![nyc_taxi](https://cloud.githubusercontent.com/assets/14088093/25310558/bce34f14-27b4-11e7-9cc1-124f3e9d013a.png)

# Introduction

The New York City Taxi  has released a staggeringly detailed historical dataset covering over 1.1 billionindividual taxi trips in the city from January 2009 through June 2015.As the Data is huge, I have taken data from Jan 2016 to June 2016 for my analysis.Taken as a part of data How much are the earnings by each Taxi Companies , What affects the speed of the Taxi , How weather is related to the rides are the co-relations that you can infer from it .

# Prerequisites

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
    
# Step -1 :Data Collection

#### Weather Data

![weather](https://cloud.githubusercontent.com/assets/25700292/25308539/a69dd146-2784-11e7-91bc-03cce4dc5e6d.gif)

#### Uber Data

![uber](https://cloud.githubusercontent.com/assets/25700292/25308606/8c62c53c-2786-11e7-80a7-e522ee8e7152.gif)

#### Green Taxi Data

![greentaxi](https://cloud.githubusercontent.com/assets/25700292/25308640/42f6ac00-2787-11e7-90bf-9beaa094d955.gif)

#### Yellow Taxi Data
   
![yellowtaxi](https://cloud.githubusercontent.com/assets/25700292/25308659/9d0e6a16-2787-11e7-903f-fabc69f9be5f.gif)

#### Link to Get Taxi Data

<a href="http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml">Yellow Taxi and Green Taxi Data</a>

I have not uploaded Yellow Taxi Data as the file sizes are huge. It can be downloaded from the above link.
Also I did use more csv files than the one uploaded in github Data Folder.


# Step -2 :Data Processing

## 1.Ride Count and Fare Analysis of GreenTaxi,Uber,YellowTaxi

Step-1:Merge all GreenTaxi Files to one dataFrame and Yellow Taxi Files to another Frame

Step-2:Take Sampling records from Yellow Taxi as records are huge

Step-3:Put Uber Data in a DataFrame

Step-4:Merge all the dataframe into one DataFrame selecting only the required columns (E.g Pickup Date)

Step-5:Group the Records Based on Taxi,Month to get the count

Step-6:Group the Records Based on Taxi,Month on all the Fares Column


## 2. Speed Co-relation between No of Rides per hour and Distance

Step-1:Merge all GreenTaxi Files to one dataFrame

Step-2:Choose the columns PickupDate,DropDate,Distance

Step-3:Calculate speed column using the formula Speed=(Distance/(DropDate-PickUpDate)

Step-4:Remove the records with 0.0 values as some speeds are negligible due to traffic

Step-5:Group the Records By Speed of the Ride and Take the percentile speed change with respect to total Trips

Step-6:Group the Records By Speed of the Ride and Take the percentile Distance covered with respect to total Trips


## 3. Average Tip Range for the Drivers and Peak Hours where more Tips were Given

Step-1:Merge all GreenTaxi Files to one dataFrame and Take a Sample of 20,000 records

Step-2:Calculate the Tip Percentage of each Ride from the Columns Tip_Amount and Total_Amount

Step-3:Partition the data into bins based on Tip Percentage Ranges and group by the Bins

        Bin Ranges={"No Tip", '1 to 5','5 to 10','10 to 15','15 to 20','20 to 25','25 to 30'}
        
Step-4:Plot the graph with co-relation between bins,Percentage,No of Rides

Step-5:Calculate the Hour and Weekday for each Ride from the Dataframe along with Average Tip Given

Step-6:The output of the step-5 is pivotted for my convenience to plot HeatMap


## 4. Green Taxi Rides Comparison with Weather Changes

Step-1:Merge all GreenTaxi Files to one dataFrame.

Step-2:Put the Weather Dataset in a DataFrame between the Months where GreenTaxi Records were Taken

Step-3:Group the Records of GreenTaxi based on pickupDate

Step-4:Merge Weather and GreenTaxi based on Date 

Step-5:Use Numpy Bins to calculate count of rides based on the Precipitation Ranges

        Percipitation Bins={0.0, 1.0, 2.0, 3.0}
        
Step-6:Use Numpy Bins to calculate count of rides based on the Snow Ranges

        Snow Bins={0.0,5.0,10.0,15.0,20.0,25.0}
        
## 5. Pick ups and Drops Based on location in NYC

Step-1:Merge all GreenTaxi Files to one dataFrame and Take a Sample of 20,000 records

Step-2:Calculate the PickupHour and DropHour from PickupDate column and DropDate column.

Step-3:Google Maps API is used to calculate locations from Latitude and Longitude

        URL-https://maps.googleapis.com/maps/api/geocode/json
        
```
        
        SampleJson:
        
        [{"long_name": "331", "short_name": "331", "types": ["street_number"]}, {"long_name": "79th Street", "short_name": "79th St", "types": ["route"]}, {"long_name": "Bay Ridge", "short_name": "Bay Ridge", "types": ["neighborhood", "political"]}, {"long_name": "Brooklyn", "short_name": "Brooklyn", "types": ["political", "sublocality", "sublocality_level_1"]}, {"long_name": "Kings County", "short_name": "Kings County", "types": ["administrative_area_level_2", "political"]}, {"long_name": "New York", "short_name": "NY", "types": ["administrative_area_level_1", "political"]}, {"long_name": "United States", "short_name": "US", "types": ["country", "political"]}, {"long_name": "11209", "short_name": "11209", "types": ["postal_code"]}, {"long_name": "3609", "short_name": "3609", "types": ["postal_code_suffix"]}]
        
```
        
Step-4:Group the Data by Drop Time and Drop Location.

Step-5:Group the Data by Pickup Time and PickUp Location.

# Step-3: Data Analysis


## 1.Ride Count and Fare Analysis of GreenTaxi,Uber,YellowTaxi

The below Plot calculates the No of Rides by each Taxi Companies based on Month.

<img width="871" alt="screen shot 2017-04-22 at 7 03 08 pm" src="https://cloud.githubusercontent.com/assets/25700292/25308969/5ef17596-278e-11e7-8643-de0585403bb2.png">

The below Plot calculates Amount Earned under different category every month by all three companies

<img width="690" alt="amount earned by taxis-6 months category" src="https://cloud.githubusercontent.com/assets/25700292/25309630/36548abc-27a0-11e7-9329-946df5c300c7.png">

The below Plot  show Total Amount Earned by Taxi Companies Every Month

<img width="684" alt="monthwise by company" src="https://cloud.githubusercontent.com/assets/25700292/25309632/365634de-27a0-11e7-8a6d-619ce38549bf.png">

The below Plot  show Amount Earned by Different Taxi Companies subcategorzing the previous plot.

<img width="711" alt="amount earned by taxis-category" src="https://cloud.githubusercontent.com/assets/25700292/25309631/3655eca4-27a0-11e7-95e5-85a25b228c9c.png">



## 2. Speed Co-relation between No of Rides per hour and Distance

The below plot indicates when the No of Rides are higher the average speed is low.
This can be explained as: When the no of rides are higher,there are lot of taxis on the road and causes traffic which results in lower average speed

![speedchange_trips](https://cloud.githubusercontent.com/assets/25700292/25309312/c7404506-2797-11e7-8bba-f45f29686076.png)

The below plot indicates when the no of taxis covering longer distance is lower when compared to taxis covering shorter distance.

![speedchange_distance](https://cloud.githubusercontent.com/assets/25700292/25309557/75d49350-279e-11e7-8c44-200cc98a3beb.png)


## 3. Average Tip Range for the Drivers and Peak Hours where more Tips were Given

The below plot calculates the co-relation between percentage of rides,no of rides and the Avergage Tips Given. We can understand from the analysis that if the number of rides are more the Tip range is very low. Vice Versa,If the no of rides is very less,Tip Range is very high. The above plot indicates customers were more satisfied when the no of rides were low they would have got the rides quicker after booking a Taxi and wait time would have been less.

![analysis3_average_tip_given](https://cloud.githubusercontent.com/assets/25700292/25309096/85501ec4-2791-11e7-82f5-bc2091cd6e62.png)


The below categorizes the average Tip Percentage on a weekday basis by binning into every hour of the day. From the plot we can understand that Tip ranges were higher after 12:00 AM and before 9:00 AM.

![heatmap](https://cloud.githubusercontent.com/assets/25700292/25309097/86e94864-2791-11e7-908f-ba7e1305d299.png)


## 4. Green Taxi Rides Comparison with Weather Changes

##### Precipitation Output


Condtions|count
------|--------
0-1|2683594
1-2|179273
2-3|11031

The below plot indicates there were no rides when precipitation ranges of weather were higher in NYC

<img width="637" alt="precipitation-ride" src="https://cloud.githubusercontent.com/assets/25700292/25309286/30ee107e-2797-11e7-9001-581a50fe177a.png">

##### Snow Output

Condtions|count
------|--------
0 - 5|150265.0
5 - 10|227127.0
10 - 15|0.0
15 - 20|87265.0
20 - 25|22010.0

The below plot indicates there were less rides when it was snowing in NYC

<img width="630" alt="snow-ride" src="https://cloud.githubusercontent.com/assets/25700292/25309285/30ed2aa6-2797-11e7-9b1e-eb5a805caf53.png">


## 5. Pick ups and Drops Based on location in NYC

The below plot indicates there were more picks up in Brooklyn in the early morning hours compared to other places

<img width="635" alt="pickup" src="https://cloud.githubusercontent.com/assets/25700292/25309589/4e743134-279f-11e7-9ebe-e1c1c480ff0b.png">

The below plot indicates there were more drops up in Brooklyn in the early morning hours  compared to other places

<img width="636" alt="dropoff" src="https://cloud.githubusercontent.com/assets/25700292/25309590/4e748fa8-279f-11e7-8f57-ca16d01cca35.png">

The below plot shows the pickup and drop locations in the scatterplot.

<img width="602" alt="pickup_drop_locations" src="https://cloud.githubusercontent.com/assets/14088093/25310512/dc5bcf16-27b3-11e7-87db-21977a9ec519.png">






