<h1 align="center">Instagram_Crawler</h1>
<p align="center">Extract Data From Instagram Using Selenium/Python.</p>

<p align="center">
  <a href="https://bit.ly/3iaSD77">Detail Info</a> •
  <a href="#description">Description</a> •
  <a href="#install">Install Libraries</a> •
  <a href="#get-started">Get Started</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#stack">Stack</a> •
  <a href="#contribute">Contribute</a>
</p>

<p align="center">
  <img src="/images/instagram_logo.png" width=50% height=auto alt="logo_image"/>
</p>

<h2 align="center">Description</h2>

**Instagram Crawler** is a python module for crawling Instagram data.

⚠️ _If you access more than a certain number of posts on Instagram, the posts are no longer loaded. Therefore, about 100 to 300 posts can be crawled._

<h2 align="center">Install</h2>

Simply run :

```console
pip install -r requirements.txt
```

---

You can also install additional dependencies (for running examples, generating documentation, etc...) with :
⚠️ _**Python ≥ 3.6** required_

<h2 align="center">Get Started</h2>

The full documentation contains more detailed tutorials, but to get a taste of the framework, you can take a look at the `examples` folder.  
Let's look at the easy example, `bart_easy.py`. You can run the example with following command :

```console
$ python3 main.py --id=[user_id] \
  --password=['user_password']\
  --hash_tag=[hash_tag] \
  --display=[0 or 1] \
  --extract_num=[extract_num: int] \
  --login_option=[instagram or facebook] \
  --extract_file=[file name] \
  --extract_tag_file=[tag file name] \
  --driver_path=[chromedriver path]
```



```python
# -*- coding:utf-8 -*-

import argparse
from instagram_crawler.metadata import EXTRACT_NUM, LOGIN_OPTION, SAVE_FILE_NAME, SAVE_FILE_NAME_TAG
from instagram_crawler.extract_data import crawling_instagram


parser = argparse.ArgumentParser(description='Crawling Instagram Post - Comment',
                                 formatter_class=argparse.RawTextHelpFormatter)


def get_arguments():
    parser.add_argument("--driver_path", 
                        help="selenium chrome driver path", 
                        required=True, type=str)

    parser.add_argument("--id", 
                        help="instagram or facebook id", 
                        required=True, type=str)

    parser.add_argument("--password", 
                        help="instagram or facebook password", 
                        required=True, type=str)

    parser.add_argument("--hash_tag", 
                        help="The hashtag you want to extract.", 
                        required=True, type=str)

    parser.add_argument("--display",
                        help="display selenium chromedriver or not 0 or 1",
                        required=True, type=int)


    parser.add_argument("--extract_num", 
                        help="The number of posts I want to extract.", 
                        default=EXTRACT_NUM, type=int)

    parser.add_argument("--login_option", 
                        help="select login account [facebook, instagram]", 
                        default=LOGIN_OPTION, type=str)

    parser.add_argument("--extract_file",
                        help="set extract file name", 
                        default=SAVE_FILE_NAME, type=str)

    parser.add_argument("--extract_tag_file",
                        help="set extract tag file name", 
                        default=SAVE_FILE_NAME_TAG, type=str)

    _args = parser.parse_args()

    return _args


def instagram_main():
    args = get_arguments()
    is_file_save, is_tag_file_save = crawling_instagram(args=args)

    if is_file_save:
        print("file save success - {}".format(args.extract_file))

    if is_tag_file_save:
        print("file save success - {}".format(args.extract_tag_file))


if __name__ == "__main__":
    instagram_main()
```

<h2 align="center">Stack</h2>

#### [Pandas](https://pandas.pydata.org/)

Library used for make result csv file.

#### [Selenium](https://github.com/SeleniumHQ)

Library used for extract instagram data in chrome browser.

<h2 align="center">Contribute</h2>

To contribute, simply clone the repository, add your code in a new branch and open a pull request !
