#Batch script for faststructure 

------> fast.sh <------
#!/bin/bash
#SBATCH --job-name=structure
#SBATCH --partition=hpc
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --ntasks-per-node=1
#SBATCH --mem=30g
#SBATCH --time=24:00:00
#SBATCH --output=/shared/home/mbxrs14/project_3/err_out/%x%r.out
#SBATCH --error=/shared/home/mbxrs14/project_3/err_out/%x%r.err

# These steps are required to activate conda
source $HOME/.bash_profile

conda activate /shared/home/mbxrs14/miniconda3/envs/faststructure

for i in {1..30}
do

     structure.py -K $i --input=/shared/home/mbxrs14/project_3/fast_s/rehead/rehead --format=bed --output=/shared/home/mbxrs14/project_3/fast_s/rehead/rehead_output"$i"

     chooseK.py --input=/shared/home/mbxrs14/project_3/fast_s/rehead/rehead_output"$i" > /shared/home/mbxrs14/project_3/fast_s/rehead/chooseK"$i".txt

     distruct.py -K $i --input=/shared/home/mbxrs14/project_3/fast_s/rehead/rehead_output"$i" --output=/shared/home/mbxrs14/project_3/fast_s/rehead/rehead_output_distruct"$i".svg
done
