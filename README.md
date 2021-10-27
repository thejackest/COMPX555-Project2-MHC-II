# COMPX555-Project2-MHC-II

All of the functions used in the report are in the python, to run the specific function, just need to simplify uncomment some codes.

Provided data file has been exported into data.txt

Awk to separate data into two different files:
NotBinding:
awk '{if($1 == "0") print $2}' data.txt | tr -d ' ' > notBinding.txt
Binding:
awk '{if($1 == "1") print $2}' data.txt | tr -d ' ' > binding.txt
