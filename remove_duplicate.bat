set PIP=c:\python25\pyInstaller-1.3\
python %PIP%Makespec.py --onefile --console --upx --tk remove_duplicate.py
python %PIP%Build.py remove_duplicate.spec