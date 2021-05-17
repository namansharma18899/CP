import os
import subprocess
import sys

# project_id="singular-acumen-237807"
# dataset_id="enter_dataset_id_here"
# sa_id="testingsa01"
# sa_name="saName"
# sa_desc="saDesc"
# bash="bash"
# role="roles/bigquery.jobUser"
# permissionOutputFile="demo.json"
# #########################################
# select_project = "gcloud config set project {}".format(project_id).split(' ')
# project_list_cmd = "gcloud projects list --format=value(projectId)".split(' ')
# sa_create_cmd= "gcloud iam service-accounts create {} --description={} --display-name={})".format(
# sa_id,sa_desc,sa_name).split(' ')
# sa_permission_cmd="gcloud projects add-iam-policy-binding {} \
#  --member=serviceAccount:{}@{}.iam.gserviceaccount.com --role={}".format(
#      project_id,sa_id, project_id,role     
#      ).split(' ')
# print(sa_permission_cmd)
# # sa_create = project_list_command.split(' ')
# # shell_command = ["python","--version"]
# x = subprocess.call(sa_permission_cmd)
# print(x)