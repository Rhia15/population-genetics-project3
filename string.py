#this turns a text file with candidate genes into the Athaliana orthologs for the string input 

#file containing all the genes from the orientated file 
#path is always '/Users/rhianah/Downloads/Project_3/gatk/GS_1/LABNEN/genes/thalianatext.txt'

gene_list_file = '/Users/rhianah/Downloads/Project_3/gatk/GS_1/LABNEN/genes/thalianatext.txt'

# Define an empty dictionary to store the orthos for each gene
#put it in  dictionary with cochlearia gene to A thaliana gene 
genes_dict = {}

# Loop through each line in the file
with open(gene_list_file, 'r') as f:
    for line in f:
        # Split the line into its columns
        cols = line.strip().split(',')
        gene = cols[0].replace('.t1', '').replace('.t2', '').replace('.t3', '').replace('.t4', '')
        ortho = cols[1]
        
        # If the gene is not in the dictionary, create a new list for it
        if gene not in genes_dict:
            genes_dict[gene] = []
        
        # Add the ortho to the gene's list
        genes_dict[gene].append(ortho)

# Print the dictionary
print(genes_dict)

#Customise this bit, contains the gene lists you want to query, the ones you want the thaliana IDs from 

gene_list = '/Users/rhianah/Downloads/Project_3/gatk/GS_1/LABODN/genes/LABODN_fst_sweeps.txt'

#the path to the output file you want it in 

output_file = '/Users/rhianah/Downloads/Project_3/gatk/GS_1/LABODN/genes/LABODNstring_fst_sweep_thaliana.txt'


count = 0 
with open(gene_list, 'r') as f, open(output_file, 'w') as out_f:
    for gene_name in f: 
        gene_name = gene_name.strip()
        
        # Check if the gene name is in the dictionary
        if gene_name in genes_dict:
            # Access the orthologs for the gene name and print them
            orthologs = genes_dict[gene_name]
            out_f.write(','.join(orthologs) + '\n')
            print(f"Orthologs for {gene_name}: {orthologs}")
            count += 1
        else:
            print(f"No orthologs found for {gene_name}")

print(f"number of hits: {count}")




