a =  [1,2,3,4,5,]
print(a)

a[2:4] = ['Three','Four','Five']
print(a)

rssitem = {'title' :'Pythonの勉強前',
            'link' :'http://host.to/blog/entry',
            'dc:date':'2016-05-16T13:24:04Z'}
rssitem.update({'title'  :'Pythonを勉強中',
                'dc:creator':'someone'})

print(rssitem.keys())
print(rssitem)

                                                                                          
