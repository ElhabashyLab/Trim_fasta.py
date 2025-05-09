# trim_fasta

Command-line Python script allows for flexible trimming of protein FASTA sequences. Users can trim sequences by specifying a range of positions, removing residues from the end, and filtering based on minimum sequence length.

# Installation
> git clone https://github.com/YourUsername/trim_fasta.git  
cd trim_fasta

# Requirements
Python 3.x
No external dependencies are required

# Usage
The script can be run directly from the command line. The following command-line arguments are available for use.
> python3 trim_fasta.py -i INPUT_FILE -o OUTPUT_FILE 

# Argument
-i, --input	str	Path to the input FASTA file (required)  
-o, --output	str	Path to the output FASTA file (required)  
-f	int	First residue to keep (1-based, inclusive)  
-l	int	Last residue to keep (inclusive)  
-t	int	Trim N residues from the end (conflicts with -f or -l)  
-m	int	Minimum length of trimmed sequence to keep (default: 0)  

# Examples
Keep residues 5 to 100 (inclusive):
> python3 fasta_trimmer.py -i input.fasta -o trimmed.fasta -f 5 -l 100

Trim 10 residues from the end of all sequences:
> python3 fasta_trimmer.py -i input.fasta -o trimmed.fasta -t 10

Keep residues from position 20 to the end, but only if result is at least 50 residues long:
> python3 fasta_trimmer.py -i input.fasta -o trimmed.fasta -f 20 -m 50

# License
This script is licensed under the MIT License. See the LICENSE file for more details.  
This script is based on the FASTX-toolkit (https://github.com/agordon/fastx_toolkit) by A. Gordon (assafgordon@gmail.com), originally written in C and licensed under the GNU Affero General Public License (AGPL).



