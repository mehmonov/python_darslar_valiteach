def book_info(name, author, genre, rel_data, lang, rang='oq',**etc):  
    """
        Bu funksiya orqali siz kitoblar uchun ma'lumotni olishingiz mumkin
    """
    book = {
        'name': name,
        'author': author,
        'genre': genre,
        'rel_data':rel_data,
        'lang': lang,
        'rang':rang,
        "boshqa": etc
    }
    
    print(book)

# info = book_info('Mehrobdan chayon','Abdulla Qodiriy','drama','1929','uzbek','red','maslahat')

