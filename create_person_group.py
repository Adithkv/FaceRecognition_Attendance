import cognitive_face as CF
import global_variables as global_var
from global_variables import personGroupId
import sys

Key = global_var.key

CF.Key.set(Key)

BASE_URL = global_var.BASE_URL  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
personGroups = CF.person_group.lists()
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print (personGroupId + " already exists.")
        sys.exit()

res = CF.person_group.create(personGroupId)
print (res)
