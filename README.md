# real-estate-price-prediction

## DESCRIPTION

### This project aims to create a Machine Learning model to make price predictions on real estate sales in Belgium.

### Task # 1 is to build a dataset gathering information about at least 10,000 properties all over Belgium.

I built a `data_acquisition` notebook in `data_acquistion` folder to set about doing this.

I started by building a function to get the page links (page URLs) I would need through accessing the homepage (root URL). Then, I pass on the page URLs to a function that will extract the property links (property URLs) from each page. From there, I pass on the property URLs to a function the will extract each property's information and save it in a dictionary. This dictionary is then stored into a `pandas` dataframe and saved to a `csv` file.

At the end of alloted duration for Task # 1, I have written up all the functions needed to extract the property information. However, I am only able to extract 1,140 properties in a `csv` file because my `get-page-links` function can only extract the page links for the first 15 pages of *Apartment* pages and *House* pages respectively (30 pages total). I would still need to refine this function to extract all the page links. Another possibility is to extract only about the first 135 pages from *Apartment* and the first 135 pages from *House* to get to around 10,000 properties.

The resulting data is also very raw and still needs a lot of *scrubbing*. There are also a lot of mismatched data (as in data that are not in the right columns (insert *sadface* here)).

### Task # 2 is to take dataset from Task # 1, clean it, interpret it, and analyze it.

At the beginning of Task # 2, I re-ran `data_acquisition` from Task # 1 to read 60 pages each from *Apartment* and *House* (120 pages total) and extracted 4,560 properties raw data.

*Cleaning/scrubbing* this data involved finding null/empty data and converting it to `None`, minimizing non-numeric values and removing mismatched data. After data *cleaning/scrubbing*, I removed duplicate entries and also rows with no address information. I ended up with a working dataset of 3,585 rows and 99 columns (see `data_analysis` notebook in `data_analysis` folder).

The *scrubbing* was a long process and I could have done a better job by employing functions on all the columns first then going through each column to see what else needs cleaning instead of going through each column one at a time from the get go. I only realized this when I was nearly done with the *scrubbing* (insert *facepalm* here).

At the end of alloted duration for Task # 2, I produced three graphic visualizations using `matplotlib` (see `data_analysis_2` file). 

`fig_1.png` is a graph on the number of properties for sale in Belgium by province.

![alt text](https://github.com/m9tadeo/real-estate-price-prediction/blob/main/data_analysis/fig_1.png)

`fig_2.png` is a graph on the median property price per province.

![alt text](https://github.com/m9tadeo/real-estate-price-prediction/blob/main/data_analysis/fig_2.png)

`fig_3.png` is a graph on the average property price by energy class.

![alt text](https://github.com/m9tadeo/real-estate-price-prediction/blob/main/data_analysis/fig_3.png)

### Task # 3 is to create a Machine Learning model to predict prices on Belgium's real estate sales.

After evaluating the data for what can be used for model training, I ended up with a working dataset of 991 rows and 20 columns (see `model_training` notebook in `model_training` folder). 

I considered 5 columns as categorical data and the rest are numerical data. One column is the target feature (`price`). I used `OneHotEncoder` on my categorical data. I then used `MinMaxScaler` to scale all the data after splitting between training set and test set. I tested 6 different regression models on my data with varying results (see `model_training_2` notebook).

**Extra** I also built a `features_correlation` notebook to look into the correlation scores between certain columns and the price.

### Task # 4 is to deploy a machine learning model, create an API that can handle a machine learning model, and deploy an API to Render with Docker.

Inside `deployment` folder are 3 other folders. The `preprocessing` folder contains my `cleaning_data` module which is used to clean/preprocess the input data that will be used to make a price prediction. The `predict` folder contains my `prediction` module which is used to take the cleaned/preprocessed input data from the `cleaning_data` module and produce an output of a predicted price. The `model` folder contains the `joblib` files (encoder, scaler, and model) saved from training the model (see `model_working` notebook). These will then be used/called-up in the `prediction` module.

I built my API using `Flask` and saved it in the `app.py` file inside `deployment` folder. This API contains a route at `/predict` that accepts a `GET` request and returns a string to explain what the `POST` request expects (data and format). It then accepts a `POST` request that receives data of a House or Apartment in `JSON` format that is then passed on to the modules mentioned in the preceding paragraph to predict a price. It will return an output of the price prediction or an error message if the data doesn't contain the required information. This API also has a route at `/` that accepts a `GET` request to check if the server is alive and returns `It's alive!` if it is.

I was able to run my API successfully on my local machine however, at the end of alloted duration for Task # 4, I did not have enough time to create a `Dockerfile` to wrap my API and then deploy my docker image in `Render.com`.

### THE END

## INSTALLATION

This project can be accessed in a Python editor of your choice. I use `VSCode` (~~because I'm a human~~). I also used Python 3.10 running on a `virtual environment`. All the libraries I used are always on the first part of each notebook or .py file.

## USAGE

This project may be viewed by anyone who wants to follow along in my training process of building a machine learning model from inital data collection, to cleaning, to analysis and visualization, to model training and prediction, and finally to deployment via an API.

I would not really recommend using this for anything else other than for educational purposes (insert `grimacing face` here).

## CONTRIBUTORS

Marlon Tadeo

This project is part of a bootcamp training in Python and Data Science. While I worked solo on it, I obviously could not have done any of it without help from my instructors and my fellow learners.

## TIMELINE

Project started 4 October 2022

> Task # 1 started 4 October 2022  
> Task # 1 ended 10 October 2022  
> Task # 2 started 10 October 2022  
> Task # 2 ended 18 October 2022  
> Task # 3 started 24 October 2022  
> Task # 3 ended 27 October 2022  
> Task # 4 started 31 October 2022  
> Task # 4 ended 4 November 2022

Project ended 4 November 2022

## PERSONAL SITUATION
I am currently a Junior Data Scientist at BeCode Ghent. You can reach me at `m9tadeo@gmail.com`.
