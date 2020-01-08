##S1: Create a new project using 

```
scrapy startproject goodreads
cd goodreads
scrapy genspider goodread www.goodreads.com/quotes
```

##S2: Navigate to goodread.py and update it with the file present

##S3: Run the crawler using
```
scrapy crawl goodread -o quotes.csv
```
