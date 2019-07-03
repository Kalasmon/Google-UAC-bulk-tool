#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
# import base64
from googleads import adwords
import my_init as mi
import my_init_adwordsclient as mia


def MyloadImages(client, image_lan, allorgeo):
    
    imgdir = mi.myinitimgdir(allorgeo) 
    
    image_lan = image_lan.decode('utf-8')    

    flist = os.listdir(imgdir)
    
    if len(flist) < 1:
        raise NoFileError
    
    imageidlist = []
    
    for eachfile in flist:

      # Initialize appropriate service.
      media_service = client.GetService('MediaService', version='v201802')

      # with open(imgdir + '/' + eachfile, 'rb') as image_handle:
      with open('C:/Python27/adwapi/01_adduaccampaign/images_all/300-250-A.gif', 'rb') as image_handle:
        print image_handle 
        # image_data = base64.encodestring(image_handle.read()).decode('utf-8')
        image_data = image_handle.read()#.decode('utf-8')
        

      # Construct media and upload image.
      media = [{
          'xsi_type': 'Image',
          'data': image_data,
          'type': 'IMAGE'
      }]
      media = media_service.upload(media)[0]

      imageidlist.append(media['mediaId'])

    return imageidlist


if __name__ == '__main__':
    test_customer_id = '814-932-3139'
    test_client = mia.MyInitAdwordsClient(test_customer_id)
    MyloadImages(test_client, '英语', 'all')
