![JPM Logo](https://assets.stickpng.com/images/58480a96cef1014c0b5e491d.png)
___

 Throughout the virtual experience, I familiarized yourself with JPMorgan Chase frameworks and applied my technical skills to a hypothetical request from the firm’s trading floor to analyze and visualize data in a new way.

## Virtual Experience Link:

https://www.theforage.com/virtual-internships/prototype/R5iK7HMxJGBgaSbvk/JP-Morgan-Banking-Technology-Virtual-Program?ref=4AiKNGoEiBmcRxP9M#lp

## Tasks Breakdown

### <u>**Task 1:**</u>

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

### <u>**Task 2:**</u>

### <u>**Task 3:**</u>

### <u>**Task 4:**</u>