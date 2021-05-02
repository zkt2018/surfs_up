# surfs_up
##**Overview of the analysis**
In this project, using tools such as SQLite, SQLAlchemy, and Flask, we query through the weather dataset. We are using SQLAlchemy to connect to our SQLite database and using the queries, filter the data and give a structure to it. Then by Flask application, we design a web application to connect to our query results.
This data will be used to provide the weather information of an island called Oahu, so the investors get the required information before making a decision to build Surf n’ Shake shop(s) on the island.
With these tools, the unstructured data has been ordered and specific information has been gathered and visualized by Flask application. 

##**Results**
1. Based on the analysis, the number of data available for June is higher than the one for December. In addition the standard deviation is higher in December. This reveals that the spread of data is less in December rather than June. 
2. The difference between minimum and maximum shows a bigger difference in December. Even though the maximum temperature during the two months is very close, the interquartile numbers reveal that there may have been more outliers in December than June. This has resulted in higher standard deviation although the range between the minimum and maximum is bigger.

![temp_june.png](https://github.com/zkt2018/surfs_up/blob/main/temp_june.png)

![temp_dec.png](https://github.com/zkt2018/surfs_up/blob/main/temp_dec.png)

3. Lastly, the average temperature is higher in June than December (74.94 vs. 71.04). These differences significantly impact on the number of the tourists that visit the island during each month or during the year.

##**Summary**
The temperature query generally provides good information to help with better understanding of the weather pattern in the island. However, there are other factors that can significantly impact on the weather, e.g. precipitation and location on the island. The average of the temperature during the two analyzed months does not show a major difference, hence, we need to consider the precipitation as well before we get into the conclusion. The other factor that must be considered and we can add to our queries is the location of the station. Depending how far the station is located from the ocean, the temperature might be different. Another factor that seems important in surfing is the wind speed. Although, the wind speed can change more significantly during the day, considering this factor in the analysis can provide a more clear idea about the weather.

