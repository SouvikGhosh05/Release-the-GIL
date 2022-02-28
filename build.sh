#! /bin/bash

if python3 --version 2>&1 | grep -q '^Python'; then
    
    if_Cython_installed=$(
    python3 <<EOF
try:
    import cython;
    print("Installed")
except Exception:
    print("Not installed")
EOF
    )
    if [[ $if_Cython_installed == "Installed" ]]; then
        echo "Cython is installed. No need to install."
        cd src/Beyond-GIL/ && python3 setup.py build_ext --inplace -f
        echo "Cython Build finished."
    else
        echo "Cython is not installed. Installing...."
        pip3 install -U -r requirements.txt
        cd src/Beyond-GIL/ && python3 setup.py build_ext --inplace -f
        echo "Cython Build finished."
    fi
    
else
    echo "Python3 is not installed. Installing...." 
    sudo apt-get install python3
    echo "Try running this script again."
fi
