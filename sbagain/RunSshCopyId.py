#!/usr/bin/env python
import sys
from packages.sshcopyid import SshCopy

print("usage: python RunSshCopyId.py user host passwd port")
cSSH = SshCopy(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
cSSH.send()
print(sys.argv)
