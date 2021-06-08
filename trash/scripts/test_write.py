import csv

"""articles_titles = ['Fire', 'Hospital', 'Holidays', 'Party']
articles_texts = ['There was a fire.', 'He was ill.', 'We are going to the sea.', 'Let\'s celabrate Anna\'s Birthday!']
articles_tags = ['#fire', '#ill', '#sea', '#birthday']
articles_urls = ['https://#fire', 'https://#hospital', 'https://#holidays', 'https://#party']

with open("TEST_artciles.csv", "a") as fic:
    fic_writer = csv.writer(fic, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fic_writer.writerow(['Domaine', 'Title', 'Text', 'Tag', 'URL'])
    for title, text, tag, url in zip(articles_titles, articles_texts, articles_tags, articles_urls):
        name_domaine = str(url).split('/')
        fic_writer.writerow([name_domaine[2].upper(), title, text, tag, url])"""

url = 'https://www.cnews.fr/france'
name_domain = str(url).split('/')[3]
print(name_domain)