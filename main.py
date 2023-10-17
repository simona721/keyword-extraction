from rake_nltk import Rake


text = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis justo ac est rhoncus posuere quis quis enim. Morbi sit amet semper tellus, id commodo nunc. Donec in sem vitae nulla dapibus interdum. Nam dui justo, pretium nec convallis pulvinar, fringilla eget metus. Ut et mauris maximus odio auctor semper. """


r = Rake()
r.extract_keywords_from_text(text)

keywordExtracted = r.get_ranked_phrases_with_scores()
print(keywordExtracted)

