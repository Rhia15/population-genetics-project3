#This file removes the ".t" from the gene so it can be inputted into the AFDall.py script before getting AFD plots  

###removed the .t1 ect from the genes and then creates a file to input into AFDall.py

with open("/Users/rhianah/Downloads/Project_3/gatk/GS_1/LABODN/genes/LABODN_100SNPs_5000ppm_Dxy_0ol.txt", "r") as input_file: 
    lines = input_file.readlines()

filtered_lines = [line for line in lines if "." not in line]

with open("/Users/rhianah/Downloads/Project_3/gatk/GS_1/LABODN/genes/LABODN_Dxy_filter.txt", "w") as output_file: 
    output_file.writelines(filtered_lines)
