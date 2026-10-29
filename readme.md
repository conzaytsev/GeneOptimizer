# Gene Optimizer
Python module for gene optimisation based on CEI and GeneSpace models.

This tool is based on [Codon Expression Index](https://github.com/conzaytsev/CodonExpressionIndex) and [Gene Space](https://github.com/conzaytsev/GeneSpace) models

## Requirements
`Python>3.9`, for custom model training: `cei`, `genespace`

## Data
This tool comes with a pre-trained model for E. coli.

It can also be used with custom models.

For CEI a custom dataset should be provided as a table in the csv format with three columns: ID; expression value; gene sequence.
First line of the table is reserved for the header.


Example:

    Protein ID;Protein copies;Gene sequence
    P69776;38022.530250746298;ATGAAAGCTACTAAACTGGTACTGGGCGCGGTAATCCTGGGTTCTACTCTGCTGGCAGGTTGCTCCAGCAACGCTAAAATCGATCAGCTGTCTTCTGACGTTCAGACTCTGAACGCTAAAGTTGACCAGCTGAGCAACGACGTGAACGCAATGCGTTCCGACGTTCAGGCTGCTAAAGATGACGCAGCTCGTGCTAACCAGCGTCTGGACAACATGGCTACTAAATACCGCAAGTAA
    P0AG51;4376.7908013480401;ATGGCAAAGACTATTAAAATTACTCAAACCCGCAGTGCAATCGGTCGTCTGCCGAAACACAAGGCAACGCTGCTTGGCCTGGGTCTGCGTCGTATTGGTCACACCGTAGAGCGCGAGGATACTCCTGCTATTCGCGGTATGATCAACGCGGTTTCCTTCATGGTTAAAGTTGAGGAGTAA
    P0A7Q6;3802.6818971891998;ATGAAAGTTCGTGCTTCCGTCAAGAAATTATGCCGTAACTGCAAAATCGTTAAGCGTGATGGTGTCATCCGTGTGATTTGCAGTGCCGAGCCGAAGCATAAACAGCGCCAAGGCTGA


The GeneSpace model can either use the same format dataset as CEI, or a Fasta file with nucleotide sequences.

## Installation
From PyPI:

    pip install genop

For the latest development version: 
    
    pip install git+https://github.com/conzaytsev/GeneOptimizer.git

## Usage
#### Using the pre-trained models:

    import genop

    model = genop.Optimizer(input_sequence)
    optimized_sequence = model.optimize(target_expression)

#### Using custom models:

    import genop
    import cei
    import genespace

    expression_model = cei.CodonExpressionIndex(path_to_dataset)
    subspace_model = genespace.CodonPairSubspace(path_to_dataset, nu=0.1)
    optimization_model = genop.Optimizer(input_sequence, expression_model=expression_model, subspace_model=subspace_model)
    optimized_sequence = model.optimize(target_expression)

#### `genop.Optimizer` parameters:

To use a nucleotide input_sequence (default):
    
    sequence_type='nucleotide'

To use an amino acid input_sequence:
    
    sequence_type='protein'

To activate an optimization parameter set its priority value to any positive value (default 0 for everything except `expression_priority`):
    
    expression_priority=1
    subspace_priority=1
    center_priority=1
    gc_priority=1

Each parameter's priority value affects its influence on the internal weight function. Higher values compared to other parameters make optimized sequence more tailored to the target values of such parameters.

To exclude any oligonucleotides from the optimized sequence:
    
    restriction_sites = ['AAGGTAGGC', 'TTTATTATT']

#### `Optimizer.optimize` parameters:

Target expression value in ppm (protein copies per million expressed by the cell):

    target_score=10

Distance from the edge of the genome subspace (positive values indicate that a sequence fits inside the subspace, negative for the outside):

    target_distance=0.002

Distance from the center of the gene space (values from 0 to 1 indicate sequence codon usage irregularity, where 0 means that each codon is used exactly the same number of times and 1 if for a sequence consisting exclusively of a single codon:

    target_center=0.3

% of the target GC content in the optimized sequence:

    target_gc=0.46



