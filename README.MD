# Craigslist Spider
This is a spider to scrap from the Craigslist website. It scraps data from every list in selected catagroy, including date, title, url, description, images, and then output data to csv or json file.

## Usage
```bash
scrapy crawl crag -a category='https://XXXXX.craigslist.org/search/XXXXX' -o result.json
```