# <u>Scraping HelloIITK</u>

### Objective : To scrape the lecture details, and the link for the video lecture of the latest 'N' lectures of a particular course.
---

### Process:
It was easy to understand that the lecture details were given by an api endpoint `'/api/<course_code_here>/lectures/summary'`. Since the HelloIITK, implements security using cookies, I got hold of the cookies when I logged in to HelloIITK site using my browser, and made the requests in the code using the obtained cookies. The rest is quite straight forward, just extract the relevant stuff from the JSON object, and you'll have the details about the lecture stored in a CSV file.

### Usage:

Please login to the HelloIITK website, using web debugging tool get hold of the cookies. And <strong>UPDATE</strong> the cookies that you found from the browser in the `scrape_config.py`. 

After updating `scrape_config.py` , run `scrape.py` using :

```$ python3 scrape.py```