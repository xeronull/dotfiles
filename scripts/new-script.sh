#!/bin/bash
#
# new-script.sh
#
# This utility creates the requested .sh file and initializes a header (this) in it.
#
# Copyright 2017 (c) Samantaz
#


# Define copyright holder (Capitalize result of 'whoami')
#
username=$(whoami)
username="${username^}"


# Parse cli options
for arg in "$@"; do
    case $arg in
        *) script_name="${arg%sh}";;
    esac
done

# Check that a script name have been provided
if [ -z $script_name ]; then
    echo "Please specify a script name";
    exit;
fi

# Save current directory, then move to the right folder
tmp_dir=$(pwd);
cd ~/Scripts;

# Check if the file already exists !
if [ -e "$script_name".sh ]; then
    echo "Error: file $script_name.sh exists";
    exit;
fi


# =======================
# Create file and content
# =======================

# Create file and apply execute (+x) flag
touch "$script_name".sh;
chmod +x "$script_name".sh;

cat << EOF > "$script_name".sh;
#!/bin/bash
#
# $script_name.sh
#
# Insert description here
#
# Copyright $(date +%Y) (c) $username
#

EOF

# Include root checking and command line parsing scripts
cat << "EOF" >> "$script_name".sh;

# Check if user is root. If not, exit script
#
#[[ $EUID -eq 0 ]] || { echo "This script needs root privileges"; exit; }


# Parse cli options
for arg in "$@"; do
    case $arg in
        *) echo "$arg";;
    esac
done

# Ask user for something
read -n1 -p "Sure ? [y/n] " answer && echo;
[[ $answer == [Yy]* ]] || echo "okay";

EOF


# Open for editing
nano "$script_name".sh;


# Go back to where the user was
cd $tmp_dir;
