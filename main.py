import json
import requests

def get_mean(list):
    mean = 0
    for item in list:
        mean += float(item)
    return mean/len(list)
diabetes_certain = ['18c15185-fb76-43a0-b19a-cbf821108289', '1cb36563-fe65-4d33-aebf-17662139400d', '262b3073-b3ed-449b-a593-798a4b1d554e', '3a8f40da-a97f-4d81-b3cb-f72b255eeb6b', '41fdbf54-244c-48d4-beb4-f673b5571dff', '5570e679-2e66-4350-9d96-a26224f99164', '565c317f-f016-487f-9e36-7e1b2f49c16c', '5ec820ef-0b7e-4b5b-bf4f-2e31b68c789e', '69c801fa-67b8-4b0e-a854-0a0dfe28e8a0', '751ad074-8099-4446-a51d-188eb844c57f', '857b26a2-0da4-4b9a-b074-7757591f0368', '8b5259e4-4175-4fc8-8801-8a7fdef43870', 'a5fe67b5-ede5-4a6a-90a2-7370b67cd882', 'afedcde4-49e3-4fed-8704-9d812a3dda62', 'c6932e1b-d0cd-4af5-b207-0c027b3c276d', 'e2ec862e-0bd4-4d4b-84dc-35e237eb4f7d', 'e8026595-992c-4932-b66a-73670a2a4855', 'eba9e563-bba1-4b58-9e4f-e688c8ff771f']

