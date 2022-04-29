#!/usr/bin/env bash

# Call from top project directory, docs directory, or readme_chunks directory
# Generates the following files from the readme_chunks:
# 	- ./docs/index.md (skips get involved chunk, already documented by read the docs)
# 	- ./README.md

current_path=`pwd`

# if readme_chunks at end of path
if [[ $current_path =~ readme_chunks$ ]]; then
    proj_dir="../../" #set base relative to readme_chunks
elif [[ $current_path =~ docs$ ]]; then
    proj_dir="../" #set base relative to docs
elif [[ $current_path =~ accessibility$ ]]; then
    proj_dir="./" #set base relative to the top of the directory
else
	proj_dir="bad"
fi

if [[ "$proj_dir" != "bad" ]]; then
	# input chunks
	intro_in="${proj_dir}/docs/readme_chunks/introduction.md"
	get_involved_in="${proj_dir}/docs/readme_chunks/getinvolved.md"
	accessibility_standards_in="${proj_dir}/docs/readme_chunks/accessibility_standards.md"
	
	# output files
	index_file_out="${proj_dir}/docs/index.md"
	readme_out="${proj_dir}/README.md"
	
	# update read the dox (skip get involved section)
	# there are dedicated sections for getting involved
	cat $intro_in > $index_file_out
	cat $accessibility_standards_in >> $index_file_out

	# # update the main README.md file
	cat $intro_in > $readme_out
	cat $get_involved_in >> $readme_out
	cat $accessibility_standards_in >> $readme_out
else
	echo "Error: please call from top directory, docs directory, or readme_chunks directory."
fi

