# for element in $(printenv)
# do
#   echo $element
# done
# permission_to_append={
#    "role": "READER",
#    "userByEmail": "hi"
#   }
# x=$(cat temp.json |jq '.access += [{"role": "READER","userByEmail": "hi"}]')
# echo $x
permission_to_append="{\"role\":\"READER\"\,\"userByEmail\":\"useremail\"}\,"
str="s/access\":\[/&$permission_to_append/"
sed -i $str temp.json