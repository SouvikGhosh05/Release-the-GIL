#! /bin/bash

echo "You are about to clean the cython build files."
echo "Pytest will fail unless you make the build again."
echo "Are you sure you want to clean the build? Type 'Yes' to continue:" | tr "\n" " "  # Remove newline with space
read -r REPLY

if [[ $REPLY = @(Yes|yes|y) ]]; then

    cd src/Beyond-GIL/  && rm -rf add_n_sub.cpython-39-x86_64-linux-gnu.so  &&
    cd src_Cython/      && rm -rf add_sub.c add_sub.html
    echo "Cython build files cleaned."
else
    echo "No files cleaned."
fi
