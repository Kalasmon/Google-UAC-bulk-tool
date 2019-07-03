#!/usr/bin/env python
# -*- coding: utf-8 -*-

import my_upload_image as mui
import my_get_newvideo as mgn

def MyGetMedia(client, customerid, mediatype):
    
    medialist = {}
    '''
    if mediatype == 'gb':
        medialist['youtubeVideoMediaIds'] = {}
        medialist['imageMediaIds'] = mui.MyUploadImage(client)
    elif mediatype == 'gy':
        medialist['imageMediaIds'] = {}
        medialist['youtubeVideoMediaIds'] = mgn.myGetVideolist(client, customerid)
    elif mediatype == 'ga':
    '''
    medialist['youtubeVideoMediaIds'] = mgn.myGetVideolist(client, customerid)
    medialist['imageMediaIds'] = mui.MyUploadImage(client)
    
    return medialist


'''
    if mediatype == 'gb':
        medialist['key'] = 'imageMediaIds'
        medialist['id'] = mui.MyUploadImage(client)
    elif mediatype == 'gy':
        medialist['key'] = 'youtubeVideoMediaIds'
        medialist['id'] = mgn.myGetVideolist(client, customerid)
'''