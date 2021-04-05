import os
from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


# przeniosłem tą metodę z innego programu
def levenshtein_distance(s, t):
    n = range(0, len(s) + 1)
    for y in range(1, len(t) + 1):
        l, n = n, [y]
        for x in range(1, len(s) + 1):
            n.append(min(l[x] + 1, n[-1] + 1, l[x - 1] + ((t[y - 1] != s[x - 1]) and 1 or 0)))
    return n[-1]


FILENAMES = 'Filenames.txt'
FAVORITES = 'Favorites.txt'
FOLDER = '/Users/matveidzebysh/Desktop/Skrypty/PyCharm/'

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
categoryLinksList = ['https://www.sciencedaily.com/news/top/science/',
                     'https://www.sciencedaily.com/news/health_medicine/',
                     'https://www.sciencedaily.com/news/mind_brain/',
                     'https://www.sciencedaily.com/news/living_well/',
                     'https://www.sciencedaily.com/news/matter_energy/',
                     'https://www.sciencedaily.com/news/space_time/',
                     'https://www.sciencedaily.com/news/computers_math/',
                     'https://www.sciencedaily.com/news/plants_animals/',
                     'https://www.sciencedaily.com/news/earth_climate/',
                     'https://www.sciencedaily.com/news/fossils_ruins/',
                     'https://www.sciencedaily.com/news/science_society/',
                     'https://www.sciencedaily.com/news/business_industry/',
                     'https://www.sciencedaily.com/news/education_learning/',
                     'https://www.sciencedaily.com/news/strange_offbeat/']
categories = ['Top science news', 'Health & Medicine', 'Mind & Brain', 'Living well', 'Matter & Energy', 'Space & Time',
              'Computers & Math', 'Plants & Animals', 'Earth & Climate', 'Fossils & Ruins', 'Society',
              'Business industry',
              'Education & Learning', 'Strange offbeat']
FAVORITESET = False  # zmienna służy do sprawdzenia czy pracujemy z listą ulubionych w metodzie removeFavorite


def getCategoryLink(category):
    index = -1
    for i in categories:
        if i == category:
            index = categories.index(i)
    return categoryLinksList[index]


def getTopLinksListFromCategoryLink(category):
    topList = []
    response = requests.get(category, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])
    topList.append('https://www.sciencedaily.com' + links[19])
    topList.append('https://www.sciencedaily.com' + links[20])
    topList.append('https://www.sciencedaily.com' + links[21])
    topList.append('https://www.sciencedaily.com' + links[22])
    return topList


def getLatestLinksListFromCategoryLink(category):
    latestList = []
    response = requests.get(category, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])
    latestList.append('https://www.sciencedaily.com' + links[23])
    latestList.append('https://www.sciencedaily.com' + links[24])
    latestList.append('https://www.sciencedaily.com' + links[25])
    latestList.append('https://www.sciencedaily.com' + links[26])
    latestList.append('https://www.sciencedaily.com' + links[27])
    latestList.append('https://www.sciencedaily.com' + links[28])
    latestList.append('https://www.sciencedaily.com' + links[29])
    latestList.append('https://www.sciencedaily.com' + links[30])
    latestList.append('https://www.sciencedaily.com' + links[31])
    latestList.append('https://www.sciencedaily.com' + links[32])
    return latestList


