import re


sentence_1 = "The Hubble.Space.Telescope (often referred to as HST or " \
             "Hubble) is a space telescope that was launched into low Earth " \
             "orbit in 1990 and remains in operation...."

new_sentence_1 = re.sub(r'(?<=\w)\.(?=\w)', ' ', sentence_1)
new_sentence_1 = re.sub(r'\.(?!$)', '', new_sentence_1)

sentence_2 = " It was not the first space telescope, but it is one of the " \
             "largest and most versatile, renowned both as a vital research " \
             "tool and as a public relations boon for astronomy."

sentence_3 = " The Hubble telescope is named after astronomer Edwin Hubble " \
             "and is one of NASA's Great Observatories....."

new_sentence_3 = re.sub(r'\.(?!$)', '', sentence_3)

sent_4_5 = " The Space Telescope Science Institute (STScI) selects Hubble's " \
           "targets and processes the resulting data, while the Goddard " \
           "Space Flight Center (GSFC) controls the spacecraft.A commission " \
           "headed by Lew Allen, director of the Jet Propulsion Laboratory, " \
           "was established to determine how the error could have arisen."

new_sent_4_5 = re.sub(r'(?<=[.,])(?=\S)', ' ', sent_4_5)

sentence_6 = " The Allen Commission found that a reflective null corrector, " \
             "a testing device used to achieve a properly shaped " \
             "non-spherical mirror, had been incorrectly assembled—one lens " \
             "was out of position by 1.3 mm (0.051 in)."

text = sentence_1 + sentence_2 + sentence_3 + sent_4_5 + sentence_6
print(text)
print("----------")

new_text = new_sentence_1 + sentence_2 + new_sentence_3 + new_sent_4_5 + \
           sentence_6
print(new_text)
print("----------")

split_text = re.split(r'\.\s+', new_text)
print(split_text)
