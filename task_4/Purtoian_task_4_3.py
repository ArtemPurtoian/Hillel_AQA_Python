import re


text = "The Hubble.Space.Telescope (often referred to as HST or Hubble) is " \
       "a space telescope that was launched into low Earth orbit in 1990 " \
       "and remains in operation.... It was not the first space telescope, " \
       "but it is one of the largest and most versatile, renowned both as a " \
       "vital research tool and as a public relations boon for astronomy. " \
       "The Hubble telescope is named after astronomer Edwin Hubble and is " \
       "one of NASA's Great Observatories..... The Space Telescope Science " \
       "Institute (STScI) selects Hubble's targets and processes the " \
       "resulting data, while the Goddard Space Flight Center (GSFC) " \
       "controls the spacecraft.A commission headed by Lew Allen, director " \
       "of the Jet Propulsion Laboratory, was established to determine how " \
       "the error could have arisen. The Allen Commission found that a " \
       "reflective null corrector, a testing device used to achieve a " \
       "properly shaped non-spherical mirror, had been incorrectly " \
       "assembled—one lens was out of position by 1.3 mm (0.051 in)."

clean_text_1 = re.sub(r'\.{2,}', '.', text)
clean_text_2 = re.sub(r'\.', ' ', clean_text_1, count=2)
clean_text_3 = re.sub(r'\.(?=[A-Z])', '. ', clean_text_2)

split_text = re.split(r'(?<=[.!?])\s+', clean_text_3)
print(split_text)
