# GREat Expectations

### Introduction

The goal of our project is to try and disentangle the process of graduate school admissions by analysing the various factors at stake, and apply predictive models. Broadly, we want to discover the notions about:
- Patterns in student profiles applying to different graduate schools across geographic locations.
- Inferring and leveraging definitive existing correlations.
- Conclusions about admit/reject ratios, strength of an applicant profile, probability of admission, appropriate universities for a specific profile.

### Data Collection Scripts
#### Step 1 : Setup MIMTPROXY on a web browser and start the listener

#### Step 2 : Setting up website
After setting up filters on the website [https://admits.fyi](https://admits.fyi) and executing the javascript to automate pagination. The network calls would be being monitored.

#### Step 3 : 
Move the capture object into the directory `data_collection/objects` and run the script 
```python colleges.py```
 The JSON with all data will be saved in the directory `data_collection/jsons`. 

### EDA, Analysis and Predictive Modelling

We perform our experiments on three major case studies:
- Carnegie Mellon University
- University of Illinois, Urbana Champaign
- University of California, Los Angeles

The following notebooks inside the `notebooks` directory contain the reproducable code for the EDA, classification and regression analysis and results:
- `CMU_analysis.ipynb`
- `UIUC.ipynb`
- `UCLA_regression.ipynb`

For more details, please refer to `Report.pdf` and the project slides in the `Slides` directory.
Project done by:
- Vishaal Udandarao (2016119)
- Suryatej Reddy (2016102)
- Surabhi S Nath (2016271)
- Suril Mehta (2015104)
