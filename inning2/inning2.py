# -*- coding: utf-8 -*-
import sys
import os
import gzip
import re
from collections import Counter
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from toolbox import file_tool


def show_samples(samples, sample_count=5):
    for item in samples[:sample_count]:
        print(item)
        print("-" * 50)


def main(path=""):
    tweets_file = path
    if not tweets_file:
        tweets_file = os.path.join(os.path.dirname(__file__), "../dataset/tweets.txt.gz")

    if os.path.splitext(tweets_file)[1].lower() != ".gz":
        raise Exception("file extension is not .gz ({0}). please confirm file format.".format(tweets_file))

    tweets = []
    with gzip.open(tweets_file, "rb") as f:
        content = f.read()
        decoded = content.decode("utf-8")
        tweets = decoded.split("\r\n")  # tweets are separated by \r\n (\n is used for cr in tweet)

    # knock11: extract tweet which includes "拡散希望"
    kakusan_kibou = [t for t in tweets if t.find("拡散希望") > -1]
    print('knock11. show tweets whick includes "拡散希望"')
    show_samples(kakusan_kibou)

    # knock12: extract tweet which ends with "なう"
    ends_with_now = [t for t in tweets if t.endswith("なう")]
    print('knock12. show tweet which ends with "なう"')
    show_samples(ends_with_now)

    # knock13: extract retweet comment
    retweet_with_comment = [t[:t.find("RT @")] for t in tweets if t.find("RT @") > 0]
    print('knock13. show retweet with comment')
    show_samples(retweet_with_comment)

    # knock14: extract username
    user_pattern = r"@\w+"
    users = Counter()
    for t in tweets:
        for u in re.findall(user_pattern, t):
            users[u] += 1

    print('knock14. show users in tweet ({0} users found. show top 10).'.format(len(users.most_common())))
    print(users.most_common(10))

    # knock15: replace user name to link of user page
    replaced_to_link = []
    for t in tweets:
        replaced = re.sub(user_pattern, lambda m: '<a href="https://twitter.com/{0}">{0}</a>'.format(m.group(0)), t)
        if t != replaced:
            replaced_to_link.append(replaced)

    print('knock15. show tweets that replaced user name to link.')
    show_samples(replaced_to_link)

    # knock15: extract some bracket pattern
    upper_pattern = r"[\(|（][A-Z]+[\)|\）]"
    kanji_pattern = r"[\(|（][一-龠]+[\)|\）]"
    uppers = []
    kanjis = []

    def make_match_pair(pattern, text):
        index = 0
        matchies = re.findall(pattern, text)
        result = []
        for matched in matchies:
            to_index = text.find(matched)
            left_part = text[index:to_index].split("\n")
            result.append((left_part[-1], re.sub(r"[\(\)（）]", "", matched)))
            index = to_index
        return result

    for t in tweets:
        uppers += make_match_pair(upper_pattern, t)
        kanjis += make_match_pair(kanji_pattern, t)

    print('knock16. extract upper alphabet and kanji in bracket.')
    print(uppers[:5])
    print(kanjis[:5])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
