# Text_Classification_Using_EM_And_Semisupervied_Learning

The acquisition of large amount of labeled text data for text classification is a tedious and expensive task, while there is huge amount of unlabeled data set on Web resources which are easy and cheap. In this project, we investigate the effectiveness of using semi-supervised learning and expectation-maximizatoin(EM) algorithm to take advantage of large amount of unlabeled data to obtain highly accurate text classification. We built a simple multinomial Naive Bayes(NB) classifier and trained it using EM procedure and both labeled and unlabeled text data. And we studied the relation between the multiclass classification accuracy and the fraction of unlabeled data in the training data set. We also explore methods to reduce computational expense in EM procedures to speed up training process. The result showed that our semi-supervised EM NB classifier can achieve above 50% accuracy on average given only 2% labeled data, and above 70% accuracy given one third of training data labeled.

## Getting Started

The models and algorithms of our project is implemented in Python code with the help of IPython Notebook for data and result visualization. All experiments are executed on local machine.

### Prerequisites

Following Python packages have to be installed before executing the project code

```
numpy
scipy
sklearn
nltk==3.1
wordcloud
matplotlib
seaborn
```
* Note _nltk v3.2_ may have issue with stemming functions.

### Installing

IPython notebook can be installed separately using pip 

```
pip install ipython
```

Or with Anaconda bundle.

```
conda update conda
conda update ipython
```

## Running the tests

And IPython notebook can be viewed using available web browser by the following command-line in terminal inside the directory of code:

```
ipython notebook
```
The semi-supervised EM Naive Bayes class in python script is called inside experiment codes. Most of our code are recorded in ipython notebook cells. This notebook can be executed cell by cell in sequential order, or execute all at once using the Kernel starter. And the results will be visualized in images shown below the corresponding cells. 

## Expected Results

The result is to improve the multi-class text classification accuracy by semi-supervised EM Naive Bayes classifier given both labeled and unlabeled documents.

![Classification Accuracy Improvement](https://github.com/jerry-shijieli/Text_Classification_Using_EM_And_Semisupervied_Learning/blob/master/result/cv_f1.png)

![Word Cloud of Most Probable Keywords in Each Class](https://github.com/jerry-shijieli/Text_Classification_Using_EM_And_Semisupervied_Learning/blob/master/result/test_em_nb_wc.png)

For more details and intermediate results, please check the ipython notebooks in the folder [code](https://github.com/jerry-shijieli/Text_Classification_Using_EM_And_Semisupervied_Learning/tree/master/code)


## Contributors

* **Shijie Li**  *(email: sli41@ncsu.edu)* 
* **Yifan Guo** *(email: yguo14@ncsu.edu)*

## Acknowledgments

* Thank Prof. Min Chi for the support on this project.
* Thank all TAs of CSC591 course for the evaluation and feedback on this project.


