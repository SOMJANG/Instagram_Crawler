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
