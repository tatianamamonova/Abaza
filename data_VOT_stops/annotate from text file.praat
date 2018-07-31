# This is a Praat script that annotate all annotations from selected TextGrid using text file.
# Compare with http://www.helsinki.fi/%7Elennes/praat-scripts/public/label_from_text_file.praat

# This script is distributed under the GNU General Public License.
# George Moroz 11.09.2017

# read all files from the selected directory -------------------------------------------------------

form Open all files in directory
  comment Provide path to the file with stimuli:
  text resultfile /C:/Users/User/Desktop/azaza/final_edition/2018.07.14_D2_stops/uterances.csv
  comment Which tier should be annotated:
  integer anntier 1
  comment Annotation should be created in every ... interval:
  integer blank 1
  comment Should existing annotation be overwritten (1 is true)?
  integer replace 1
endform

replacement$ = if replace = 1 then ".*" else "^$" fi

grid = selected ("TextGrid", 1)
Read Strings from raw text file: resultfile$
annotfile = selected ("Strings", 1)
n_annotation = Get number of strings
for i from 1 to n_annotation
	selectObject: annotfile
	annotation$ = Get string: i
	selectObject: grid
	Replace interval text: anntier, i*blank, i*blank, replacement$, annotation$, "Regular Expressions"
endfor
selectObject: annotfile
Remove
selectObject: grid