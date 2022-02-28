#!/bin/sh
######################################################################
# File_name :   migration_script.sh
# Purpose   :   Migrates svn repo to git repo.
# Date      :   March 2021
# Usage     :   ./migration_script.sh
#
# Version.  Date.       Comments.              		Who
# -------   --------    -------------------    		--------------
# 1.0       15/03/21    First release          		PP
# 1.1       22/03/21    Second release                  PP
# 1.2       07/07/21    Third release                   PP
#####################################################################
# Pre-reqs
# Server should be up and running
######################################################################

SCRIPT_PATH=/opt/software
LOG_FILE=$SCRIPT_PATH/svn_git_workdir/logs/script_error.log 

# Path to svn_git_workdir
cd $SCRIPT_PATH/svn_git_workdir

# Uncomment all svn steps for using cksum reports
# Running git svn clone migration command and going in the project's dir
while IFS= read -r url
do
#  cd $SCRIPT_PATH/SVN_Checkout
#  svn co $url
  cd $SCRIPT_PATH/svn_git_workdir
  file1=$(echo ${url#*/svn/})
  IFS='/' read -ra addr <<< "$file1"
  for ((i=0; i<${#addr[@]}; i++))
  do
     if [ $((${#addr[@]}-$i)) = 1 ]
     then
     git svn clone $url --no-metadata --prefix "" -s ${addr[$i]}
     cd ${addr[$i]}
     pwd
     appname=$(echo ${addr[$i]})
     echo "this is git application  $appname"
     for t in $(git for-each-ref --format='%(refname:short)' refs/remotes/tags); do git tag ${t/tags\//} $t && git branch -D -r $t; done
   
     find -type f -exec cksum "{}" + > $SCRIPT_PATH/git_cksum_report/$appname-git-1.txt
     cd $SCRIPT_PATH/git_cksum_report
     grep -v "./.git" $appname-git-1.txt > $appname-git-2.txt
     sort -u -k3 $appname-git-2.txt > $appname-git.txt
     rm -rf $appname-git-1.txt $appname-git-2.txt
 #    cd $SCRIPT_PATH/SVN_Checkout
 #    cd ${addr[$i]}
 #    cd trunk
     pwd
 #    application=$(echo ${addr[$i]})
 #    find -type f -exec cksum "{}" + > $SCRIPT_PATH/git_cksum_report/$application-svn-1.txt
 #    cd $SCRIPT_PATH/git_cksum_report
 #    sort -u -k3 $application-svn-1.txt  > $application-svn.txt
 #    rm -rf $application-svn-1.txt    
     cd $SCRIPT_PATH/svn_git_workdir
     fi
  done

done < /opt/software/AppNames.txt

# Comparing cksums of both files to check if difference is there or not
#diff cksumtrunk.txt cksumsvn_trunk.txt


# Files that will be attached in the email
#file1=$SCRIPT_PATH/cksumtrunk.txt
#file2=$SCRIPT_PATH/cksumsvn_trunk.txt


#mail -s $subject -a $file1 piyush.parasar@gmail.com < $SCRIPT_PATH/Email.txt   