patient_ids = ['0029a7f9-fd73-4629-9a2f-3170c0338420', '011611bb-cb81-437c-ab2c-14c8ee1dd819', '02c0d81c-0438-4d24-8737-3aeba8e221c7', '07258091-7a24-4096-8a33-aeea4f9784b3', '08eb5d8e-f13a-408c-9edc-ddc8428c3793', '0923b2b9-b076-4b7c-aea2-5fe76e259035', '0a2274ed-dda2-4f37-ba8d-7b1ccb28f37c', '0b66fe33-2924-4802-8bd8-e0daf19f0f13', '0ba791f0-3a46-4ccb-8f3c-293c8f207b03', '0bd3fb14-d2f4-47ed-be02-3d41beba2ee7', '0c190312-214b-4bb5-9e8c-53bebb9af853', '0c659112-2aa9-4033-85f2-ec1792b783f5', '0f89bcab-0c58-4d4f-983e-d703fd392c3d', '106081bf-7b7d-451e-97d7-f391d75a09dd', '1543a5de-fb5b-4fe1-ade0-dbc444deb460', '16e0d083-d3ac-4d3b-8278-c2b6eabdd0ba', '188fca6d-d489-4d4c-a6d6-c3662bb852dd', '18c15185-fb76-43a0-b19a-cbf821108289', '1ab36730-46ca-4371-8b18-77eed7adfcb2', '1c6e552d-7c93-4dbb-999f-323588914ef6', '1cb36563-fe65-4d33-aebf-17662139400d', '1d3a7794-0cc9-4caa-b1b5-72420e838550', '1edce023-fe52-43a3-aa74-5a65ba2b6293', '1f771da3-ab67-4576-8484-8000d5259554', '255beacd-58aa-4874-a851-6c1d201d483c', '262b3073-b3ed-449b-a593-798a4b1d554e', '27725f6f-b76d-46bc-bdbb-30ed422d0321', '27a1f01d-528b-4548-933c-3c87b24ba224', '28a09d03-4df7-431e-809e-bf2ed72b0268', '28a94687-c571-4f3e-aae0-ddb74df03bc4', '2915822d-c347-4803-b420-31a865aaf90e', '2961d31a-80ce-4522-84e8-366ee1cc826e', '297d92d7-0eff-4677-bfd1-abc1b8ad5140', '2a4f21d6-ff00-4f6c-8fed-2fcf2cdadfb0', '3171402d-9e28-40c2-9b2d-0ab8647d3291', '327c82fd-f742-49f7-843a-90f14ee4a4d8', '3543de00-7868-4cef-9a9d-115b6be71a7b', '38f2d480-9a88-4774-a25c-89b2501aefe6', '3a8f40da-a97f-4d81-b3cb-f72b255eeb6b', '3d816c1a-fde7-43a1-8729-ba5b15e0b84a', '408547e2-15ce-4c49-8ae7-39fdf8bd8a77', '41fdbf54-244c-48d4-beb4-f673b5571dff', '46d36f32-49b2-4be2-b5fd-3ee990e4b6fb', '492d8cf0-ea09-47d4-a318-1e0cb0410fa3', '4ac4a457-1603-4049-a7f2-3be735996968', '4b757e15-d038-4e63-bc47-9da2aa3c1d8f', '5242cdf6-ae79-45c6-afe0-f93c24f6b313', '54516bab-acd6-4069-a874-cd4b8ac2d760', '5570e679-2e66-4350-9d96-a26224f99164', '565c317f-f016-487f-9e36-7e1b2f49c16c', '582edcad-2a7e-44a6-a3a8-c2283dbbc55e', '58f47f58-7698-4bb4-a041-289551d35e78', '59422f81-516a-43a9-8a1c-ef1ee10b23ed', '59708e17-1df8-43f4-bba6-7b0fbf0304ff', '5a52916d-4c45-41de-b707-0c79b4482b39', '5afd7f48-e947-4d5b-a815-d1c03ae46c7b', '5ba2d7a6-d9a3-4ea0-ab8e-2c75ce80fcf7', '5d3e5bd5-c1dc-405c-a9f0-86bd2295f74b', '5ec820ef-0b7e-4b5b-bf4f-2e31b68c789e', '660d60eb-15ff-412e-9f9c-93f613fde3b3', '663238c2-02e7-4ca8-a716-21e90cb9f30a', '674d21fd-db9b-4e57-97fd-b31524537a3b', '683b985d-53b6-4f95-8d5a-22a828fd8cbd', '691a9369-6765-4aaf-9874-ff0e68996080', '69c801fa-67b8-4b0e-a854-0a0dfe28e8a0', '6e3c88b7-b6e8-4644-bb46-2bb42c0c2202', '6f92a50b-9109-41c8-affd-32e06c5aeea1', '71851b39-14b7-4b63-9f99-bb64fa98faac', '7190bc91-a1c7-4cbc-a250-98a46d011c6d', '72657370-5370-4c3b-bb6d-ce0adbdc1a48', '74d3e560-b649-4f2e-8e87-3cd1619de390', '751ad074-8099-4446-a51d-188eb844c57f', '78265db7-a57c-44ee-8598-f8f9cc388364', '79ac35df-0bd4-46a9-bcf8-75f8f09dde08', '7caf9351-25ed-416e-bb2c-3e4dd25b0ded', '7dcfa66f-46dc-40b3-ba96-98915f03b769', '857b26a2-0da4-4b9a-b074-7757591f0368', '882123e1-079a-45c2-b6d4-640f0cc914a6', '89c52cab-88b1-446a-9852-29e6b2593645', '8b5259e4-4175-4fc8-8801-8a7fdef43870', '8bd1459b-a52d-4323-a74d-585c7f67d8a1', '8dad4c13-cdad-41ea-a281-40ee25532e29', '8e562f53-a04c-4ccd-ac90-aeedef1f6ac1', '8e67674e-6324-4675-b3ef-7804d8d6e22b', '8f7927d2-473f-4d72-a3a7-aa4e52090980', '8fa87a59-7991-4279-8472-59e94d75b38c', '90d050ca-813c-4a95-a97b-b7097aa9d4d7', '93178604-7b31-46f9-bdb4-b85742c69215', '937fdd2b-17d8-414c-ac57-21c008d25b57', '97ed9c61-65fe-4fdd-96fe-21cd904c1492', '98808dae-e37b-4917-8d7e-cb4a9094ea08', '9be1a368-3b25-4ef1-b024-3108b100fa7e', '9c5d337c-a273-4050-b1c4-74ac3a46b938', '9ed9bc12-f2b1-464c-93ae-f0f65b3c7439', 'a2613ac6-57c5-46ae-85db-a51775c6746d', 'a5fe67b5-ede5-4a6a-90a2-7370b67cd882', 'a7455719-6075-453f-bd03-78a667c9566f', 'a787d385-a93d-4173-af59-1c77f8717240', 'a92f8e98-6a6c-48a8-94c8-30ae8ff9595b', 'a93af917-94b1-4ee1-a6f8-0152c1cf54b8', 'aa0cf644-b16c-478d-8754-eb8638e4ecf1', 'aa58a33d-58c8-40f0-a4c6-50f82c49f2f1', 'ac36f7c6-28ce-45c8-a626-5f89537f7d49', 'ada64b06-cabf-4656-afdb-b97f951c4244', 'afc359fa-3c62-446a-beef-20986b5367df', 'afedcde4-49e3-4fed-8704-9d812a3dda62', 'b03585bc-0a25-459e-829a-445c563abf63', 'bb856f38-7ac6-4ca6-a824-9d77211199de', 'bb8d18c5-386b-478a-8092-b00cee1baaea', 'bc28dc47-f5db-4266-ab12-0d26ecdd4616', 'bc9ff862-2d73-4448-b345-c49154171f3b', 'bfaaa672-ae24-4778-a268-8a30b1942754', 'c3d4f7c6-5f55-46f6-a50d-3b26d4efb57e', 'c6932e1b-d0cd-4af5-b207-0c027b3c276d', 'c8c347e6-b01a-48bd-91ee-668660d3e029', 'ce5070c2-54ed-4abc-91f3-23d9e9db5e5c', 'cf20b245-4479-44e5-94d7-bf6f9f5c60f3', 'd053c996-0242-4440-999b-8de0e9b68556', 'd187a687-d97b-4322-a880-dbcd6a6c5b96', 'd6f0b72a-e600-4076-8dc5-111306efca94', 'd6fb68c5-725f-4b3b-891a-2b5e37361544', 'd948c9c2-9122-4520-80a4-b3d30906c35d', 'db01f94f-7708-4a8e-ae98-4c5e08c563ab', 'dbbd0304-ef1f-417a-8d9c-2b9079ffeef3', 'dc529a5b-40da-4f12-87b8-f35abab47c18', 'dd436a6a-5517-4ada-9ea2-8923f5cf42a5', 'dd646870-7b15-4eef-9a0f-eab615b280c6', 'ddfaea94-d559-4073-9b57-3f139a01af4d', 'e11fe5e0-5025-4d5a-a9da-29490576c958', 'e21e3713-14e6-4b77-b7b1-9914b47daec0', 'e2ec862e-0bd4-4d4b-84dc-35e237eb4f7d', 'e8026595-992c-4932-b66a-73670a2a4855', 'ea3263f3-24cb-4f62-a663-e9d68e654960', 'eba9e563-bba1-4b58-9e4f-e688c8ff771f', 'eef20546-a9a9-4eea-b6ab-17fbd8752f25', 'ef557a1a-c95c-4082-bcb5-8499451df619', 'efe33ea6-f31c-47c4-b6ad-e485266c5031', 'effe0c11-95cf-4c40-9b8e-037fb4c2489a', 'f03b4556-ec9f-4c67-ba19-77a9f0f7b8d0', 'f2ceedbb-007a-4eb9-bcc3-4cb6971a5562', 'f3c92834-7e41-4c49-923a-2459c442545d', 'f640cd74-8bba-458c-95dc-71d67fc77e45', 'f6df5be9-f85f-4c93-a500-34585f412656', 'f77669d3-724e-4bfd-bcb4-dbad700515b4', 'f7a66aa0-6a5e-4977-8fc0-91eadef8435f', 'fba96114-7d33-4f69-b866-f07a95f7748d', 'fbc7b10b-14e3-40e0-8ec4-5a9366872feb']

