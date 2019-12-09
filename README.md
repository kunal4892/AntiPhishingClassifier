# AntiPhishingClassifier
Classifier for segregating Phishing websites from legitimate websites.

# Team Members:
* Noopur Rajesh Kumar Kalawatia
* Harshit Agrawal
* Kumar Kunal
* Richa Singh

# Description
The project aims to take different approcches to mine associative rules from a list of comprehnsive datasets.
The rules that comply with a particalur accepatable threshold are selected to be used to training the models.

The following Supervised learning models are used with K-fold validations:
* Log-Reg
* K Nearest Neighbors
* Decision Tree
* Random Forest

The dataset is segregated into training and testing datasets.
The training dataset is used to perform k-fold validations over 
each of the models and the performance with each of the models
is documented. Then the models are exposed to the completely 
untouched dataset. This performance gives us the real world 
application efficiency. 

The goal of using K-fold validations is to obtain the best possible
hyper parameter over various runs over different divisions of the training 
partition of the dataset.

our goal is to compare and contrast how consistent each model is during the
training and testing phase. This gives us an insight of how good the mined features
are for all the different models and hints at whether the selected features need to
be refined/rethought for more effective training. We expect to demonstrate this by
showing the feature separation using different plots.

Though the metric initially decided to be used for analysing the performance was F1-score.
We use acuuracy scores finally beacause the dataset is very well balanced in both the categories.
