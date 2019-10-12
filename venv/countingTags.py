import HTMLParser

#print('start tags', parser.start_tags_list)

#print(HTMLParser.MyHTMLParser.start_tags_list)

def tag_count():
    tag_count = {}
    for key in HTMLParser.MyHTMLParser.start_tags_list:
        if key not in tag_count:
            tag_count[key]=1
        else:
            tag_count[key]+=1
    print (tag_count)
    return tag_count

tag_count()





