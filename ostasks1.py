#!/usr/bin/python
import os

userlist = ["alpha", "beta", "gamma"]

print "Adding users to system"
print "############################################################################################"
# Loop to add user from userlist
for user in userlist:
  exitcode = os.system(("id %s") % user )
  if exitcode != 0:
    print "User %s does not exist. Adding it." % user
    print "##############################################"
    print
    os.system(("useradd %s") % user )
  else:
    print "User already exist, skipping it."
    print "##############################################"
    print

# Condition to check if group exists or not, add if not exist.
exitcode = os.system("grep science /etc/group")
if exitcode != 0:
  print "Group science does not exist. Adding it."
  print "##############################################"
  print
  os.system("groupadd science")
else:
  print "Group already exist, skipping it."
  print "##############################################"
  print

# Adding all the user to science group
for user in userlist:
  print "Adding user %s in the science group" % user
  print "##############################################"
  print
  os.system(("usermod -G science %s") % user)

print "Adding directory"
print "##############################################"
print

if os.path.isdir("/opt/science_dir"):
  print "Directory already exist, skipping it"
else:
  os.mkdir("/opt/science_dir")


print "Assigning permission and ownership to the directory."
print "##############################################"
print
os.system("chown :science /opt/science_dir")

os.system("chmod 770 /opt/science_dir")
