# Scrapy_crawl_qichacha

#### Requests:

python-version: python 3.6

Make sure that scrapy has been installed in your computer.

#### Usage:

At first you need visit https://www.qichacha.com/user_login and login to get your cookie.

Then clear the cookies that exist in the cookies.txt before, and paste your own cookie into it. 

You can paste more than one cookies into it and which will make the crawler better performance beacause of the limitation of the website visiting.

Open your command window and enter the master path:

```cmd
cd Scrapy_crawl_qichacha-master
```

Then start to crawl:

```cmd
scrapy crawl qcc
```

Then follow the instructions that showing in the window.

![](C:\Users\37661\Desktop\cmd.png)

#### Note:

When crawling too fast the verification code will appear and make the program report an error, so this program set a relatively slow speed, and you can change it in the settings.py. 

When the program report an error this means that there is a verification code appear in your account, and you need to visit the URL in the browser and enter the confirmation code.



