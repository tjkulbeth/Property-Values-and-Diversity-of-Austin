![The Big Hero 6](images/banner.jpg)

# Property Values and Diversity of Austin

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
* H-Null: If property values rise within Austin (by zip code area), then there will be no changes of the diversity index*.

* H-Alt: If property values rise within Austin (by zip code area), then the diversity index* will show significant negative changes.

* The 'Diversity Index' is a value between 0 and 1 which represents the probability of two people being of a different race if randomly picked from the same sample.

### Research Questions to Answer:
1. Does the diversity negatively impacted by the raise of home value in Austin?
2. What is Austin's geographical layout like in relation to home value and diversity?
3. Is there any specific locations that diversity and home value show strong correlations?
4. (bonus) Is school rating a good predictor of home value?

### Data Sources
* Zillow Home Value Index (ZHVI) for All Homes - Time Series, 1996-2018 (https://www.zillow.com/research/data/)
* U.S. Census American Community Survey (ACS), 2011-2017 (https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml)
* GreatSchools API (https://www.greatschools.org/api/docs/technical-overview/)

#### How are data described:
1 - Diversity Index
2 - Period
3 - Home Value
4 - Zip data (for geo location and map)

### Tools & Techniques:
1 - Pandas DataFrame for ETL
2 - Matplotlib, Follium, Google Map API for Visualization
3 - Python LXML/XML parsing for GreatSchools.org API

### Our Findings
#### 01 - Godwin - Data Merge Process - Scatter Plot
![Scatter](images/01-01-godwin-scatter.png)

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
![Aydin Heatmap](images/03-01-aydin-heatmap.png)

#### 04 - Trevor - Zip Code Color Map
![Trevor Zip Map Animations](images/04-01-trevor-diversity-index.gif)
![Trevor Zip Map Animations](images/04-02-trevor-property-index.gif)

#### 05 - Agustin and Billy - General Trend vs Specific Areas
![Billy Home Value vs. Diversity All](images/05-01-Billy-Value-Diversity-All.png)


#### 06 - Agustin and Billy - School Ratings and Home Values


### Conclusion


### Questions?
![Thank you](images/bmax-bye.gif)