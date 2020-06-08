# scrapyFormRequestDemo

This is a Scrapy project to login quotes website with formrequest  http://quotes.toscrape.com.

This project is only meant for educational purposes.

## Selection

Request Form Data


![Image of Request Form Data](https://github.com/Aniruddhsinh03/scrapyFormRequestDemo/blob/master/screenshots/requestform_2.png)

Csrf_token Selection


![Image of Csrf Token](https://github.com/Aniruddhsinh03/scrapyFormRequestDemo/blob/master/screenshots/requestForm1.jpg)

## Request data

This project Login with POST request.
The extracted data looks like this sample:

    
        'Url': 'http://quotes.toscrape.com/login',
        'Form Data': 'csrf_token': csrf_token,
                      'username': 'foobar',
                       'password': 'foobar'
        
    


## Spiders

This project contains one spider and you can list them using the `list`
command:

    $ scrapy list
    scrapyFormRequestDemoSpider

Spider login with form data.




## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl scrapyFormRequestDemoSpider


