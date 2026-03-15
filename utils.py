import re

def parse_names(text):

    names=[n.strip() for n in re.split("[,\n]",text) if n.strip()]

    return names,len(names)


def limit_words(text,max_words=120):

    words=text.split()

    return " ".join(words[:max_words])