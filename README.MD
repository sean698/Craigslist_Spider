# Craigslist Spider
This program using Scrapy to crawl the Craigslist website. It scraps data from every post in selected categroy, including date, title, url, description, images, and then output data to csv or json file.

## Usage
```bash
scrapy crawl crag -a category='https://XXXXX.craigslist.org/search/XXXXX' -o result.json
```
