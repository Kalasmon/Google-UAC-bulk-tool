#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
- 每次只能针对一个 CID 生成一个 adwords_client，所以要批量处理 MCC 中多个帐号前必须先提取 CID 列表
'''

from googleads import adwords
from googleads import oauth2 


def MyInitAdwordsClient(client_customer_id):
    CLIENT_ID = 'xxxxxxxx'
    CLIENT_SECRET = 'xxxxxxxx'
    REFRESH_TOKEN = 'xxxxxxxx'   
    oauth2_client = oauth2.GoogleRefreshTokenClient(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
    DEVELOPER_TOKEN = 'xxxxxxxx'
    USER_AGENT = 'BG'
    adwords_client = adwords.AdWordsClient(DEVELOPER_TOKEN, oauth2_client, USER_AGENT, client_customer_id=client_customer_id)
    return adwords_client


if __name__ == '__main__':
    test_customer_id = '814-932-3139'
    client = MyInitAdwordsClient(test_customer_id)
    print client
    campaign_service = client.GetService('CampaignService', version='v201802')