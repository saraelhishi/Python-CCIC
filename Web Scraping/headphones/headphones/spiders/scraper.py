#!/usr/bin/env python
# coding: utf-8

# In[1]:


######################### Building a Web Craweler using Scrapy #######################################
######################################################################################################


# In[2]:


import scrapy


# In[3]:


# create a scraper class
class HeadphoneSpider(scrapy.Spider): #inherits from scrapy spiders
    name = 'headphones'  # When we will run our spider form terminal, 
                        # you will use the name of the spider to start crawling the web. 
    
    # define a function that send a request to the websites we will scrape
    def start_requests(self):
        urls = [
            'https://www.jbl.com/headphones/'
        ]   	# list to enter our urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 
            
    def parse(self, response):
        img_urls = response.css('img::attr(src)').extract()
        with open('urls.txt', 'w') as f: 
            for u in img_urls:
                f.write(u + "\n")


# In[ ]:




