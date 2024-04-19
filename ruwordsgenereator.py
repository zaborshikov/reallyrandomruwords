from random import random as rand
from typing import List


def generate_word(word_length: int, letters: List[str] = letters, sfreqs: List[float] = sfreqs) -> str:

    '''
    Generate a word with fixed length

    Args:
      word_length (int): length of the word
      Optional:
        letters: letters of alphabet
        sfreqs: sum of freqs in your alphabet. For example, when frequency of your letters is (0.25, 0.25, 0.5), sfreqs for that is (0.25, 0.5, 1). As code: sfreq[i] = sum(freq[:i + 1])

    Returns:
      word (str): generated word
    '''
    letters = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')
    sfreqs = (0.0801, 0.096, 0.1414, 0.15839999999999999, 0.18819999999999998, 0.27269999999999994, 0.27309999999999995, 0.2825, 0.299, 0.3725, 0.3846, 0.4195, 0.46349999999999997, 0.4956, 0.5626, 0.6723, 0.7004, 0.7477, 0.8024, 0.865, 0.8912, 0.8938, 0.9035000000000001, 0.9083000000000001, 0.9227000000000001, 0.93, 0.9336000000000001, 0.934, 0.9530000000000001, 0.9704, 0.9736, 0.98, 1.0001)

    word = ''
    for _ in range(word_length):
        r = rand()*sfreqs[-1]
        cumulative = 0
        for sfreq, letter in zip(sfreqs, letters):
            if r < sfreq:
                word += letter
                break
    return word
