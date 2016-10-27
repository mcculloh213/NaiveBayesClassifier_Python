# NaiveBayesClassifier_Python
Naive Bayes Classifier agent built in Python 3

## About
Naive Bayes classifier is a probabilistic classifier that uses Bayes' theorem to estimate the classification of a data entity (row of data). It depends on a (naive)
assumption of independence between the probability of effects given a cause to estimate the probability of a cause given multiple effects, hence the name 
Naive Bayes classifier.

### Running
 * _NaiveBayesClassifier.py_ `./NaiveBayesCalculator.py`
     This is the "main" function that runs the program. To run the program enter:
     ```shell
     $ python NaiveBayesClassifier.py "./absolute/path/to/data.csv" <"./absolute/path/to/estimation_data.csv">
     ```
     For example, running the command:
     ```shell
     $ python NaiveBayesClassifier.py "./data/pima-indians-diabetes.csv"
     ```
     will run the Naive Bayes agent on the `pima-indians-diabetes.csv` dataset. While this may not do anything interesting, going into the main log,
     (`./logs/main.log`) the last line will display the accuracy of the classifier on the passed dataset. A more interesting example, however:
     ```shell
     $ python NaiveBayesClassifier.py "./data/primate-factors.csv" "./data/primate-factors-no-class-var.csv"
     ```
     will create a new `.csv` file, `./data/primate-factors-predictions.csv` and a new `.txt` file, `./data/primate-factors-predictions-about.txt`
     that describes the unknown dataset with estimated classes and the accuracy of the classifier on the known dataset, respectively.
     
     The program assumes data is in the following format:
     
     | _AttributeR,C_ | _AttributeR,C_ | _..._ | _AttributeR,C_ | _Class VariableR_ |
     
     | :------------: | :------------: | :---: | :------------: | :---------------: |
     
     | _Attribute1,1_ | _Attribute1,2_ | _..._ | _Attribute1,N_ | _Class Variable1_ |
     
     | _Attribute2,1_ | _Attribute2,2_ | _..._ | _Attribute2,N_ | _Class Variable2_ |
     
     |     _..._      |     _..._      | _..._ |     _..._      |       _..._       |
     
     | _AttributeN,1_ | _AttributeN,2_ | _..._ | _AttributeN,N_ | _Class VariableN_ |

## Versions & Revisions
 * Version 1.0, last modified 10/27/2016 _(current)_
     * Base implementation
     * Probability is only estimated on a Normal (Gaussian) Distribution
     * Known data is currently split at 67% training, 33% testing
 
