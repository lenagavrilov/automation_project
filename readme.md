# Automation Project

This project will take an html source of a site and compare the number of it's different elements with expected numbers  

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

To run this project you will need Microsoft SQL Server Studio 2012 or higher installed.
You can download the installation file from Microsoft site:
https://www.microsoft.com/en-us/download/details.aspx?id=29062


### Installing

You will need to install a few modules: pyodbc, HTMLParser from html.parser, Urllib.request and
Counter from collections.

Also, You will need to connect to database "automation" and edit your server settings in file "main",
in "connection" variable, so the program will be able to compare actual data with expected data in "automation" 
database.

In the end the program will give you results like this (for the site you entered):

head:   5 expected, found: 1
meta:   10 expected, found: 2
title:   18 expected, found: 1
script:   1 expected, found: 7
....


## Authors
	Lena Gavrilov
### Contributers
	Dina Freidenberg, https://github.com/dina304
## Acknowledgments
	Big thanks to Dina Freidenberg who was so great and patient with me while going over my code again and again, 
	giving remarks and challenging me to use new features.


