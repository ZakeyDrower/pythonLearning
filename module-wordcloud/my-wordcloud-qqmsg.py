# https://blog.csdn.net/FrankieHello/article/details/79531489
from scipy.misc import imread
from wordcloud import WordCloud
#import wordcloud.wordcloud as wordCloud
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from scipy.misc import imread
import re
import os

datafolder = 'F:/pythonLearn/module-wordcloud/data/'
src_file = 'msg-201414.txt'

def save2file(text):
    file = open(datafolder + os.path.splitext(src_file)[0] + '-jb.txt', 'w')
    file.write(text)
    file.close()
    return file

def createText():  
    record_file = open(datafolder + src_file, 'r', encoding='utf-8')  
    ignore_file = open(datafolder + '../ignore-words.txt','r', encoding='utf-8')  

    line_list = []  
    for line in record_file:  
        if line.isspace():  
            continue  
        if re.match(r'(\d{4}-\d{1,2}-\d{1,2})',line[:10]) is not None:  
            continue  
        line_list.append(line.strip())  
  
    stop_words = set(line.strip() for line in ignore_file)  
  
    word_list = []  
  
    for line in line_list:  
        word_map = pseg.cut(line)  
        for word, type in word_map:  
            if word not in stop_words and type == 'n':  
                word_list.append(word)  
  
    record_file.close()  
    ignore_file.close()  
    return ' '.join(word_list)  

def createCloud(text):  
    mask_img = imread(datafolder + '../bg.jpg')  
    #wordCloud = WordCloud(font_path=datafolder + '../sy-heiti.otf', background_color='#fff', mask=mask_img).generate(text)  
    wordCloud = WordCloud(font_path=datafolder + '../sy-heiti.otf', background_color="white",width=8000, height=4500, margin=20).generate(text)      
    WordCloud.to_file(wordCloud, os.path.splitext(datafolder+'../output/'+src_file)[0] + '-out.png')
    plt.imshow(wordCloud)  
    plt.axis('off')  
    plt.show()

# if __name__ == '__main__':  
#     txt = createText()  
#     file = save2file(txt)
#     #file = datafolder + src_file + '-jb.txt'
#     createCloud(txt) 

if __name__ == '__main__': 
    with open('F:\\pythonLearn\\module-wordcloud\\data\\msg-201414--jb.txt', 'r') as rfile:
        print('text loading ... ... ')
        txt = rfile.read()
        print('text loaded!')
        print('pic generating ... ... ')        
        createCloud(txt)
    rfile.close()