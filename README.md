# Get a best possible route by Python bot
> A webscraper to give best route by opening and getting position using Python

## Prerequisites
- Selenium
- time
- Google webdriver

## Steps
1. Create a driver passing path of driver into ```webdriver.Chrome()```
2. Get google maps by opening on Chrome
3. Take two inputs as From and Destination
4. By taking id as *searchbox* pass key as from, I've sent it as Ujire directly
5. Find the xpath of search button and using driver click that button after entering the search value
6. Get directions of that route by clicking th button
7. Find kelometers of different options to travel the distance like for 
    - Total KM by NH
    - Time by Train
    - Total KM by walk
    - Total KM by car
8. Return a route which has lowest KM value.  
