Python 3.8.8 (default, Apr 13 2021, 12:59:45) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> samfile = pysam.AlignmentFile("file.bam") 
>>> start = 115740000
>>> stop = start + 4999
>>> window_counts = [0] * 20000
>>> window = 0
>>> for read in samfile.fetch("chr1",115740000,116000000):
                for read in samfile.fetch("chr1",start,stop):
                                if read.mapping_quality >= 30 and (not read.is_duplicate) and read.is_paired and (not read.mate_is_unmapped):
                                                mate = samfile.mate(read)
                                                if mate.mapping_quality >= 30 and mate.reference_name == "chr1" and (read.template_length >=1000 or read.template_length <= -1000):
                                                                window_counts[window] = window_counts[window] + 1
                print(start, stop, window_counts[window], file=open("Integration Site.txt", "a") 
                start = start + 500
                stop = stop + 500
                window = window + 1