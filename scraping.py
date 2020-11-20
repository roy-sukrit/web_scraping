
#  import requests
#  import urllib.request
#  import random
#  from bs4 import BeautifulSoup as bs
#  import pandas 
#  base_url = 'https://goodlogo.com/top.250/n/250/interval/'
#  l=[]
#  k=[]
#  name1=[]
#  name2=[]
#  for page_no in range(1, 9, 1):
#      # print(base_url+str(page_no))
#      sourcecode = requests.get(base_url+str(page_no),
#                                headers={'User-Agent': 'Mozilla/5.0'})
#      #print(base_url+str(page_no))
#      plain_text = sourcecode.text
#      soup = bs(plain_text, 'html.parser')
   
#      link = soup.select(".top_s3l")
#      for tag in link:
       
#          my_images = tag.get('src')
      
       
   
       
       
#          #<-------Files Name-------------->#
#          l.append(my_images.replace("/images/logos/small/", ""))
       
       
       
#          #<--------links of all the images in .top_s3l-------->#
#          # full_name = 'https://goodlogo.com'+my_ima
       
   
#      link1 = soup.select(".top_s3")
#      for tag1 in link1:
#          my_images1 = tag1.get('src')
       
#          k.append( my_images1.replace("/images/logos/small/", ""))
         
      
#  mylinks=l+k
#  myName=l+k
#  new=[]
#  for item in myName:
#       new.append(item.replace(".gif","").replace(".png","").replace(".jpg",""))
#  df=pandas.DataFrame(new,mylinks)
#  df.to_csv("mydata")

