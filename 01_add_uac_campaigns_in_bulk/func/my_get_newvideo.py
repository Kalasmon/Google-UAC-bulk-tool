#!/usr/bin/env python
# -*- coding: utf-8 -*-

from googleads import adwords
import csv
import pickle
import my_init_adwordsclient as mia
import my_init as mi



PAGE_SIZE = 10000

def myGetVideolist(client, customerid):
  # Initialize appropriate service.
  media_service = client.GetService('MediaService', version='v201802')

  # Construct selector and get all images.
  offset = 0
  selector = {
      'fields': ['MediaId'],#, 'Type', 'Width', 'Height', 'MimeType'
      'predicates': [{'field': 'Type', 'operator': 'IN', 'values': ['VIDEO']}],
      'paging': {
          'startIndex': str(offset),
          'numberResults': str(PAGE_SIZE)
      }
  }
  more_pages = True
  
  page = media_service.get(selector)
  
  videolist = []
  
  if 'entries' in page:
      for video in page['entries']:
          videolist.append(video['mediaId'])
  
  
  newlist = deduplicate(videolist, customerid)
  # newlist = videolist
  
  print 'newlists: '
  print newlist
  
  return newlist
  


def deduplicate(videolist, customerid):
    
    oldlist = pickle.load(open(mi.myinitvdodir() + customerid + '_2.txt', "r"))
    
    newlist = list(set(videolist) - set(oldlist))

    pickle.dump(oldlist, open(mi.myinitvdodir() + customerid + '_1.txt', "w"))
    
    pickle.dump(videolist, open(mi.myinitvdodir() + customerid + '_2.txt', "w"))
    
    return newlist



def initvdofile(client, customerid):
    
    newlist = myGetVideolist(client, customerid)
    
    pickle.dump(newlist, open(mi.myinitvdodir() + customerid + '_2.txt', "w"))
  
    
'''
  while more_pages:
    page = media_service.get(selector)

    # Display results.
    if 'entries' in page:
      for image in page['entries']:
        print image
        try:
          dimensions = dict([(entry['key'], entry['value'])
                             for entry in image['dimensions']])
        except AttributeError:
          dimensions = {'FULL': {'height': 0, 'width': 0}}
        if image['type'] == 'IMAGE':
          print ('%s with id "%s", dimensions \'%sx%s\', and MimeType "%s"'
                 ' was found.' % (image['type'], image['mediaId'],
                                  dimensions['FULL']['height'],
                                  dimensions['FULL']['width'],
                                  image['mimeType']))
        elif image['type'] == 'VIDEO':
          print ('%s with id "%s" was found.' % (image['type'],
                                                 image['mediaId']))
    else:
      print 'No images/videos were found.'
    offset += PAGE_SIZE
    selector['paging']['startIndex'] = str(offset)
    more_pages = offset < int(page['totalNumEntries'])
'''


if __name__ == '__main__':
  # Initialize client object.
  test_customer_id = '829-365-9721'
  test_client = mia.MyInitAdwordsClient(test_customer_id)
  initvdofile(test_client,test_customer_id)
  
  # l = myGetVideolist(test_client, test_customer_id)
  
  # oldlist = pickle.load(open(mi.myinitvdodir() + test_customer_id + '_2.txt', "r"))
  # print 'new l'
  # print l
