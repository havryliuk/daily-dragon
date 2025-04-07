from daily_dragon.vocabulary import Vocabulary


def get_words_from_vocabulary(user_id):
    vocabulary = Vocabulary(user_id)
    return vocabulary.get_all_words()


if __name__ == '__main__':
    user_id = 344989590
    words = get_words_from_vocabulary(user_id)
    words_last_added = sorted(words.items(), key=lambda x: x[1]['added_on'], reverse=True)[:10]
    print(words_last_added)
