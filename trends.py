def trends():
      base= start_date=end_date= out_curr=""
      import requests
      url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(base,start_date,end_date,out_curr)

      response = requests.get(url)
      #import libraries to handle request to api




      # import requests
      import json

      import pprint
      # base currency or reference currency
      base="USD"

      # required currency for plot
      out_curr="INR"

      # exchange data from a date
      start_date="2021-01-01"

      # exchange data till a date
      end_date="2021-03-04"

      # api url for request
      url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(base,start_date,end_date,out_curr)
      response = requests.get(url)

      # retrive response in json format
      data = response.json()

      pprint.pprint(data["rates"])
      # create an empty array to store date and exchange rates
      rates=[]
      # extract dates and rates from each item of dictionary or json in the above created list
      for i,j in data["rates"].items():
            rates.append([i,j[out_curr]])
      print(rates)

      import pandas as pd
      df=pd.DataFrame(rates)
      # define column names explicitely
      df.columns=["date","rate"]
      # df
      import matplotlib.pyplot as plt

      # Put dates on the x-axis
      x = df['date']
      # Put exchange rates on the y-axis
      y = df['rate']
      # Specify the width and height of a figure in unit inches
      fig = plt.figure(figsize=(15,6))
      # Rotate the date ticks on the x-axis by degrees
      plt.xticks(rotation=90)
      # Set title on the axis
      plt.xlabel('Date', fontsize=12)
      plt.ylabel('Exchange Rates', fontsize=12)
      # Plot the data
      plt.plot(x,y)
      plt.show()