infection_list = ["15cb54b1-7983-40c7-91af-43701984d90b","3ed878a0-60aa-48c4-bb52-d64c72c6ef75", "8e4955b4-7313-451f-abc1-af165af6f080", "dd62061c-4475-4398-8569-fa0e12f62b33", "e5850a8f-5a21-49c5-80be-5270e3b126bb","eef20546-a9a9-4eea-b6ab-17fbd8752f25"]
dyslipidemia_list = ['1543a5de-fb5b-4fe1-ade0-dbc444deb460', '01cb3f14-e2b7-4655-94cb-3cce7a9d6c1c', '1543a5de-fb5b-4fe1-ade0-dbc444deb460', '2230463c-a0ff-49ba-b2bf-289f619703e0', '3a350f35-30d8-42f2-a5d0-1c62ef80ca79', '3c811f1d-2fe9-4f21-85d8-da62868a3863', '514257c1-c3cf-4ec4-86f4-d28081a44bb4', 'aeac2b55-3ae3-418e-886c-5374e232bd53']
def get_patient_ids():
    global patient_ids
    patient_ids = []
    page = 1
    while page < 24:
        response_raw = requests.get("https://sandbox86.tactiorpm7000.com/tactio-clinician-api/1.1.4/bearer 4220b158662c1423012c8106ca59d14f678ddc82/Patient", params = {"page": str(page) },headers = {"Authorization" :"bearer 4220b158662c1423012c8106ca59d14f678ddc82"})
        print("Status code: ", response_raw.status_code, "Page: ", page)
        response = json.loads(response_raw.content)
        print(response)
        patients = response["entry"]
        for patient in patients :
            #print(patient["resource"]["id"])
            patient_ids.append(patient["resource"]["id"])
        page += 1