def getTopArticleListFromCategoryLink(category):
    response = requests.get(category, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    topArticles = []
    iter = 0
    for i in soup.find_all('h3', class_='latest-head'):
        if iter < 4:
            topArticles.append(i.getText())
            iter += 1
    return topArticles


def getLatestArticlesFromCategoryLink(category):
    response = requests.get(category, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    ar = soup.find('ul', id='featured_shorts').text
    latestArticles = ar.split('\n')
    return latestArticles


def getTextFromLink(link):
    response = requests.get(link, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('h1', id='headline').text + '.txt'
    if article in files:
        messagebox.showerror('Error has occured', 'Article was already downloaded')
        return None
    files.append(article)
    writeFilenames(files)
    date = 'Date : ' + soup.find('dd', id='date_posted').text
    source = 'Source : ' + soup.find('dd', id='source').text
    summary = 'Summary : ' + soup.find('dd', id='abstract').text
    intro = soup.find('p', id='first').text
    t = soup.find('div', id='text').text
    result = [article, date, source, summary, 'Link: ' + link, '\n', intro]
    res = t.split('\n')
    res = list(filter(None, res))
    for i in res:
        result.append(i)
    writeTextToFile(result)
    return result


def writeTextToFile(text):
    file = open(FOLDER + text[0], 'w')
    file.write('\n'.join(text))


def writeFilenames(files):
    file = open(FOLDER + FILENAMES, 'w')
    file.write('\n'.join(files))


def readFilenames():
    try:
        return open(FOLDER + FILENAMES).read().split('\n')
    except Exception:
        return []


def writeFavorites(filenames):
    file = open(FOLDER + FAVORITES, 'w')
    file.write('\n'.join(filenames))


def readFavorites():
    try:
        return open(FOLDER + FAVORITES).read().split('\n')
    except Exception:
        return []


def addFavorite():
    try:
        filename = filename_box.get(filename_box.curselection())
        if filename in favorites:
            return messagebox.showerror('Error has occurred', 'Article is already in favorites')
        favorites.append(filename)
        writeFavorites(favorites)
        return messagebox.showinfo('Favorite list', 'Article was successfully added to favorites')
    except Exception:
        messagebox.showerror('Error has occurred', 'You did not choose any article')


def openText():
    try:
        filename = filename_box.get(filename_box.curselection())
        txt = fileToString(open(FOLDER + filename).read().split('\n'))
        output.config(text=txt)
    except Exception:
        messagebox.showerror('Error has occured', 'You did not choose any article')


def fileToString(file):
    str = ''
    for i in file:
        str += i + "\n"
    return str


def topBox():
    global variable
    category = variable.get()
    link = getCategoryLink(category)
    topArticleBox.delete(0, 'end')
    topArticles = getTopArticleListFromCategoryLink(link)
    [topArticleBox.insert(i, a) for i, a in enumerate(topArticles)]


def topLoad():
    global variable
    category = variable.get()
    link = getCategoryLink(category)
    links = getTopLinksListFromCategoryLink(link)
    try:
        idx = topArticleBox.curselection()[0]
        text = getTextFromLink(links[idx])
        if text is not None:
            filename_box.insert(END, text[0])
            messagebox.showinfo('Top article download', 'Article was successfully downloaded')
    except Exception:
        messagebox.showerror('Error has occured', 'You did not choose any article')


def latestBox():
    global variable
    category = variable.get()
    link = getCategoryLink(category)
    latestArticleBox.delete(0, 'end')
    latestArticles = getLatestArticlesFromCategoryLink(link)
    [latestArticleBox.insert(i, a) for i, a in enumerate(latestArticles)]


def latestLoad():
    global variable
    category = variable.get()
    link = getCategoryLink(category)
    links = getLatestLinksListFromCategoryLink(link)
    try:
        idx = latestArticleBox.curselection()[0]
        text = getTextFromLink(links[idx])
        if text is not None:
            filename_box.insert(END, text[0])
            messagebox.showinfo('Latest article download', 'Article was successfully downloaded')
    except Exception:
        messagebox.showerror('Error has occured', 'You did not choose any article')


def deleteArticle():
    try:
        idx = filename_box.curselection()[0]
        ans = messagebox.askyesno('Delete file', 'Do you want to delete file?')
        if ans:
            filename = files.pop(idx)
            filename_box.delete(idx)
            os.remove(FOLDER + filename)
            writeFilenames(files)
            messagebox.showinfo('File deleted', f'Article {filename} was successfully deleted')
    except Exception:
        messagebox.showerror('Error has occured', 'You did not choose any file')


def showFavorites():
    filename_box.delete(0, 'end')
    [filename_box.insert(i, a) for i, a in enumerate(favorites)]
    global FAVORITESET
    FAVORITESET = True


def downloads():
    filename_box.delete(0, 'end')
    files = readFilenames()
    [filename_box.insert(i, a) for i, a in enumerate(files)]
    global FAVORITESET
    FAVORITESET = False


def removeFavorite():
    if not FAVORITESET:
        return messagebox.showerror('Error has occurred',
                                    'To remove favorite,you first need to open Favorites using option "Show favorites"')
    try:
        idx = filename_box.curselection()[0]
        ans = messagebox.askyesno('Removing', 'Do you want to remove atricle from favorites?')
        if ans:
            filename = favorites.pop(idx)
            filename_box.delete(idx)
            writeFavorites(favorites)
            messagebox.showinfo('Article removed', f'Article {filename} was successfully removed from favorites')
    except Exception:
        messagebox.showerror('Error has occurred', 'You did not choose any file')


def show():
    messagebox.showinfo(
        "Instruction",
        "To download articles use appropriate buttons\n "
        "With every change of category Top and Latest lists must be updated"
        " with the help of 'Get top' and 'Get latest' buttons")


def search():
    res = []
    helper = {}
    name = searchVar.get()
    minimum = levenshtein_distance(name, files[0])
    for i in files:
        tmp = levenshtein_distance(name, i)
        helper[i] = tmp
        if tmp < minimum:
            minimum = tmp
    for key in helper.keys():
        if helper[key] == minimum:
            res.append(key)
    filename_box.delete(0, 'end')
    [filename_box.insert(i, a) for i, a in enumerate(res)]


if __name__ == '__main__':
    root = Tk()
    root.title('Projekt')
    root.geometry('1600x1200')

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Show downloads", command=downloads)
    filemenu.add_command(label="Open article", command=openText)
    filemenu.add_command(label="Delete article", command=deleteArticle)
    filemenu.add_command(label="Add to favorites", command=addFavorite)
    menubar.add_cascade(label="Downloads", menu=filemenu)

    favmenu = Menu(menubar, tearoff=0)
    favmenu.add_command(label="Show favorites", command=showFavorites)
    favmenu.add_command(label="Remove from favorites", command=removeFavorite)
    menubar.add_cascade(label="Favorites", menu=favmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instruction", command=show)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    left_frame = Frame(root)
    left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    right_frame = Frame(root)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)
    root.grid_rowconfigure(0, weight=1)

    # Left frame
    searchVar = StringVar()
    search_entry = Entry(left_frame, textvariable=searchVar)
    search_entry.grid(row=0, column=0, sticky='nsew', pady=5, padx=5)

    searchBtn = Button(left_frame, text='Search in downloads', command=search)
    searchBtn.grid(row=0, column=1, sticky='nsew', padx=5)

    filename_box = Listbox(left_frame)
    filename_box.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

    topArticleBox = Listbox(left_frame)
    topArticleBox.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

    latestArticleBox = Listbox(left_frame)
    latestArticleBox.grid(row=4, column=1, columnspan=2, sticky='nsew', padx=5, pady=5)

    categoryLabel = Label(left_frame, text='Choose category: ').grid(row=2, column=0, sticky='nsew', padx=1, pady=2)

    variable = StringVar(left_frame)
    variable.set(categories[0])
    w = OptionMenu(left_frame, variable, *categories)
    w.grid(row=2, column=1, sticky='nsew', padx=1, pady=2)

    getTopBtn = Button(left_frame, text='Get Top', command=topBox)
    getTopBtn.grid(row=3, column=0, sticky='nsew', padx=5)

    getLatestBtn = Button(left_frame, text='Get Latest', command=latestBox)
    getLatestBtn.grid(row=3, column=1, sticky='nsew', padx=5)

    loadTopBtn = Button(left_frame, text='Load from Top', command=topLoad)
    loadTopBtn.grid(row=5, column=0, sticky='nsew', padx=5)

    loadLatestBtn = Button(left_frame, text='Load from Latest', command=latestLoad)
    loadLatestBtn.grid(row=5, column=1, sticky='nsew', padx=5)

    left_frame.grid_columnconfigure(0, weight=1)
    left_frame.grid_columnconfigure(1, weight=1)
    left_frame.grid_rowconfigure(1, weight=1)
    left_frame.grid_rowconfigure(2, weight=0)
    left_frame.grid_rowconfigure(3, weight=0)
    left_frame.grid_rowconfigure(4, weight=1)

    # Right frame
    output = Label(right_frame)
    output.config(text='', justify=LEFT, wraplength=700, padx=20)
    output.grid(row=1, column=0, rowspan=3, columnspan=3, sticky='nsew')

    openBtn = Button(right_frame, text='Open', command=openText)
    openBtn.grid(row=0, column=1, sticky='nsew', padx=5)

    favBtn = Button(right_frame, text='Add to favorites', command=addFavorite)
    favBtn.grid(row=0, column=0, sticky='nsew', padx=5)

    delBtn = Button(right_frame, text='Delete', command=deleteArticle)
    delBtn.grid(row=0, column=2, sticky='nsew', padx=5)

    files = readFilenames()
    [filename_box.insert(i, a) for i, a in enumerate(files)]

    favorites = readFavorites()
    root.mainloop()
