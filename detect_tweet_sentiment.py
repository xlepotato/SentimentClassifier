'''
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named
project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of
replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files
positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
You will create a csv file, which contains columns for the Number of Retweets, Number of Replies,
Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words
are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets,
and produce a graph of the Net Score vs Number of Retweets.
'''
def strip_punctuation(word):
    new_word = ""
    for char in word:
        if char not in punctuation_chars:
            new_word += char
    return new_word


def get_pos(sentences):
    count = 0
    words = sentences.split()
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in positive_words:
            count += 1
    return count


def get_neg(sentences):
    count = 0
    words = sentences.split()
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in negative_words:
            count += 1
    return count


with open("project_twitter_data.csv", "r") as data_f:
    twitter_data = data_f.readlines()


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Save the results into a csv file
with open("resulting_data.csv", "w") as out_f:
    # output the header row
    out_f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    out_f.write("\n")
    # output each of the rows:
    for lin in twitter_data[1:]:
        col = lin.split(",")
        retweets_num = col[1]
        replies_num = col[2].strip()
        p_score = get_pos(col[0]) # positive score
        n_score = get_neg(col[0]) # negative score
        net_score = p_score - n_score
        row_string = '{}, {}, {}, {}, {}'.format(retweets_num, replies_num, p_score, n_score, net_score)
        out_f.write(row_string)
        out_f.write("\n")
