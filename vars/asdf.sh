#!/bin/bash
while read line; do    
    svr_grp=$(grep -B9 $line group_dat|grep "Service group name")
    echo "$line is in group $svr_grp"
done < list_of_srvs.txt
