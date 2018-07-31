# This script will calculate the durations of all labeled segments in a TextGrid object.
# The results will be save in a text file, each line containing the label text and the 
# duration of the corresponding segment..
# A TextGrid object needs to be selected in the Object list.
#
# This script is distributed under the GNU General Public License.
# Copyright 12.3.2002 Mietta Lennes

# ask the user for the tier number
form Calculate durations of labeled segments
	comment Which tier of the TextGrid object would you like to calculate the duration for?
	integer tier_Duration 1
	comment Which tier of the TextGrid object would you like to take the information from?
	integer tier_Label_1 0
	comment Which tier of the TextGrid object would you like to take the information from?
	integer tier_Label_2 0
	comment Which tier of the TextGrid object would you like to take the information from?
	integer tier_Label_3 0
	comment Which tier of the TextGrid object would you like to take the information from?
	integer tier_Label_4 0
	comment Where do you want to save the results?
	text textfile /home/agricolamz/work/materials/2018_Abaza_expedition/sound/for_Tanya/result.txt
endform

# check how many intervals there are in the selected tier:
numberOfIntervals = Get number of intervals... tier_Duration

# loop through all the intervals
for interval from 1 to numberOfIntervals
	label$ = Get label of interval... tier_Duration interval
	# if the interval has some text as a label, then calculate the duration.
	if label$ <> ""
		start = Get starting point... tier_Duration interval
		end = Get end point... tier_Duration interval
		duration = (end - start)*1000
	# get the tier_Label_1 interval number at the start of the tier_Duration:
		secondLabel$ = ""
		if tier_Label_1 > 0
			t2 = Get interval at time... tier_Label_1 end-0.001
			secondLabel$ = Get label of interval... tier_Label_1 t2
		endif
	# get the tier_Label_2 interval number at the start of the tier_Duration:
		thirdLabel$  = ""
		if tier_Label_2 > 0
			t3 = Get interval at time... tier_Label_2 end-0.001
			thirdLabel$ = Get label of interval... tier_Label_2 t3
		endif
	# get the label of smth from tier_Label_3:
		fourthLabel$	= ""
		if tier_Label_4 > 0
			t4 = Get interval at time... tier_Label_3 end-0.001
			fourthLabel$ = Get label of interval... tier_Label_3 t4
		endif
	# get the label of smth from tier_Label_4:
		fifthLabel$	= ""
		if tier_Label_4 > 0
			t5 = Get interval at time... tier_Label_4 end-0.001
			fourthLabel$ = Get label of interval... tier_Label_4 t5
		endif
	# append the label and the duration to the end of the text file, separated with a tab:		
		resultline$ = "'fifthLabel$''tab$''fourthLabel$''tab$''thirdLabel$''tab$''secondLabel$''tab$''label$''tab$''duration''tab$''start''tab$''end''newline$'"
		fileappend "'textfile$'" 'resultline$'
	endif
endfor