def get_observations(subject, code):
    response_raw = requests.get("https://sandbox86.tactiorpm7000.com/tactio-clinician-api/1.1.4/bearer 4220b158662c1423012c8106ca59d14f678ddc82/Observation",params = {"subject": subject, "code": [code, code]}, headers = {"Authorization" :"bearer 4220b158662c1423012c8106ca59d14f678ddc82"})
    print("Status code: ", response_raw.status_code)
    response = json.loads(response_raw.content)
    #pages = response["link"][2]["url"][-1]
    #for page in pages:
    #response_raw = requests.get("https://sandbox86.tactiorpm7000.com/tactio-clinician-api/1.1.4/bearer 4220b158662c1423012c8106ca59d14f678ddc82/Observation",params = {"subject": subject, "page" : page}, headers = {"Authorization" :"bearer 4220b158662c1423012c8106ca59d14f678ddc82"})
    #response = json.loads(response_raw.content)
    observations = response["entry"]
    lst = []
    for observation in observations:
        observation_type = observation["resource"]["code"]["text"]
        if observation_type == "pressure":
            systolic = str(observation["resource"]["component"][0]["valueQuantity"]["value"])
            diastolic = str(observation["resource"]["component"][1]["valueQuantity"]["value"])
            observation_value = systolic + "/" + diastolic
        else:
            observation_value = observation["resource"]["valueQuantity"]["value"]
            observation_unit = observation["resource"]["valueQuantity"]["unit"]
        lst.append(observation_value)
        observation_date = observation["resource"]["effectiveDateTime"]
    lst.sort(reverse= True)
    print(subject, "\n",lst[0], ": ", lst[1], " ", observation_unit, "\nPerformed on: ", observation_date )
    return response
