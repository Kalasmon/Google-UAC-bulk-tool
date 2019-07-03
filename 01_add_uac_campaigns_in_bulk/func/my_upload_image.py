#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example uploads an image.

To get images, run get_all_images.py.

The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.

"""


from googleads import adwords
import my_init
import os
import my_init_adwordsclient as mia


def MyUploadImage(client):
    
  media_service = client.GetService('MediaService', version='v201802')
  
  imgdir = my_init.myinitimgdir('all')        

  flist = os.listdir(imgdir)
      
  imageidlist = []
    
  for eachfile in flist:

    with open(imgdir + '/' + eachfile, 'rb') as image_handle:
      image_data = image_handle.read()#.decode('utf-8')

    media = [{
      'xsi_type': 'Image',
      'data': image_data,
      'type': 'IMAGE'
    }]
    media = media_service.upload(media)[0]
    
    imageidlist.append(media['mediaId'])
    
  print imageidlist
 
  return imageidlist


if __name__ == '__main__':
  # Initialize client object.
  test_customer_id = '814-932-3139'
  test_client = mia.MyInitAdwordsClient(test_customer_id)
  MyUploadImage(test_client)

