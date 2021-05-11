# Failure Prediction for Mechanized Oil Equipment
  
[![View Code](https://img.shields.io/badge/View%20-Code-green)](https://github.com/tta2yta/Tic_tac_toe/tree/feature_branch)
[![Github Issues](https://img.shields.io/badge/GitHub-Issues-orange)](https://github.com/tta2yta/Tic_tac_toe/issues)
[![GitHub Pull Requests](https://img.shields.io/badge/GitHub-Pull%20Requests-blue)](https://github.com/tta2yta/Tic_tac_toe/pull/)

## Content

<a text-align="center" href="#about">About</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#method">Methods</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#ins">Installing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#with">Built with</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#ldl">Live Demo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#author">Author</a>

## About <a name = "about"></a>
This project demonstrates an approach to adopt for the transition from preventive maintenance that is manipulated at preplanned time intervals, into predictive ones. To enable such a method in the industrial production system, deep learning machine learning algorithms are used, enabling maintenance activities to be established concerning the existing operational status of the production system. For the building and implementation of the selected model, real-world data collected from the production industry is used for training and testing the model to classify or predict between healthy and non-healthy states.
LSTMs are a well-known and important tool for failure detection in time series data. They can able capture features in the time series data and therefore used to make a forecast concerning the future trend of data. In this paper, the SeqtoSeq LSTM model is used to predict failures for mechanized oil production equipment. The proposed approach composes two main parts: in the first part, each raw telemetry sensor signal data collected is pre-processed and in the second part, all pre-processed signals are given into the SeqtoSeq LSTM model to classify the health condition of the equipment. 


## 🔧 Built with<a name = "with"></a>

- Python


## 🔴 Live Demo <a name = "ldl"></a>


## Getting Started

To get a local copy of the repository please run the following commands on your terminal:

```
$ cd <failure-prediction-for-mechanized-oil-equipment>
```

```
$ git clone https://github.com/tta2yta/failure-prediction-for-mechanized-oil-equipment.git
```

## To run the code:

```
$ curl -X POST -H "Content-Type: application/json" -d @E:\data_science_II\final-paper-data\books\papers\final-paper\pass-days.json http://127.0.0.1:5000/model
```
## Usage

- You can run the application with curl command from command line, the web server accepts json format data to predict a result. Therefor, you must specify the json file in the curl command.

## ✒️  Author <a name = "author"></a>

👤 **Tedrso Tesfay**

- Github: [@tta2yta](https://github.com/tta2yta)
- Twitter: [@Tedros12859799](https://twitter.com/Tedros12859799)
- Linkedin: [tedros-tesfay-489422111](https://www.linkedin.com/in/tedros-tesfay-489422111/)


## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](https://github.com/tta2yta/failure-prediction-for-mechanized-oil-equipment/issues).


## 👍 Show your support

Give a ⭐️ if you like this project!

