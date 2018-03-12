#!/usr/bin/env python

"""Description

Setup script for IRTools -- a powerful toolset for intron retention detection and analysis

Copyright (c) 2018 Zhouhao Zeng <zzhlbj23@gwmail.gwu.edu>

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file COPYING included with
the distribution).

@version: 1.0.0
@author:  Zhouhao Zeng
@contact: zzhlbj23@gwmail.gwu.edu
"""


import sys
import logging

def run(args):
        if args.quanttype == 'IRI':
                from IRTools.quant_IRI import IRI_quant
                IRI_quanter = IRI_quant(args)
                IRI_quanter.quant()
                IRI_quanter.output_IRI_intron_level()
                IRI_quanter.output_IRI_gene_level()
                IRI_quanter.output_IRI_genome_wide()
                
                if args.ERCC:
                        from quant_ERCC_spike_in import run_quant_ERCC_spike_in
                        run_quant_ERCC_spike_in(args)                  
        elif args.quanttype == 'IRC':
                from IRTools.quant_IRC import IRC_quant
                IRC_quanter = IRC_quant(args)
                IRC_quanter.quant()
                IRC_quanter.output_IRC_junction_level()
                IRC_quanter.output_IRC_intron_level()
                IRC_quanter.output_IRC_gene_level()
                IRC_quanter.output_IRC_genome_wide()
                
                











