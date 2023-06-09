#!/usr/bin/env python3
import vcf
import matplotlib.pyplot as plt

# Reading the vcf file
#  The calculated values need to be adjusted depending on the Format of the vcf File
vcf_reader = vcf.Reader(filename="input.vcf")

# List to store the AAF values
aaf_values = []

# Loop through the variants
for record in vcf_reader:
    # Get the DP and AO values
    DP = record.INFO.get("DP")
    AO = record.INFO.get("AO")

    # Check if the DP and AO values are available
    if DP is not None and AO is not None:
        # Calculate the AAF
        aaf = AO/DP
        aaf_values.append(aaf)

# Plotting the AAF distribution
plt.hist(aaf_values, bins=50, edgecolor="black")

# Adding labels and title to the plot
plt.xlabel("Allele Frequency")
plt.ylabel("Count")
plt.title("Allele Frequency Distribution")

# Saving the plot as a PNG image
plt.savefig("aaf_distribution.png")