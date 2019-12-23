from os import walk
import pandas as pd
from pandas.io.json import json_normalize
import json
from . import script

a = script.main()
list1 = list()
for dirpath, dirname, filenames in walk('F:\\Django Project\\mic-graph\\Scripts\\json_data\\misp_graph'):
    a = filenames

list1 = list()
d = dict()
di = dict()
data = list()
k=1
graph_value = list()
misp_value = list()
graph_list = list()
misp_list = list()
list1 = list()
list2 = list()
for i in range(0,len(a)):
    print(a[i])
    file = open('F:\\Django Project\\mic-graph\\Scripts\\json_data\\misp_graph\\'+str(a[i]),'r')
    a1 = json.load(file)
    for j in range(0,len(a1)):
            if j == 0:
                graph_odata_context = a1[j]['@odata.context']
                graph_id = a1[j]['id']
                graph_azureTenantId=a1[j]['azureTenantId']
                graph_action=a1[j]['action']
                graph_additionalInformation=a1[j]['additionalInformation']
                graph_activityGroupNames=a1[j]['activityGroupNames']
                graph_confidence=a1[j]['confidence']
                graph_description=a1[j]['description']
                graph_diamondModel=a1[j]['diamondModel']
                graph_emailEncoding=a1[j]['emailEncoding']
                graph_emailLanguage=a1[j]['emailLanguage']
                graph_emailRecipient=a1[j]['emailRecipient']
                graph_emailSenderAddress=a1[j]['emailSenderAddress']
                graph_emailSenderName=a1[j]['emailSenderName']
                graph_emailSourceDomain=a1[j]['emailSourceDomain']
                graph_emailSourceIpAddress=a1[j]['emailSourceIpAddress']
                graph_emailSubject=a1[j]['emailSubject']
                graph_emailXMailer=a1[j]['emailXMailer']
                graph_expirationDateTime=a1[j]['expirationDateTime']
                graph_externalId=a1[j]['externalId']
                graph_fileCompileDateTime=a1[j]['fileCompileDateTime']
                graph_fileCreatedDateTime=a1[j]['fileCreatedDateTime']
                graph_fileHashType=a1[j]['fileHashType']
                graph_fileHashValue=a1[j]['fileHashValue']
                graph_fileMutexName=a1[j]['fileMutexName']
                graph_fileName=a1[j]['fileName']
                graph_filePacker=a1[j]['filePacker']
                graph_filePath=a1[j]['filePath']
                graph_fileSize=a1[j]['fileSize']
                graph_fileType=a1[j]['fileType']
                graph_domainName=a1[j]['domainName']
                graph_ingestedDateTime=a1[j]['ingestedDateTime']
                graph_isActive=a1[j]['isActive']
                graph_killChain=a1[j]['killChain']
                graph_knownFalsePositives=a1[j]['knownFalsePositives']
                graph_lastReportedDateTime=a1[j]['lastReportedDateTime']
                graph_malwareFamilyNames=a1[j]['malwareFamilyNames']
                graph_networkCidrBlock=a1[j]['networkCidrBlock']
                graph_networkDestinationAsn=a1[j]['networkDestinationAsn']
                graph_networkDestinationCidrBlock=a1[j]['networkDestinationCidrBlock']
                graph_networkDestinationIPv4=a1[j]['networkDestinationIPv4']
                graph_networkDestinationIPv6=a1[j]['networkDestinationIPv6']
                graph_networkDestinationPort=a1[j]['networkDestinationPort']
                graph_networkIPv4=a1[j]['networkIPv4']
                graph_networkIPv6=a1[j]['networkIPv6']
                graph_networkPort=a1[j]['networkPort']
                graph_networkProtocol=a1[j]['networkProtocol']
                graph_networkSourceAsn=a1[j]['networkSourceAsn']
                graph_networkSourceCidrBlock=a1[j]['networkSourceCidrBlock']
                graph_networkSourceIPv4=a1[j]['networkSourceIPv4']
                graph_networkSourceIPv6=a1[j]['networkSourceIPv6']
                graph_networkSourcePort=a1[j]['networkSourcePort']
                graph_passiveOnly=a1[j]['passiveOnly']
                graph_severity=a1[j]['severity']
                graph_tags=a1[j]['tags']
                graph_targetProduct=a1[j]['targetProduct']
                graph_threatType=a1[j]['threatType']
                graph_tlpLevel=a1[j]['tlpLevel']
                graph_url=a1[j]['url']
                graph_userAgent=a1[j]['userAgent']
                graph_vendorInformation=a1[j]['vendorInformation']
            elif j == 1:
                misp_id = a1[j]['id']
                misp_orgc_id = a1[j]['orgc_id']
                misp_org_id = a1[j]['org_id']
                misp_date = a1[j]['date']
                misp_threat_level_id = a1[j]['threat_level_id']
                misp_info = a1[j]['info']
                misp_published = a1[j]['published']
                misp_uuid = a1[j]['uuid']
                misp_attribute_count = a1[j]['attribute_count']
                misp_analysis = a1[j]['analysis']
                misp_timestamp = a1[j]['timestamp']
                misp_distribution = a1[j]['distribution']
                misp_proposal_email_lock = a1[j]['proposal_email_lock']
                misp_locked = a1[j]['locked']
                misp_publish_timestamp = a1[j]['publish_timestamp']
                misp_sharing_group_id = a1[j]['sharing_group_id']
                misp_disable_correlation = a1[j]['disable_correlation']
                misp_extends_uuid = a1[j]['extends_uuid']
                misp_Org = a1[j]['Org']
                misp_Org_id = misp_Org['id']
                misp_Org_name = misp_Org['name']
                misp_Org_uuid = misp_Org['uuid']
                misp_Org_local = misp_Org['local']
                misp_Orgc = a1[j]['Orgc']
                misp_Orgc_id = misp_Orgc['id']
                misp_Orgc_name = misp_Orgc['name']
                misp_Orgc_uuid = misp_Orgc['uuid']
                misp_Orgc_local = misp_Orgc['local']
                misp_Attribute = a1[j]['Attribute']
                '''misp_Attribute_id=misp_Attribute['id']
                misp_Attribute_type=misp_Attribute['type']
                misp_Attribute_category=misp_Attribute['category']
                misp_Attribute_to_ids=misp_Attribute['to_ids']
                misp_Attribute_uuid=misp_Attribute['uuid']
                misp_Attribute_event_id=misp_Attribute['event_id']
                misp_Attribute_distribution=misp_Attribute['distribution']
                misp_Attribute_timestamp=misp_Attribute['timestamp']
                misp_Attribute_comment=misp_Attribute['comment']
                misp_Attribute_sharing_group_id=misp_Attribute['sharing_group_id']
                misp_Attribute_deleted=misp_Attribute['deleted']
                misp_Attribute_disable_correlation=misp_Attribute['disable_correlation']
                misp_Attribute_object_id=misp_Attribute['object_id']
                misp_Attribute_object_relation=misp_Attribute['object_relation']
                misp_Attribute_value=misp_Attribute['value']
                misp_Attribute_Galaxy=misp_Attribute['Galaxy']
                misp_Attribute_ShadowAttribute=misp_Attribute['ShadowAttribute']'''
                misp_Attribute_id= []
                misp_Attribute_type=[]
                misp_Attribute_category=[]
                misp_Attribute_to_ids=[]
                misp_Attribute_uuid=[]
                misp_Attribute_event_id=[]
                misp_Attribute_distribution=[]
                misp_Attribute_timestamp=[]
                misp_Attribute_comment=[]
                misp_Attribute_sharing_group_id=[]
                misp_Attribute_deleted=[]
                misp_Attribute_disable_correlation=[]
                misp_Attribute_object_id=[]
                misp_Attribute_object_relation=[]
                misp_Attribute_value=[]
                misp_Attribute_Galaxy=[]
                misp_Attribute_ShadowAttribute=[]
                misp_Attribute_Tag = []
                misp_Attribute_Tag_id= []
                misp_Attribute_Tag_name=[]
                misp_Attribute_Tag_colour=[]
                misp_Attribute_Tag_exportable=[]
                misp_Attribute_Tag_user_id=[]
                misp_Attribute_Tag_hide_tag=[]
                misp_Attribute_Tag_numerical_value=[]
                for i in range(0,len(misp_Attribute)):
                    misp_Attribute_id.append(misp_Attribute[i]['id'])
                    misp_Attribute_type.append(misp_Attribute[i]['type'])
                    misp_Attribute_category.append(misp_Attribute[i]['category'])
                    misp_Attribute_to_ids.append(misp_Attribute[i]['to_ids'])
                    misp_Attribute_uuid.append(misp_Attribute[i]['uuid'])
                    misp_Attribute_event_id.append(misp_Attribute[i]['event_id'])
                    misp_Attribute_distribution.append(misp_Attribute[i]['distribution'])
                    misp_Attribute_timestamp.append(misp_Attribute[i]['timestamp'])
                    misp_Attribute_comment.append(misp_Attribute[i]['comment'])
                    misp_Attribute_sharing_group_id.append(misp_Attribute[i]['sharing_group_id'])
                    misp_Attribute_deleted.append(misp_Attribute[i]['deleted'])
                    misp_Attribute_disable_correlation.append(misp_Attribute[i]['disable_correlation'])
                    misp_Attribute_object_id.append(misp_Attribute[i]['object_id'])
                    misp_Attribute_object_relation.append(misp_Attribute[i]['object_relation'])
                    misp_Attribute_value.append(misp_Attribute[i]['value'])
                    misp_Attribute_Galaxy.append(misp_Attribute[i]['Galaxy'])
                    misp_Attribute_ShadowAttribute.append(misp_Attribute[i]['ShadowAttribute'])
                    #misp_Attribute_Tag = misp_Attribute[i]['Tag']
                    #print(misp_Attribute_Tag)
                    try:
                        #print(misp_Attribute[i]['Tag'])
                        for k in range(0,len(misp_Attribute[i]['Tag'])):
                            misp_Attribute_Tag = misp_Attribute[i]['Tag']
                            misp_Attribute_Tag_id.append(misp_Attribute_Tag[k]['id'])
                            misp_Attribute_Tag_name.append(misp_Attribute_Tag[k]['name'])
                            misp_Attribute_Tag_colour.append(misp_Attribute_Tag[k]['colour'])
                            misp_Attribute_Tag_exportable.append(misp_Attribute_Tag[k]['exportable'])
                            misp_Attribute_Tag_user_id.append(misp_Attribute_Tag[k]['user_id'])
                            misp_Attribute_Tag_hide_tag.append(misp_Attribute_Tag[k]['hide_tag'])
                            misp_Attribute_Tag_numerical_value.append(misp_Attribute_Tag[k]['numerical_value'])
                    except KeyError:
                        pass
                    
                  

                    
                misp_ShadowAttribute = a1[j]['ShadowAttribute']
                misp_RelatedEvent = a1[j]['RelatedEvent']
                misp_Galaxy = a1[j]['Galaxy'][0]
                misp_Galaxy_id = misp_Galaxy['id']
                misp_Galaxy_uuid = misp_Galaxy['uuid']
                misp_Galaxy_name = misp_Galaxy['name']
                misp_Galaxy_type = misp_Galaxy['type']
                misp_Galaxy_description = misp_Galaxy['description']
                misp_Galaxy_version = misp_Galaxy['version']
                misp_Galaxy_icon = misp_Galaxy['icon']
                misp_Galaxy_namespace = misp_Galaxy['namespace']
                misp_Galaxy_GalaxyCluster = misp_Galaxy['GalaxyCluster'][0]
                misp_Galaxy_GalaxyCluster_id = misp_Galaxy_GalaxyCluster['id']
                misp_Galaxy_GalaxyCluster_uuid = misp_Galaxy_GalaxyCluster['uuid']
                misp_Galaxy_GalaxyCluster_collection_uuid = misp_Galaxy_GalaxyCluster['collection_uuid']
                misp_Galaxy_GalaxyCluster_type = misp_Galaxy_GalaxyCluster['type']
                misp_Galaxy_GalaxyCluster_value = misp_Galaxy_GalaxyCluster['value']
                misp_Galaxy_GalaxyCluster_tag_name = misp_Galaxy_GalaxyCluster['tag_name']
                misp_Galaxy_GalaxyCluster_description = misp_Galaxy_GalaxyCluster['description']
                misp_Galaxy_GalaxyCluster_galaxy_id = misp_Galaxy_GalaxyCluster['galaxy_id']
                misp_Galaxy_GalaxyCluster_source = misp_Galaxy_GalaxyCluster['source']
                misp_Galaxy_GalaxyCluster_authors = misp_Galaxy_GalaxyCluster['authors']
                misp_Galaxy_GalaxyCluster_version = misp_Galaxy_GalaxyCluster['version']
                misp_Galaxy_GalaxyCluster_tag_id = misp_Galaxy_GalaxyCluster['tag_id']
                misp_Galaxy_GalaxyCluster_meta = misp_Galaxy_GalaxyCluster['meta']
                misp_Galaxy_GalaxyCluster_meta_extensions = misp_Galaxy_GalaxyCluster_meta['extensions']
                misp_Galaxy_GalaxyCluster_meta_payment_method = misp_Galaxy_GalaxyCluster_meta['payment-method']
                misp_Galaxy_GalaxyCluster_meta_price = misp_Galaxy_GalaxyCluster_meta['price']
                misp_Galaxy_GalaxyCluster_meta_ransomnotes = misp_Galaxy_GalaxyCluster_meta['ransomnotes']
                misp_Galaxy_GalaxyCluster_meta_ransomnotes_filenames= misp_Galaxy_GalaxyCluster_meta['ransomnotes-filenames']
                misp_Galaxy_GalaxyCluster_meta_refs = misp_Galaxy_GalaxyCluster_meta['refs']
                misp_Galaxy_GalaxyCluster_meta_synonyms = misp_Galaxy_GalaxyCluster_meta['synonyms']
                misp_Galaxy_GalaxyCluster_local = misp_Galaxy_GalaxyCluster['local']
                misp_Object=a1[j]['Object'][0]
                misp_Object_id=misp_Object['id']
                misp_Object_name=misp_Object['name']
                misp_Object_meta_category=misp_Object['meta-category']
                misp_Object_description=misp_Object['description']
                misp_Object_template_uuid=misp_Object['template_uuid']
                misp_Object_template_version=misp_Object['template_version']
                misp_Object_event_id=misp_Object['event_id']
                misp_Object_uuid=misp_Object['uuid']
                misp_Object_timestamp=misp_Object['timestamp']
                misp_Object_distribution=misp_Object['distribution']
                misp_Object_sharing_group_id=misp_Object['sharing_group_id']
                misp_Object_comment=misp_Object['comment']
                misp_Object_deleted=misp_Object['deleted']
                misp_Object_ObjectReference=misp_Object['ObjectReference']
                misp_Object_Attribute=misp_Object['Attribute']
                misp_Object_Attribute_id = []
                misp_Object_Attribute_type=[]
                misp_Object_Attribute_category=[]
                misp_Object_Attribute_to_ids=[]
                misp_Object_Attribute_uuid=[]
                misp_Object_Attribute_event_id=[]
                misp_Object_Attribute_distribution=[]
                misp_Object_Attribute_timestamp=[]
                misp_Object_Attribute_comment=[]
                misp_Object_Attribute_sharing_group_id=[]
                misp_Object_Attribute_deleted=[]
                misp_Object_Attribute_disable_correlation=[]
                misp_Object_Attribute_object_id=[]
                misp_Object_Attribute_object_relation=[]
                misp_Object_Attribute_value=[]
                misp_Object_Attribute_Galaxy=[]
                misp_Object_Attribute_ShadowAttribute=[]
                for i in range(0,len(misp_Object_Attribute)):
                    misp_Object_Attribute_id.append(misp_Object_Attribute[i]['id'])
                    misp_Object_Attribute_type.append(misp_Object_Attribute[i]['type'])
                    misp_Object_Attribute_category.append(misp_Object_Attribute[i]['category'])
                    misp_Object_Attribute_to_ids.append(misp_Object_Attribute[i]['to_ids'])
                    misp_Object_Attribute_uuid.append(misp_Object_Attribute[i]['uuid'])
                    misp_Object_Attribute_event_id.append(misp_Object_Attribute[i]['event_id'])
                    misp_Object_Attribute_distribution.append(misp_Object_Attribute[i]['distribution'])
                    misp_Object_Attribute_timestamp.append(misp_Object_Attribute[i]['timestamp'])
                    misp_Object_Attribute_comment.append(misp_Object_Attribute[i]['comment'])
                    misp_Object_Attribute_sharing_group_id.append(misp_Object_Attribute[i]['sharing_group_id'])
                    misp_Object_Attribute_deleted.append(misp_Object_Attribute[i]['deleted'])
                    misp_Object_Attribute_disable_correlation.append(misp_Object_Attribute[i]['disable_correlation'])
                    misp_Object_Attribute_object_id.append(misp_Object_Attribute[i]['object_id'])
                    misp_Object_Attribute_object_relation.append(misp_Object_Attribute[i]['object_relation'])
                    misp_Object_Attribute_value.append(misp_Object_Attribute[i]['value'])
                    misp_Object_Attribute_Galaxy.append(misp_Object_Attribute[i]['Galaxy'])
                    misp_Object_Attribute_ShadowAttribute.append(misp_Object_Attribute[i]['ShadowAttribute'])
                misp_Tag = a1[j]['Tag']
                misp_Tag_id = []
                misp_Tag_name = []
                misp_Tag_colour = []
                misp_Tag_exportable = []
                misp_Tag_user_id = []
                misp_Tag_hide_tag = []
                misp_Tag_numerical_value = []
                for i in range(0,len(misp_Tag)):
                    misp_Tag_id.append(misp_Tag[i]['id'])
                    misp_Tag_name.append(misp_Tag[i]['name'])
                    misp_Tag_colour.append(misp_Tag[i]['colour'])
                    misp_Tag_exportable.append(misp_Tag[i]['exportable'])
                    misp_Tag_user_id.append(misp_Tag[i]['user_id'])
                    misp_Tag_hide_tag.append(misp_Tag[i]['hide_tag'])
                    misp_Tag_numerical_value.append(misp_Tag[i]['numerical_value'])
                    #misp_Tag2.append("-------------------------------------------")
                #misp_Tag_id = misp_Tag['id']
                #print(misp_Tag_id)
                
            
        
    graph_value = [
        graph_odata_context,
        graph_id,
        graph_azureTenantId,
        graph_action,
        graph_additionalInformation,
        graph_activityGroupNames,
        graph_confidence,
        graph_description,
        graph_diamondModel,
        graph_emailEncoding,
        graph_emailLanguage,
        graph_emailRecipient,
        graph_emailSenderAddress,
        graph_emailSenderName,
        graph_emailSourceDomain,
        graph_emailSourceIpAddress,
        graph_emailSubject,
        graph_emailXMailer,
        graph_expirationDateTime,
        graph_externalId,
        graph_fileCompileDateTime,
        graph_fileCreatedDateTime,
        graph_fileHashType,
        graph_fileHashValue,
        graph_fileMutexName,
        graph_fileName,
        graph_filePacker,
        graph_filePath,
        graph_fileSize,
        graph_fileType,
        graph_domainName,
        graph_ingestedDateTime,
        graph_isActive,
        graph_killChain,
        graph_knownFalsePositives,
        graph_lastReportedDateTime,
        graph_malwareFamilyNames,
        graph_networkCidrBlock,
        graph_networkDestinationAsn,
        graph_networkDestinationCidrBlock,
        graph_networkDestinationIPv4,
        graph_networkDestinationIPv6,
        graph_networkDestinationPort,
        graph_networkIPv4,
        graph_networkIPv6,
        graph_networkPort,
        graph_networkProtocol,
        graph_networkSourceAsn,
        graph_networkSourceCidrBlock,
        graph_networkSourceIPv4,
        graph_networkSourceIPv6,
        graph_networkSourcePort,
        graph_passiveOnly,
        graph_severity,
        graph_tags,
        graph_targetProduct,
        graph_threatType,
        graph_tlpLevel,
        graph_url,
        graph_userAgent,
        graph_vendorInformation
        ]
    list1.append(graph_value)
    misp_value = [
    misp_id,
    misp_orgc_id,
    misp_org_id,
    misp_date,
    misp_threat_level_id,
    misp_info,
    misp_published,
    misp_uuid,
    misp_attribute_count,
    misp_analysis,
    misp_timestamp,
    misp_distribution,
    misp_proposal_email_lock,
    misp_locked,
    misp_publish_timestamp,
    misp_sharing_group_id,
    misp_disable_correlation,
    misp_extends_uuid,
    misp_Org_id,
    misp_Org_name,
    misp_Org_uuid,
    misp_Org_local,
    misp_Orgc_id,
    misp_Orgc_name,
    misp_Orgc_uuid,
    misp_Orgc_local,
    misp_Attribute_id,
    misp_Attribute_type,
    misp_Attribute_category,
    misp_Attribute_to_ids,
    misp_Attribute_uuid,
    misp_Attribute_event_id,
    misp_Attribute_distribution,
    misp_Attribute_timestamp,
    misp_Attribute_comment,
    misp_Attribute_sharing_group_id,
    misp_Attribute_deleted,
    misp_Attribute_disable_correlation,
    misp_Attribute_object_id,
    misp_Attribute_object_relation,
    misp_Attribute_value,
    misp_Attribute_Galaxy,
    misp_Attribute_ShadowAttribute,
    misp_Attribute_Tag_id,
    misp_Attribute_Tag_name,
    misp_Attribute_Tag_colour,
    misp_Attribute_Tag_exportable,
    misp_Attribute_Tag_user_id,
    misp_Attribute_Tag_hide_tag,
    misp_Attribute_Tag_numerical_value,
    misp_ShadowAttribute,
    misp_RelatedEvent,
    misp_Galaxy_id,
    misp_Galaxy_uuid,
    misp_Galaxy_name,
    misp_Galaxy_type,
    misp_Galaxy_description,
    misp_Galaxy_version,
    misp_Galaxy_icon,
    misp_Galaxy_namespace,
    misp_Galaxy_GalaxyCluster_id,
    misp_Galaxy_GalaxyCluster_uuid,
    misp_Galaxy_GalaxyCluster_collection_uuid,
    misp_Galaxy_GalaxyCluster_type,
    misp_Galaxy_GalaxyCluster_value,
    misp_Galaxy_GalaxyCluster_tag_name,
    misp_Galaxy_GalaxyCluster_description,
    misp_Galaxy_GalaxyCluster_galaxy_id,
    misp_Galaxy_GalaxyCluster_source,
    misp_Galaxy_GalaxyCluster_authors,
    misp_Galaxy_GalaxyCluster_version,
    misp_Galaxy_GalaxyCluster_tag_id,
    misp_Galaxy_GalaxyCluster_meta_extensions,
    misp_Galaxy_GalaxyCluster_meta_payment_method,
    misp_Galaxy_GalaxyCluster_meta_price,
    misp_Galaxy_GalaxyCluster_meta_ransomnotes,
    misp_Galaxy_GalaxyCluster_meta_ransomnotes_filenames,
    misp_Galaxy_GalaxyCluster_meta_refs,
    misp_Galaxy_GalaxyCluster_meta_synonyms,
    misp_Galaxy_GalaxyCluster_local,
    misp_Object_id,
    misp_Object_name,
    misp_Object_meta_category,
    misp_Object_description,
    misp_Object_template_uuid,
    misp_Object_template_version,
    misp_Object_event_id,
    misp_Object_uuid,
    misp_Object_timestamp,
    misp_Object_distribution,
    misp_Object_sharing_group_id,
    misp_Object_comment,
    misp_Object_deleted,
    misp_Object_ObjectReference,
    misp_Object_Attribute_id,
    misp_Object_Attribute_type,
    misp_Object_Attribute_category,
    misp_Object_Attribute_to_ids,
    misp_Object_Attribute_uuid,
    misp_Object_Attribute_event_id,
    misp_Object_Attribute_distribution,
    misp_Object_Attribute_timestamp,
    misp_Object_Attribute_comment,
    misp_Object_Attribute_sharing_group_id,
    misp_Object_Attribute_deleted,
    misp_Object_Attribute_disable_correlation,
    misp_Object_Attribute_object_id,
    misp_Object_Attribute_object_relation,
    misp_Object_Attribute_value,
    misp_Object_Attribute_Galaxy,
    misp_Object_Attribute_ShadowAttribute,
    misp_Tag_id,
    misp_Tag_name,
    misp_Tag_colour,
    misp_Tag_exportable,
    misp_Tag_user_id,
    misp_Tag_hide_tag,
    misp_Tag_numerical_value
    ]
    list1.append(misp_value)
    list2.append(list1)
    list1=[]
    #print("\n")
    #print(graph_value)
    #print(graph_value)
    #print("\n")
    #print(misp_value)
        #data.append(a1[j])

    #for k in range(0,len(data)):
        #print(data[k]['id'])
        
#print(misp_list)
#print("\n")
#print(graph_list)
#print(list2[1])
