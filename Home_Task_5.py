from datetime import datetime

# Create 'News' class, date is calculated during publishing and set up by default
class News:
     def __init__(self, text, city, date_time = datetime.now().strftime("%d/%m/%Y, %H:%M")):
          self.text = text
          self.city = city
          self.date_time = date_time


# Create 'PrivateAd' class
class PrivateAd:
     def __init__(self, text):
         self.text = text

     def date_time(self):

          str_d1 = input('Please input "Actual until" date in format: d/m/Y: ')

          # Convert string data type to datetime datatype for inputed date
          d1 = datetime.strptime(str_d1, "%d/%m/%Y")
          # Double convertion for publishing date (datetime-string-datetime)
          d2 = datetime.now().strftime("%d/%m/%Y")
          dt_object = datetime.strptime(d2, "%d/%m/%Y")

          # Difference between dates in timedelta
          delta = d1 - dt_object

          return (f'{delta.days} days left')

# Crate 'UsefulTips' class
class UsefulTips:
     def __init__(self, text, author):
          self.text = text
          self.author = author


# Create a function which will help the user to create his publication
def publishing():
     n = input('Choose your data type (News, Private Ad, Useful Tips): ')
     try:
          if n == 'News':
               news = News(input('Your text: '), input('City: '))
               result = (f'News -------------------------\n{news.text}\n{news.city}, {news.date_time}\n------------------------------')
          elif n == 'Private Ad':
               private_ad = PrivateAd(input('Your text: '))
               result = (f'Private Ad -------------------\n{private_ad.text}\nActual until: {private_ad.date_time()}\n------------------------------')
          elif n == 'Useful Tips':
               useful_tips = UsefulTips(input('Your tip: '), input('Author: '))
               result = (f'Useful Tips ------------------\n{useful_tips.text}\nAuthor: {useful_tips.author}\n------------------------------')
          return result
     except:
          print('This data type is not supported.')


l = publishing()


# Create a function which will write new publications to the end of the file
def write_to_file():
     try:
          f = open('C:/Users/Yelyzaveta_Shapran/Desktop/New folder (2)/newsfeed.txt','a')
          f.write(l + '\n\n\n')
          f.close()
     except:
          print('Please repeat again according to the specified data types.')

write_to_file()