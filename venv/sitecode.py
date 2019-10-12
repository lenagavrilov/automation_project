import urllib.request
import sys


# site_name = input("Type the site: ")
# code_url = 'http://' + site_name

code_url = sys.argv[1]
file_name = 'C:\\Users\\Lena_Laptop\\PycharmProjects\\automation\\venv\\sitehtml.txt'
urllib.request.urlretrieve(code_url,filename=file_name)

