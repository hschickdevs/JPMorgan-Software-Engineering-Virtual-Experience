![JPM Logo](https://1000logos.net/wp-content/uploads/2020/04/J.P.-Morgan-Chase-Logo.png)
___

 Throughout the virtual experience, I familiarized yourself with JPMorgan Chase frameworks and applied my technical skills to a hypothetical request from the firm’s trading floor to analyze and visualize data in a new way.

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

### **[Task 4:](./Task%204/)**
___