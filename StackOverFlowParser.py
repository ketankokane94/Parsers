import scrapy
import urllib.request


def stackoverflowURL():
    ItemToBeSearched = "natural%20Language%20processing"
    totalPosts = []
#view-source:http://stackoverflow.com/search?page=1&tab=Votes&q=natural%20Language%20processing
    totalPages = ['http://stackoverflow.com/search?page='+str(page)+'&tab=Votes&pagesize=15&q='+ItemToBeSearched for page in (range(1,2))]
    #5741
    
    for page in totalPages:
        print(page)
        data = urllib.request.urlopen(page).read()
        print (data)
        hxs = scrapy.Selector(text=data)
        totalPosts += hxs.xpath('//div[@class = "result-link"]/span/a/@href').extract()
        print (hxs.xpath('//div[@class = "result-link"]/span/a/@href').extract())
    '''    
    with open("stackoverflowURL.txt", "a") as myfile:
        for post in totalPosts:
            try:
                post = post + '\n'
                myfile.write(post)
            except:
                pass
    '''



stackoverflowURL()