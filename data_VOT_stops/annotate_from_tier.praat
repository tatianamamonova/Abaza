# This is a Praat script that creates a new tier and splits non-empty intervals on selected number of subintervals.

# This script is distributed under the GNU General Public License.
# George Moroz 18.07.2018

form start
  comment Which tier is the base for the splist?
  integer ut_tier 2
  comment How many new intervals should be created?
  integer n_intervals 4
endform

Insert interval tier: 1, ""
ut_tier = ut_tier+1
n_annotation = Get number of intervals: ut_tier
for i from 1 to n_annotation
	start = Get starting point: ut_tier, i
	end = Get end point: ut_tier, i
	interval_n = Get interval at time: ut_tier, start
	label_n$ = Get label of interval: ut_tier, interval_n
	if label_n$ != ""
		for j from 0 to n_intervals
			boundary_time = start + (end-start)/(n_intervals)*j
			Insert boundary: 1, boundary_time
		endfor
	endif
endfor
