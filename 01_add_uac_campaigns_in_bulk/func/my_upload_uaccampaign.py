#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import time
import my_init as mi
import my_init_adwordsclient as mia
import my_upload_image as mui


def my_upload_uaccampaign(client, ostype, geoname, mediatype, cname_id, mediaidlist):
  # Initialize appropriate services.
  campaign_service = client.GetService('CampaignService', version='v201802')

  budget_id = CreateBudget(client)

  # Create the Universal App campaign.
  universal_app_campaign = {
      ## campaign name
       'name': mediatype.upper() + '-' + cname_id + '-' + geoname.upper() + '-' + mi.myinitgbbid(ostype, geoname, mediatype)[:3] + '-' + time.strftime('%m') + time.strftime('%d'),
      # Recommendation: Set the campaign to PAUSED when creating it to stop the
      # ads from immediately serving. Set to ENABLED once you've added targeting
      # and the ads are ready to serve.
      'status': 'ENABLED',
      'advertisingChannelType': 'MULTI_CHANNEL',
      'advertisingChannelSubType': 'UNIVERSAL_APP_CAMPAIGN',
      # Set the campaign's bidding strategy. Universal app campaigns only
      # support TARGET_CPA bidding strategy.
      'biddingStrategyConfiguration': {
          # Set the target CPA to $1 / app install.
          'biddingScheme': {
              'xsi_type': 'TargetCpaBiddingScheme',
              'targetCpa': {
                  'microAmount': mi.myinitgbbid(ostype, geoname, mediatype)
              }
          },
          'biddingStrategyType': 'TARGET_CPA'
      },
      # Note that only the budgetId is required
      'budget': {
          'budgetId': budget_id
      }##,
      # Optional fields
      ##'startDate': (datetime.datetime.now() +
      ##              datetime.timedelta(1)).strftime('%Y%m%d'),
      ##'endDate': (datetime.datetime.now() +
      ##            datetime.timedelta(365)).strftime('%Y%m%d'),
     
  }

  ## upload images
  
  universal_app_campaign['settings'] = [
      # Set the campaign's assets and ad text ideas. These values will
      # be used to generate ads.
      {
          'xsi_type': 'UniversalAppCampaignSetting',
          ## appId
          'appId': mi.myinitappid(ostype),
          'appVendor': mi.myinitappvendor(ostype),
          'description1': mi.myinittxtlan(geoname)[0].decode('utf-8'),
          'description2': mi.myinittxtlan(geoname)[1].decode('utf-8'),
          'description3': mi.myinittxtlan(geoname)[2].decode('utf-8'),
          'description4': mi.myinittxtlan(geoname)[3].decode('utf-8'),
          # Optional: You can set up to 10 image assets for your campaign.
          # See upload_image.py for an example on how to upload images.
          #
          # mediaidlist['key']: mediaidlist['id']
          'imageMediaIds':mediaidlist['imageMediaIds'],
          'youtubeVideoMediaIds':mediaidlist['youtubeVideoMediaIds']
          # 'youtubeVideoMediaIds': [4535299397L, 4535299610L, 4535300798L, 4535303981L, 4536331848L, 4536332379L, 4536332388L, 4539252691L]

      }
  ]

  # Optimize this campaign for getting new users for your app.
  universal_app_campaign_setting = universal_app_campaign['settings'][0]
  universal_app_campaign_setting['universalAppBiddingStrategyGoalType'] = (
      'OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME')
  ## universal_app_campaign_setting['appVendor'] = ('VENDOR_UNKNOWN')

  # Optional: If you select the OPTIMIZE_FOR_IN_APP_CONVERSION_VOLUME goal type,
  # then also specify your in-app conversion types so AdWords can focus your
  # campaign on people who are most likely to complete the corresponding in-app
  # actions.
  #
  # Conversions type IDs can be retrieved using ConversionTrackerService.get.
  # universal_app_campaign['selectiveOptimization'] = {
  #     'conversionTypeIds': [INSERT_CONVERSION_TYPE_ID(s)_HERE]
  # }

  # Optional: Set the campaign settings for Advanced location options.
  universal_app_campaign['settings'].append({
      'xsi_type': 'GeoTargetTypeSetting',
      'positiveGeoTargetType': 'DONT_CARE',
      'negativeGeoTargetType': 'DONT_CARE'
  })

  # Construct operations and add campaigns.
  operations = [{
      'operator': 'ADD',
      'operand': universal_app_campaign
  }]

  campaigns = campaign_service.mutate(operations)['value']

  # Display results.
  if campaigns:
    for campaign in campaigns:
      print ('Universal App Campaign with name "%s" and id "%s" was added.'
             % (campaign['name'], campaign['id']))
      # Optional: Set the campaign's location and language targeting. No other
      # targeting criteria can be used for Universal App campaigns.
      SetCampaignTargetingCriteria(client, campaign, mi.myinitgeocode(geoname))
  else:
    print 'No Universal App campaigns were added.'


def CreateBudget(client):
  """Creates a budget and returns its budgetId.

  Args:
    client: An AdWordsClient instance.

  Returns:
    An int budgetId for the created Budget.
  """
  budget_service = client.GetService('BudgetService', version='v201802')

  # Create a budget.
  budget = {
      'name': 'Interplanetary Cruise App Budget #%s' % uuid.uuid4(),
      'amount': {
          'microAmount': '100000000'
      },
      'deliveryMethod': 'STANDARD', #'ACCELERATED'
      'isExplicitlyShared': False
  }

  budget_operations = [{
      'operator': 'ADD',
      'operand': budget
  }]

  # Create the budget and return its ID.
  budget_id = budget_service.mutate(budget_operations)['value'][0]['budgetId']

  return budget_id


def SetCampaignTargetingCriteria(client, campaign, geocode):
  """Sets targeting criteria for the given campaign.

  Args:
    client: An AdWordsClient instance.
    campaign: A suds object representing the campaign we wish to attach
      targeting criteria.
  """
  campaign_criterion_service = client.GetService('CampaignCriterionService')

  # Create locations. The IDs can be found in the documentation or retrieved
  # with the LocationCriterionService.
  criteria = [
      {
          'xsi_type': 'Location',
          'id': geocode
      }
  ]

  operations = [{
      'operator': 'ADD',
      'operand': {
          'campaignId': campaign['id'],
          'criterion': criterion
      }
  } for criterion in criteria]

  response = campaign_criterion_service.mutate(operations)

  if response and 'value' in response:
    # Display the added campaign targets.
    for criterion in response['value']:
      print ('Campaign criteria of type "%s" and id "%s" was added.'
             % (criterion['criterion']['type'],
                criterion['criterion']['id']))
      


if __name__ == '__main__':
    pass