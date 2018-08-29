# E-Planning Web Scraper

## Description
A web scraping application extracting data points related to each county within Ireland, with the capability to extract URLs and crawl internal pages to automate form requests and iteratively scrape paginated search results.


Link: http://eplanning.ie

This app successfully enables users to extract all recieved applications from planning application lists within specific time periods. This is achieved in a manner such that it would be possible to extract each individual agent's contact details (e.g. name, address, fax number, phone number and email) from HTML tables as a csv file (items.json), who are responsible for each respective planning application. 


## Installation
```
pip install scrapy

scrapy crawl eplanning -o items.json
```