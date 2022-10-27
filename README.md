# real-estate-price-prediction

## DESCRIPTION

This project aims to create a Machine Learning model to make price predictions on real estate sales in Belgium.

Task # 1 is to build a dataset gathering information about at least 10,000 properties all over Belgium.

At the end of alloted duration for Task # 1, I have written up all the functions needed to extract the property information in `data_acquisition` notebook in `data_acquisition` folder. However, I am only able to extract 1,140 properties in a `properties.csv` file because my `get-page-links` function can only extract the page links for the first 15 pages of *Apartment* pages and *House* pages respectively (30 pages total). I would still need to refine this function to extract all the page links. Another possibility is to extract only about the first 135 pages from *Apartment* and the first 135 pages from *House* to get to around 10,000 properties.

The resulting data is also very raw and still needs a lot of *scrubbing* such as minimizing non-numeric values and finding null/empty data and converting it to `None`. There are also a lot of mismatched data (as in data not in the right columns `:(`).

Task # 2 is to take dataset from Task # 1, clean it, interpret it, and analyze it.

At the beginning of Task # 2, I re-ran `scraper` from Task # 1 to read 60 pages each from *Apartment* and *House* (120 pages total) and extracted 4,560 properties raw data.

After *scrubbing* data, I removed duplicate entries and rows with no address information. I ended up with a working dataset of 3,585 rows and 99 columns. The *scrubbing* was rough and I could have done a better job by employing functions instead of repeating codes. I only realized this when I was nearly done with the *scrubbing*. (Insert `facepalm` here)

At the end of alloted duration for Task # 2, I produced three graphic visualizations (located in `data_analysis_2` file). `fig_1.png` is a graph on the number of properties for sale in Belgium by province.

![alt text](https://github.com/m9tadeo/real-estate-price-prediction/blob/main/data_analysis/fig_1.png)

`fig_2.png` is a graph on the median property price per province.

![alt text](https://github.com/m9tadeo/real-estate-price-prediction/blob/main/data_analysis/fig_2.png)

`fig_3.png` is a graph on the average property price by energy class.

![alt text](https://github.com/m9tadeo/real-estate-price-prediction/blob/main/data_analysis/fig_3.png)

Task # 3 is to create a Machine Learning model to predict prices on Belgium's real estate sales.

After evaluating the data for what can be used for model training, I ended up with a working dataset of 991 rows and 20 columns. 

1 column is the target feature (`y`). I considered 5 columns as categorical data and the rest are numerical data. 

After and cleaning and preprocessing the data, I tested 6 different regression models on my data with varying results. See `data_analysis_2` notebook.

## INSTALLATION

This project can be accessed in a Python editor of your choice. I use `VSCode`. I recommend creating and activating a `virtual environment`.

## USAGE

This project may be viewed by anyone who wants to follow along in the training process of data engineering, data analysis, and machine learning.

## CONTRIBUTORS

Marlon Tadeo

## TIMELINE

Project started 4 October 2022  
> Task # 1 started 4 October 2022  
> Task # 1 ended 10 October 2022  
> Task # 2 started 10 October 2022  
> Task # 2 ended 18 October 2022  
> Task # 3 started 24 October 2022  
> Task # 3 ended 27 October 2022

## PERSONAL SITUATION
I am currently a Junior Data Scientist at BeCode Ghent
