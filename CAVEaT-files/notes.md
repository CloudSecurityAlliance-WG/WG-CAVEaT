ls > file
sed "s/^/..\/..\/clean-html.py --input '/" file | sed "s/$/' --output ..\/html-files-cleaned\//" > script
remove "file" from the script
sh ./script
