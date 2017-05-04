from couchdb import Server
import json

# for local test
server = Server()
# for run on vm
# server = Server('http://admin:password@127.0.0.1:5984/')

def readFile():

    # add life satisfaction into database
    if 'dataset_life_satisfaction' in server:
        print('----database lift satisfaction existed----------------')
    else:
        db_life_satisfaction = server.create('dataset_life_satisfaction')

        with open('./dataset/SA2_Life_Satisfaction_from_0_to_100__Synthetic_Data__2011.json') as ls:
            ls_data = json.loads(ls.read())

        for ls_feature in ls_data['features']:
            fid = ls_feature['id']
            ls_properties = ls_feature['properties']
            ls_doc = {'_id': fid, 'properties': ls_properties}
            db_life_satisfaction.save(ls_doc)
        print('----------finish life satisfaction------------------')

    # add IEO into database
    if 'dataset_ieo' in server:
        print('----database ieo existed----------------')
    else:
        db_ieo = server.create('dataset_ieo')
        with open('./dataset/SA2_SEIFA_2011_-_The_Index_of_Education_and_Occupation__IEO.json') as ieo:
            ieo_data = json.loads(ieo.read())

        for ieo_feature in ieo_data['features']:
            ieo_id = ieo_feature['id']
            ieo_properties = ieo_feature['properties']
            ieo_doc = {'_id': ieo_id, 'properties': ieo_properties}
            db_ieo.save(ieo_doc)
        print('----------finish IEO------------------')

    # add self-assessed health into database
    if 'dataset_self_assessed_health' in server:
        print('----database self_assessed_health existed----------------')
    else:
        db_self_assessed_health = server.create('dataset_self_assessed_health')
        with open('./dataset/SA2_Self_Assessed_Health_-_Modelled_Estimate.json') as sah:
            sah_data = json.loads(sah.read())

        for sah_feature in sah_data['features']:
            sah_id = sah_feature['id']
            sah_properties = sah_feature['properties']
            sah_doc = {'_id': sah_id, 'properties': sah_properties}
            db_self_assessed_health.save(sah_doc)
        print('----------finish db_self_assessed_health------------------')

# add Community Strength into database
    if 'dataset_community_strength' in server:
        print('----database community_strength existed----------------')
    else:
        db_community_strength = server.create('dataset_community_strength')
        with open('./dataset/SA2_Community_Strength.json') as cs:
            cs_data = json.loads(cs.read())

        for cs_feature in cs_data['features']:
            cs_id = cs_feature['id']
            cs_properties = cs_feature['properties']
            cs_doc = {'_id': cs_id, 'properties': cs_properties}
            db_community_strength.save(cs_doc)
        print('----------finish db_community_strength------------------')


# add Community Strength into database
    if 'dataset_ier' in server:
        print('----database ier existed----------------')
    else:
        db_ier = server.create('dataset_ier')
        with open('./dataset/SA2_SEIFA_2011_-_The_Index_of_Economic_Resources__IER.json') as ier:
            ier_data = json.loads(ier.read())

        for ier_feature in ier_data['features']:
            ier_id = ier_feature['id']
            ier_properties = ier_feature['properties']
            ier_doc = {'_id': ier_id, 'properties': ier_properties}
            db_ier.save(ier_doc)
        print('----------finish ier------------------')


readFile()
