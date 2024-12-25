This Python script parses and visualizes HPGL (Hewlett-Packard Graphics Language) plotter files. It uses matplotlib for graphical rendering and supports basic HPGL commands such as PU (pen up), PD (pen down), SP (select pen color), SI (set text size), LB (label text), and RO (rotation). Key features include:

Reading HPGL files: Reads and preprocesses the HPGL content by removing newlines.
Parsing commands: Extracts valid HPGL commands using regular expressions.
Plotting commands: Handles drawing commands (PU, PD), text labeling (LB), pen selection (SP), and scaling/rotation (RO) using transformations.
Visualization: Displays the final graphical output using matplotlib.

Usage Instructions
Command-line usage:

Run the script with a single argument specifying the path to the HPGL file:

python hpglview.py <hpgl_file>
Replace <hpgl_file> with the path to your .plt or HPGL file.
