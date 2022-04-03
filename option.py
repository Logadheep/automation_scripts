
# This will import urlopen
# class from urllib module
  
  
from urllib.request import urlopen
page=urlopen("http://geeksforgeeks.org/")
  
# Fetches the code 
# of the web page
content = page.read()
  
print(content)