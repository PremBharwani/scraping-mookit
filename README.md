# <u>Scraping HelloIITK</u>

### Objective : To scrape the lecture details, and the link for the video lecture of the latest 'N' lectures of a particular course.
---

### Process:
1) <strong>First Approach</strong> [It was later told to us that this is not fair, anyways this wouldn't have been scraping. But hey, this was interesting ]
It was easy to understand that the lecture details were given by an api endpoint `'/api/<course_code_here>/lectures/summary'`. Since the HelloIITK, implements security using cookies, I got hold of the cookies when I logged in to HelloIITK site using my browser, and made the requests in the code using the obtained cookies. The rest is quite straight forward, just extract the relevant stuff from the JSON object, and you'll have the details about the lecture stored in a CSV file.
For more info : [Using API endpoint](https://github.com/PremBharwani/scraping-mookit/tree/main/using_api)

2) <strong>Second Approach</strong> : 
Made use of Selenium to reach to the desired location, and then do the processing to get the required details. So selenium is mostly used for writing tests, with its help you can simulate an user's course of actions, and then once you reach the desired location, extract the data, process it, and then save it as a CSV file. Done. For more info : [Using Selenium endpoint](https://github.com/PremBharwani/scraping-mookit/tree/main/using_selenium)
