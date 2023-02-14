# def book_info(name, author, genre, rel_data, lang, rang='oq',*boshqa):
    
#     book = {
#         'name': name,
#         'author': author,
#         'genre': genre,
#         'rel_data':rel_data,
#         'lang': lang,
#         'rang':rang,
#         "boshqa": etc
#     }
    
#     return book

# info = book_info('Mehrobdan chayon','Abdulla Qodiriy','drama','1929','uzbek','red','maslahat')

# print(info.items())

def info(**full):
    
    return full

fullInfo = info(ism="husniddin",familiya="Mehmonov")

print(type(fullInfo))