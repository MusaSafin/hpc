#!/bin/bash
# check if subdirectory ”Linux” exists in present directory.
# If yes, print message ”course”. If no, print message ”very
# easy” and create the ”Linux” directory.

if [[ ! -e "Linux" ]]; then
   echo "very easy"
   mkdir "Linux"
else
   echo "course"
fi
