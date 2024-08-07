d = {'text': '"Dr. Paul Hammond, a renowned neurologist at Johns Hopkins University, has recently published a paper in the prestigious journal '
         '\\"Nature Neuroscience\\". \nHis research focuses on a rare genetic mutation, found in less than 0.01% of the population, that appears '
         'to prevent the development of Alzheimer\'s disease. Collaborating with researchers at the University of California, San Francisco, the team '
         'is now working to understand the mechanism by which this mutation confers its protective effect. \nFunded by the National Institutes of Health, '
         'their research could potentially open new avenues for Alzheimer\'s treatment."',
 'entities': [{'start': 5,
               'end': 17,
               'span': 'Paul Hammond',
               'score': 0.731655478477478,
               'entity': '"scientist", '
                         '"university", '
                         '"city"'},
              {'start': 45,
               'end': 69,
               'span': 'Johns Hopkins University',
               'score': 0.9696738123893738,
               'entity': '"scientist", '
                         '"university", '
                         '"city"'},
              {'start': 350,
               'end': 389,
               'span': 'University of California, San Francisco',
               'score': 0.9662151336669922,
               'entity': '"scientist", '
                         '"university", '
                         '"city"'}]
 }
e = {'span':[],'score':[],'entity':[]}
for i in (d['entities']):
    e['span'].append(i['span'])
    e['score'].append(i['score'])
    e['entity'].append(i['entity'])
print(e)

# for i in (d['entities']):
#     e['span','score','entity'].append(i['span'],i['score'],i['entity'])