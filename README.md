# EGP_Realtime_ExchangeRate
a command line program that shows  EGP real time exchange rate for foreign currencies using currencyconverterAPI
https://www.currencyconverterapi.com/

# Guidelines

  # setting the environment 

1- run the command below to create the environment that contains program dependencies
   (I use conda environments)
   
   ```
         conda env create -f environment.yml 
   ```
  this command is gonna create a conda environment called apis_python
  
2- activate the environment

  ```
        source activate apis_python
  ```
 # setting the database (Postgresql)
 
 3- open DB_CONFIG.ini , provide user data and database name that you want to store user logs in using the 
     postgresql installed  on your computer
    (make sure that you don't change the any of the keywords)     
  ``` 
        [postgresql]
        host=localhost
        port=5432
        database=postgres
        user=postgres
        password=test123  
  ```
  
 # running main script
 
 4-  now you are ready to run the program as follows 
 
 ``` 
       python EGPExchangeRate.py <foreign-currency-code>
 ```
 example: 
 
 getting the EGP exhange rate for the Dollar(USD)
        
        python EGPExchangeRate.py USD
 
 this is a successful output
 
       we can connect to database successfully
       one USD equals  17.685039 Egyptian pounds
       1 Record inserted successfully into table

