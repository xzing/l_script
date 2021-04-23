#!/bin/bash
# check_results=`kubectl get pods`

data=`kubectl get deploy | awk '{print $1}' | grep -v NAME`

line="whiptail --title \"选择对应pod\" --radiolist \"空格选中，回车确认\" 40 80 30  "

# echo "$data"

OLD_IFS="$IFS"
IFS='
'
arr=($data)
IFS="$OLD_IFS"
for s in ${arr[@]}
do
line="$line \"$s\" \"\" OFF "
done

line="$line  3>&1 1>&2 2>&3"
# echo "$line"

DISTROS=`eval $line`

exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "The chosen distro is:" $DISTROS
else
    echo "You chose Cancel."
fi

kubectl logs --tail=500 -f deployment/$DISTROS --container $DISTROS
