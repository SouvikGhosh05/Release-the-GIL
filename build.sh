#!/bin/bash

build-and-install_required_packages() {
    cd src/Beyond-GIL/ && python3 setup.py build_ext --inplace -f
    if ! python3 -m flake8 --version > /dev/null 2>&1; then python3 -m pip install "$(sed -n '/flake8/p' ../../requirements.txt)"; fi
}

if python3 --version > /dev/null 2>&1; then
    
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
        build-and-install_required_packages
        echo "Cython Build finished."
        
    else
        echo "Cython is not installed. Installing...."
        python3 -m pip install "$(sed -n '/Cython/p' ../../requirements.txt)"
        build-and-install_required_packages
        echo "Cython Build finished."
    fi
    
else
    echo "Python3 is not installed. Installing...." 
    sudo apt-get install python3
    echo "Try running this script again."
fi
