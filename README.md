![The Big Hero 6](images/banner.jpg)

# Analysis of Property Values and Diversity in Austin
### UTA Data Bootcamp Project 1, Group 6

## Our Team:
![The Team](images/the-team.gif)
* Eric Tonian
* Godwin Assiogbon
* Aydin Yildirim
* Trevor Kulbeth
* Agustin Gonzalez
* Wenbin Zhao "Billy"

### Project Description:
This project will examine the relationship between property values and racial demographics in the zip codes areas of Austin, TX from 2011-2017.

### Hypothesis:
##### * H-Null: If property values rise within Austin (by zip code area), then there will be no changes of the diversity index*.
##### * H-Alt: If property values rise within Austin (by zip code area), then the diversity index* will show significant negative changes.

### Research Questions to Answer:
1. Does the diversity negatively impacted by the raise of home value in Austin?
2. What is Austin's geographical layout like in relation to home value and diversity?
3. Is there any specific locations that diversity and home value show strong correlations?

### Data Sources
* Zillow Home Value Index (ZHVI) for All Homes - Time Series, 1996-2018 (https://www.zillow.com/research/data/)
* U.S. Census American Community Survey (ACS), 2011-2017 (https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml)
* GreatSchools API (https://www.greatschools.org/api/docs/technical-overview/)

#### How are data described:
1. Diversity Index - The 'Diversity Index' is a value between 0 and 1 which represents the probability of two people being of a different race if randomly picked from the same sample.
2. Period
3. Home Value
4. Zip data (for geo location and map)

### Tools & Techniques:
1. Pandas DataFrame for ETL
2. Matplotlib, Follium, Google Map API for Visualization
3. Python LXML/XML parsing for GreatSchools.org API

### Our Findings
#### 01 - Godwin - Data Merge Process - Scatter Plot

Merging the data in one uniform dataset

Scatter Plot showing weak correlation \
![Scatter](images/01-01-godwin-scatter.png)

Since the p-value indicate that the p-value is less than .05, it rejects the null hypothesis and support our hypothesis that there is a big correlation between property value and diversity. I took it further and went into how it affects different city types and from the looks of it, it seems like rural areas takes the most hit when it comes to how diversity index affects the property value but overall, it indicates that as diversity index increases, property value across all city types decreases.\
![boxplot](images/01-02-godwin-boxplot.png)

#### 02 - Eric - Regression Analysis
![Eric Urban Line Chart](images/02-02-eric-urban-line.png)

![Eric Suburban Line Chart](images/02-03-eric-suburban-line.png)

![Eric Rural Line Chart](images/02-04-eric-rural-line.png)

#####  Linear Regression Analysis (All Zips and Years)
slope: -366763.29582571954    intercept: 391067.6471445414    stderr: 29170.424325240187
r-value: -0.48937718437748057    p-value: 1.0384045132848702e-31

![Eric Regression All](images/02-07-eric-regression-all.png)

##### Linear Regression Analysis (Urban Zips, All Years)
slope: -721519.9070789743    intercept: 604243.1975286676    stderr: 55372.521800578215
r-value: -0.8099936377599409    p-value: 2.4371772271053096e-22

![Eric Regression Urban](images/02-08-eric-regression-urban.png)


#### 03 - Aydin - Google Heat Map
For the heat map, I used the merged data from Zillow and Census .I filtered merged data by 2017 to understand how diverse is Austin and surrounding areas.I added latitude and longitude to my data chart as well to use heatmap. In short, Round Rock, Pflugerville, Leander, Buda, Mountain City, San Marcos and part of the Cedar Park have diverse population compare to rest of the Austin and surrounding areas.
![Aydin Heatmap](images/03-01-aydin-heatmap.png)

#### 04 - Trevor - Zip Code Color Map
![Trevor Zip Map Animations](images/04-01-trevor-diversity-index.gif)
![Trevor Zip Map Animations](images/04-02-trevor-property-index.gif)

https://www.dropbox.com/sh/z98ulxf2m9khuku/AAC7XHnB_WOKv-ca9jviqOS6a?dl=0

#### 04 - Agustin - Correlation Coefficient
![Agustin](images/06-01-agustin-scatter.png)
![Agustin1](images/06-02-agustin-data.png)
![Agustin2](images/06-03-agustin-data2.png)

#### 05 - Billy - General Trend vs Specific Areas
Let's take a look at the data. 
Austin as a whole (including all zip code) shows a slightly uptick of diversity index:
![Billy Data1](images/05-01-billy-all-data.png)

The graph confirms that:
![Billy Home Value vs. Diversity All](images/05-01-billy-value-diversity-all.png)

What if we look closer - just the area that immediately east of downtown by I-35?
I included 7 zip codes. Here is the map showing the zip codes selected:
![Billy Zip Map](images/zip-map.png)

Now, let's take a look at the data set:
![Billy East Central Data Set](images/05-02-billy-east-central-data.png)

Interesting, isn't it? These area shown quite a bit of movement among different ethic groups:
![Billy East Central Graph](images/05-02-billy-east-central-only.png)

Now, let's look further in granuality. Just one zip code: 78722
What about 78722?
![Billy 78722](images/05-03-billy-78722-only.png)

Let's take a look at the data first: \
![Billy 78722 data](images/05-03-billy-78722-data.png)

The graph and T test will show much more distinctive pattern than Austin in gernal:\
![Billy 78722 only](images/05-03-billy-78722-graph.png)

##### Regression Analysis:
LinregressResult(slope=-3720.172417840378, intercept=342491.2738648559, rvalue=-0.9688170714695908, pvalue=0.0003243039756793674, stderr=425.4978954053012)

### Conclusion
1. Austin as a whole, we do see a weak correlation between raising property values and falling diversity rates
2. Austin's wealth (home value) tend to concentrated to the west while eastern areas of Austin tend to be more diverse
3. When look at different areas such as certain zip codes, we see a much more pronounced pattern of home value increase cause shift of diversity to reduce. 
4. More specifically, certain central east Austin communities see a major change in ethic and racial composition change.

### Limitations
1. Data source
2. Further discussions

### Questions?
![Questions](images/why.gif)


## Thank you!
![Thank you](images/bmax-bye.gif)