high_bmi_list = ['0029a7f9-fd73-4629-9a2f-3170c0338420', '011611bb-cb81-437c-ab2c-14c8ee1dd819', '0923b2b9-b076-4b7c-aea2-5fe76e259035', u'0a2274ed-dda2-4f37-ba8d-7b1ccb28f37c', u'0b66fe33-2924-4802-8bd8-e0daf19f0f13', u'0c190312-214b-4bb5-9e8c-53bebb9af853', u'0c659112-2aa9-4033-85f2-ec1792b783f5', u'0f89bcab-0c58-4d4f-983e-d703fd392c3d', u'18c15185-fb76-43a0-b19a-cbf821108289', u'1ab36730-46ca-4371-8b18-77eed7adfcb2', u'1c6e552d-7c93-4dbb-999f-323588914ef6', u'1cb36563-fe65-4d33-aebf-17662139400d', u'262b3073-b3ed-449b-a593-798a4b1d554e', u'27a1f01d-528b-4548-933c-3c87b24ba224', u'2961d31a-80ce-4522-84e8-366ee1cc826e', u'297d92d7-0eff-4677-bfd1-abc1b8ad5140', u'2a4f21d6-ff00-4f6c-8fed-2fcf2cdadfb0', u'3171402d-9e28-40c2-9b2d-0ab8647d3291', u'327c82fd-f742-49f7-843a-90f14ee4a4d8', u'3543de00-7868-4cef-9a9d-115b6be71a7b', u'38f2d480-9a88-4774-a25c-89b2501aefe6', u'3a8f40da-a97f-4d81-b3cb-f72b255eeb6b', u'3d816c1a-fde7-43a1-8729-ba5b15e0b84a', u'41fdbf54-244c-48d4-beb4-f673b5571dff', u'4b757e15-d038-4e63-bc47-9da2aa3c1d8f', u'5570e679-2e66-4350-9d96-a26224f99164', u'565c317f-f016-487f-9e36-7e1b2f49c16c', u'582edcad-2a7e-44a6-a3a8-c2283dbbc55e', u'59422f81-516a-43a9-8a1c-ef1ee10b23ed', u'5afd7f48-e947-4d5b-a815-d1c03ae46c7b', u'5d3e5bd5-c1dc-405c-a9f0-86bd2295f74b', u'5ec820ef-0b7e-4b5b-bf4f-2e31b68c789e', u'660d60eb-15ff-412e-9f9c-93f613fde3b3', u'663238c2-02e7-4ca8-a716-21e90cb9f30a', u'674d21fd-db9b-4e57-97fd-b31524537a3b', u'683b985d-53b6-4f95-8d5a-22a828fd8cbd', u'691a9369-6765-4aaf-9874-ff0e68996080', u'69c801fa-67b8-4b0e-a854-0a0dfe28e8a0', u'6e3c88b7-b6e8-4644-bb46-2bb42c0c2202', u'7190bc91-a1c7-4cbc-a250-98a46d011c6d', u'74d3e560-b649-4f2e-8e87-3cd1619de390', u'751ad074-8099-4446-a51d-188eb844c57f', u'79ac35df-0bd4-46a9-bcf8-75f8f09dde08', u'7caf9351-25ed-416e-bb2c-3e4dd25b0ded', u'857b26a2-0da4-4b9a-b074-7757591f0368', u'882123e1-079a-45c2-b6d4-640f0cc914a6', u'8b5259e4-4175-4fc8-8801-8a7fdef43870', u'8bd1459b-a52d-4323-a74d-585c7f67d8a1', u'8e562f53-a04c-4ccd-ac90-aeedef1f6ac1', u'8e67674e-6324-4675-b3ef-7804d8d6e22b', u'8f7927d2-473f-4d72-a3a7-aa4e52090980', u'90d050ca-813c-4a95-a97b-b7097aa9d4d7', u'98808dae-e37b-4917-8d7e-cb4a9094ea08', u'9c5d337c-a273-4050-b1c4-74ac3a46b938', u'9ed9bc12-f2b1-464c-93ae-f0f65b3c7439', u'a2613ac6-57c5-46ae-85db-a51775c6746d', u'a5fe67b5-ede5-4a6a-90a2-7370b67cd882', u'a787d385-a93d-4173-af59-1c77f8717240', u'a92f8e98-6a6c-48a8-94c8-30ae8ff9595b', u'a93af917-94b1-4ee1-a6f8-0152c1cf54b8', u'ac36f7c6-28ce-45c8-a626-5f89537f7d49', u'ada64b06-cabf-4656-afdb-b97f951c4244', u'afedcde4-49e3-4fed-8704-9d812a3dda62', u'bb856f38-7ac6-4ca6-a824-9d77211199de', u'c6932e1b-d0cd-4af5-b207-0c027b3c276d', u'c8c347e6-b01a-48bd-91ee-668660d3e029', u'ce5070c2-54ed-4abc-91f3-23d9e9db5e5c', u'db01f94f-7708-4a8e-ae98-4c5e08c563ab', u'dbbd0304-ef1f-417a-8d9c-2b9079ffeef3', u'dc529a5b-40da-4f12-87b8-f35abab47c18', u'dd436a6a-5517-4ada-9ea2-8923f5cf42a5', u'dd646870-7b15-4eef-9a0f-eab615b280c6', u'ddfaea94-d559-4073-9b57-3f139a01af4d', u'e21e3713-14e6-4b77-b7b1-9914b47daec0', u'e2ec862e-0bd4-4d4b-84dc-35e237eb4f7d', u'e8026595-992c-4932-b66a-73670a2a4855', u'ea3263f3-24cb-4f62-a663-e9d68e654960', u'eba9e563-bba1-4b58-9e4f-e688c8ff771f', u'ef557a1a-c95c-4082-bcb5-8499451df619', u'f03b4556-ec9f-4c67-ba19-77a9f0f7b8d0', u'f2ceedbb-007a-4eb9-bcc3-4cb6971a5562', u'f6df5be9-f85f-4c93-a500-34585f412656', u'f7a66aa0-6a5e-4977-8fc0-91eadef8435f', u'fba96114-7d33-4f69-b866-f07a95f7748d']
diabetes_list =['0029a7f9-fd73-4629-9a2f-3170c0338420', '0b66fe33-2924-4802-8bd8-e0daf19f0f13', '0c190312-214b-4bb5-9e8c-53bebb9af853', '0c659112-2aa9-4033-85f2-ec1792b783f5', '0f89bcab-0c58-4d4f-983e-d703fd392c3d', '18c15185-fb76-43a0-b19a-cbf821108289', '1ab36730-46ca-4371-8b18-77eed7adfcb2', '1cb36563-fe65-4d33-aebf-17662139400d', '262b3073-b3ed-449b-a593-798a4b1d554e', '27a1f01d-528b-4548-933c-3c87b24ba224', '2961d31a-80ce-4522-84e8-366ee1cc826e', '297d92d7-0eff-4677-bfd1-abc1b8ad5140', '2a4f21d6-ff00-4f6c-8fed-2fcf2cdadfb0', '327c82fd-f742-49f7-843a-90f14ee4a4d8', '3a8f40da-a97f-4d81-b3cb-f72b255eeb6b', '3d816c1a-fde7-43a1-8729-ba5b15e0b84a', '41fdbf54-244c-48d4-beb4-f673b5571dff', '4b757e15-d038-4e63-bc47-9da2aa3c1d8f', '5570e679-2e66-4350-9d96-a26224f99164', '565c317f-f016-487f-9e36-7e1b2f49c16c', '59422f81-516a-43a9-8a1c-ef1ee10b23ed', '5afd7f48-e947-4d5b-a815-d1c03ae46c7b', '5d3e5bd5-c1dc-405c-a9f0-86bd2295f74b', '5ec820ef-0b7e-4b5b-bf4f-2e31b68c789e', '663238c2-02e7-4ca8-a716-21e90cb9f30a', '674d21fd-db9b-4e57-97fd-b31524537a3b', '683b985d-53b6-4f95-8d5a-22a828fd8cbd', '691a9369-6765-4aaf-9874-ff0e68996080', '69c801fa-67b8-4b0e-a854-0a0dfe28e8a0', '74d3e560-b649-4f2e-8e87-3cd1619de390', '751ad074-8099-4446-a51d-188eb844c57f', '79ac35df-0bd4-46a9-bcf8-75f8f09dde08', '7caf9351-25ed-416e-bb2c-3e4dd25b0ded', '857b26a2-0da4-4b9a-b074-7757591f0368', '882123e1-079a-45c2-b6d4-640f0cc914a6', '8b5259e4-4175-4fc8-8801-8a7fdef43870', '8bd1459b-a52d-4323-a74d-585c7f67d8a1', '8e562f53-a04c-4ccd-ac90-aeedef1f6ac1', '8e67674e-6324-4675-b3ef-7804d8d6e22b', '8f7927d2-473f-4d72-a3a7-aa4e52090980', '90d050ca-813c-4a95-a97b-b7097aa9d4d7', '98808dae-e37b-4917-8d7e-cb4a9094ea08', '9ed9bc12-f2b1-464c-93ae-f0f65b3c7439', 'a5fe67b5-ede5-4a6a-90a2-7370b67cd882', 'a787d385-a93d-4173-af59-1c77f8717240', 'a93af917-94b1-4ee1-a6f8-0152c1cf54b8', 'ac36f7c6-28ce-45c8-a626-5f89537f7d49', 'ada64b06-cabf-4656-afdb-b97f951c4244', 'afedcde4-49e3-4fed-8704-9d812a3dda62', 'bb856f38-7ac6-4ca6-a824-9d77211199de', 'c6932e1b-d0cd-4af5-b207-0c027b3c276d', 'c8c347e6-b01a-48bd-91ee-668660d3e029', 'db01f94f-7708-4a8e-ae98-4c5e08c563ab', 'dbbd0304-ef1f-417a-8d9c-2b9079ffeef3', 'dd436a6a-5517-4ada-9ea2-8923f5cf42a5', 'dd646870-7b15-4eef-9a0f-eab615b280c6', 'ddfaea94-d559-4073-9b57-3f139a01af4d', 'e21e3713-14e6-4b77-b7b1-9914b47daec0', 'e2ec862e-0bd4-4d4b-84dc-35e237eb4f7d', 'e8026595-992c-4932-b66a-73670a2a4855', 'eba9e563-bba1-4b58-9e4f-e688c8ff771f', 'ef557a1a-c95c-4082-bcb5-8499451df619', 'f2ceedbb-007a-4eb9-bcc3-4cb6971a5562', 'f6df5be9-f85f-4c93-a500-34585f412656', 'f7a66aa0-6a5e-4977-8fc0-91eadef8435f', 'fba96114-7d33-4f69-b866-f07a95f7748d']
positive_list = []
negative_list = []
def screening(id_array, code, std_mean, stdev):
    global positive_list, negative_list
    pos_list = []
    neg_list = []
    count = 1
    for id in id_array:
        print( count, "/", len(id_array))
        count +=1
        mean_lst = []
        response_raw = requests.get("https://sandbox86.tactiorpm7000.com/tactio-clinician-api/1.1.4/bearer 4220b158662c1423012c8106ca59d14f678ddc82/Observation",params = {"subject": id, "code": [code, code]}, headers = {"Authorization" :"bearer 4220b158662c1423012c8106ca59d14f678ddc82"})
        print("Status code: ", response_raw.status_code)
        response = json.loads(response_raw.content)
        #print(response)
    #    print(response)
    #    pages = response["link"][2]["url"][-1]
    #    for page in pages:
    #        response_raw = requests.get("https://sandbox86.tactiorpm7000.com/tactio-clinician-api/1.1.4/bearer 4220b158662c1423012c8106ca59d14f678ddc82/Observation",params = {"subject": subject, "page" : page}, headers = {"Authorization" :"bearer 4220b158662c1423012c8106ca59d14f678ddc82"})
    #        response = json.loads(response_raw.content)dd
        if "entry" in response:
            observations = response["entry"]
            for observation in observations:
                observation_type = observation["resource"]["code"]["text"]
                observation_value = observation["resource"]["valueQuantity"]["value"]
                print(observation_value)
                mean_lst.append(observation_value)
            mean = get_mean(mean_lst)
            print(observation_type, mean)
            if mean > std_mean- stdev:
                pos_list.append(id)
                print(True)

            neg_list.append(id)
    print (pos_list)

    positive_list = list(pos_list)
    negative_list = list(neg_list)

#print(positive_list, len(positive_list))
get_patient_ids()
#screening(patient_ids, "60621009", 30,  1)
#print(positive_list, len(positive_list))
screening(diabetes_list, "434912009", 6.3, 0.3)
screening(diabetes_list, "302788006", 7.6, 0.4)
screening(diabetes_list, "302788006", 7.6, 0.4)
screening(diabetes_list, "733829007", 6.4, 0.4)

#screening(high_bmi_list, "8480-6", 175, 10)
#screening(high_bmi_list, "", 115, 10)


#screening(positive_list , "22748-8" , 3.1, 0.3)
#screening(positive_list, "70218-3", 1.13, 0.1)
#screening(positive_list, "102737005", 1.6, 0.15)
print(positive_list, len(positive_list))
#for id in positive_list:
#    get_observations(id, ["26464-8", "386725007"])
