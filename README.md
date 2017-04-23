# MLRP Project for HackHouston 2017

# Online resume processing application using machine learning algorithms
------------------------------------------------------------------------
## Inspiration
As a team of undergrad computer scientists we will soon face the crazy world or resumes, interviews, work, etc... It stresses everyone out whether they will be able to get that dream job at Google or whether or not they are skillful enough to even compete. 

## What it does
Our machine learning system uses algorithms to classify resumes of top software engineers in various companies and label their skills accordingly. Next, the user uploads their resume and it is tested against the predicted hypothesis by the NB algorithms which in hand returns what tier you belong to. As for tiers, we divided them into two parts. Top tier, such as Google, Facebook, Amazon, IBM, etc..., and bottom tier such as local Houston companies. Unfortunately, due to time constraints we cannot provide company specific statistics according to ones resume.

## How we built it
We used scikit-learn module along with Bernoulli Naive Bayes algorithm, Passive Aggressive algorithm, Logistic Regression, ADA Boost, and Decision Trees. After comparing the accuracy results, Passive Aggressive algorithm outputted 96% accuracy thus becoming our choice for the system. Next we setup the backend using Flask and published it on PythonAnyWhere. The frontend is in HTML5/CSS3. 

## Challenges we ran into
Finding resumes! In order for our system to work accurately we must provide as much data (resumes) as possible! And not only that but quality resumes! Such things are hard to come across. Luckily, we managed to come up with 1000 resumes that we used in training and testing the module.

Algorithm Accuracy Scores:
1. Bernoulli Naive Bayes: 83% 
2. Logistic Regression: 92%
3. **Passive Aggressive: 96.875%**
4. Decision Tree: 95.102%
5. ADA Boost: 93.483%

## Accomplishments that we're proud of
We are really proud with the idea that we came up with because many many students are worried about their future and would like to know what the future holds for them. Unfortunately, we are no fortune tellers but nevertheless we are good machine learning engineers who with some help of statistics and Python can help anyone find out their realistic potential!

## What we learned
Nothing is easy! Heck, writing this isn't as easy as it looks. But we didn't give up and here we are presenting our final product (not the final idea) and open to suggestions and contributions!

## What's next for MLRP
We would like to dive deeper into machine learning algorithms to provide more descriptive and personalized results to every single user for a full user friendly experience.
