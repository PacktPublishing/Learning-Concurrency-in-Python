# Learning Concurrency in Python
This is the code repository for [Learning Concurrency in Python](https://www.packtpub.com/application-development/learning-concurrency-python?utm_source=github&utm_medium=repository&utm_campaign=9781787285378), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Python is a very high level, general purpose language that is utilized heavily in fields such as data science and research, as well as being one of the top choices for general purpose programming for programmers around the world. It features a wide number of powerful, high and low-level libraries and frameworks that complement its delightful syntax and enable Python programmers to create.
## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
import urllib.request
import time
t0 = time.time()
req = urllib.request.urlopen('http://www.example.com')
pageHtml = req.read()
t1 = time.time()
print("Total Time To Fetch Page: {} Seconds".format(t1-t0))
```

For this book, you will need the following software installed on your systems:

Beautiful Soup
RxPy
Anaconda
Theano
PyOpenCL

## Related Products
* [Learn Python in 7 Days](https://www.packtpub.com/application-development/learn-python-7-days?utm_source=github&utm_medium=repository&utm_campaign=9781787288386)

* [Learning Concurrent Programming in Scala - Second Edition](https://www.packtpub.com/application-development/learning-concurrent-programming-scala-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781786466891)

* [Learning Concurrent Programming in Scala](https://www.packtpub.com/application-development/learning-concurrent-programming-scala?utm_source=github&utm_medium=repository&utm_campaign=9781783281411)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
