#!/usr/bin/env python
# -*- coding: utf-8 -*-


import func.my_init as mi
import func.my_init_adwordsclient as mia
import func.my_upload_uaccampaign as muu
import func.my_get_medialist as mgm


if __name__ == '__main__':

  listtpye = 'ybm'                # all, colour_wolf, muslin, test, oumei, ida, ina, jpa, kra, cna
  bantype = 'low'                 # low, mid, nan
  oslist = mi.myinitostype('both')    # adr, ios, both
  imgtype = 'all'                         # geo, all
  mediatype = 'ga'                # gb, gy, ga

  imgid = 'INO0125' 
  # 确认有没带上图片！
  # 确认有没换好文案！

  
  
  
  for each_ostype in oslist:
      
    CLIENT_CUSTOMER_ID = mi.myinitcustomerid_div(each_ostype)
    adwords_client = mia.MyInitAdwordsClient(CLIENT_CUSTOMER_ID)
    mediaidlist = mgm.MyGetMedia(adwords_client, CLIENT_CUSTOMER_ID, mediatype)
    geolist = mi.myinitgeolist(each_ostype, listtpye)
    banlist = mi.myinitbanlist(each_ostype, bantype)
    
    for each_geo in geolist:

      if each_geo in banlist:
        continue
      else:
        muu.my_upload_uaccampaign(adwords_client, each_ostype, each_geo, mediatype, imgid, mediaidlist)
    

      

      
      
      















  
