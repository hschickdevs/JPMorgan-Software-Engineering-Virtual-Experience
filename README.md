![JPM Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/JPMorgan_Chase.svg/1280px-JPMorgan_Chase.svg.png)
___

 Throughout the virtual experience, I familiarized yourself with JPMorgan Chase frameworks and applied my technical skills to a hypothetical request from the firm’s trading floor to analyze and visualize data in a new way.
 
 Technologies used include: Python (Pandas, Flask), HTML/CSS, JavaScript (React, NodeJS, TypeScript), Git & GitHub

## Virtual Experience Link:

https://www.theforage.com/virtual-internships/prototype/R5iK7HMxJGBgaSbvk/JP-Morgan-Banking-Technology-Virtual-Program?ref=4AiKNGoEiBmcRxP9M#lp

## Tasks Breakdown

### **[Task 1:](./Task%201/)**
___

Overview:
* A trader has requested the development of a chart to add to their trading dashboard, allowing them to better identify improperly valued stocks using correlation coefficients.
* Theoretically, if a stock's price movements deviate from the historical correlation, this could indicate a potential trading strategy to simultaneously buy the underperformed stock, and sell the outperforming stock.

Objectives:
1. Set up local dev environment
2. Fix the broken client datafeed script in the repository by making the required adjustments to it.
3. Push changes and submit work. 

**Changes Made after Task Completion:**

In client.py:
- Added type hints for all functions
- Fixed getDataPoint function to return accurate stock price
- Fixed getRatio function to return accurate ratio
- Added error handling for getRatio function to account for zeroDivisionError
- Fixed console output to return accurate values
- Formatted the ratio values into a neat matrix (Pandas DataFrame) to display the ratio across symbols

In requirements.txt:
- Added  pandas as a package requirement

### **[Task 2:](./Task%202/)**
___

Overview:
* The main objective of the task is to fix the client-side web application so that it displays a price graph that automatically updates as it gets data from the server-side application.
* In this task we work with JavaScript (TypeScript, NodeJS, React) and Python.

Objectives:
1. Set up local dev environment 
2. Fix the broken typescript files in the project repo to make the web application output correctly
3. Push changes and submit work.

**Changes Made after Task Completion:**

In /src/App.tsx:
- Implemented the setInterval() JavaScript method to continuously fetch data from the API.
- Implemented functionality to render react Graph component.

In /src/Graph.tsx:
- Implemented React Graph component to display live-streamed stock price data.


### **[Task 3:](./Task%203/)**
___

Overview:
* The main objective of the task is to create a clear and concise dashboard that displays stock correlation data from the server-side application in a visually appealing graph.
* Given this graph, trader's should be able to quickly identify which stocks are over/under-valued based on the ratio moving from the average historical correlation. These movements from historical correlation averages can be measured by upper and lower bounds to determine the trading opportunity.
* In this task we work with JavaScript (TypeScript, NodeJS, React) and Python.

Objectives:
1. Set up local dev environment 
2. Fix the broken typescript files in the project repo to make the web application output correctly
3. Push changes and submit work.

**Changes Made after Task Completion:**

Reconfigured the React application from Task 2 to display a dashboard to display stock correlations and bounds trading opportunities. Screenshot below:

![Dashboard](./Task%203/img/screenshot.png)

In src/Graph.tsx:
- Reconfigured the existing React Graph component to monitor the ratio of two stocks against the historical correlation with upper and lower bounds. Upper bound = 5% positive deviation, lower bound = 5% negative deviation

In src/DataManipulator.ts:
-  Refactored the generateRow function to process the new data to output to the correlation graph.
- Modified the Row interface to represent the new graph attributes.

### **[Task 4 (Bonus Task):](./Task%204/)**
___

Overview:
* Make a contribution to Perspective or other project backlogs.

*In Progress*
