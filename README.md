# Education for income

### Background and Goal:
The relationship between income and Education level is well established but remains sometimes poorly understood
Our goal on this project is to Use Machine Learning and analyze the relationship between income per Capita on the number of  Bachelors percentage and postsecondary degree holding by State in the US

### Variables for Exploration: 
Per Capita Income (by State), Bachelor's degree Percentage and post secondary percentage (by State)

### Period: 2012-2017

### Tools Used:
Pandas, Matplotlib, Tableau, Scikit-Learn, HTML, CSS, Bootstrap

### Machine Learning Trends:

Pandas, get_dummies, and feature engineering was utilized to get a better fit model due to our dataset size. States and years were transformed into categorical data. Testing and training data was preprocessed through scaling to normalize the data within a smaller range

<img width="728" alt="table get" src="https://user-images.githubusercontent.com/100292828/187718726-ebd4a5d4-d0d8-4422-b042-44b0adf9faaf.png">

We ran our analysis to get our residual plot. Prior to that, we decided to run linear regressions to see the correlation between income, bachelor’s degree and post-secondary degree. Actual and predicted data was plotted on the same scatterplot.

![Incomevpostsecondary](https://user-images.githubusercontent.com/100292828/187719051-4c6401c7-ef38-469c-9136-0facc462850e.png)
![IncomevsBachelors](https://user-images.githubusercontent.com/100292828/187719306-83a33e31-6f54-4b15-a332-20ac0ba660ba.png)

The R2 of .80 indicates that the model explains about 80% of the variability of the data around the mean. The mean scored error, which shows the averaged squared difference between the predicted and actual values was .09, close to the desired 0 range. 

<img width="302" alt="last s" src="https://user-images.githubusercontent.com/100292828/187720027-e078254f-a8f2-4d47-829e-fd2d26179c66.png">

Tableau: <img width="386" alt="image" src="https://user-images.githubusercontent.com/97966485/187809775-aba8cf9c-3c3e-4ca3-88f0-7ba5895f003d.png">
<img width="385" alt="image" src="https://user-images.githubusercontent.com/97966485/187809828-ccb2e2d4-021d-44dd-bb20-fbd84143a3ca.png">
<img width="521" alt="image" src="https://user-images.githubusercontent.com/97966485/187809842-34d0268e-1f39-4d5a-ac90-2954b815dc39.png">


### Sources: 

https://apps.bea.gov/iTable/iTable.cfm?reqid=70 

https://ncses.nsf.gov/indicators/states/indicator/bachelors-degree-holders-per-25-44-year-olds 






