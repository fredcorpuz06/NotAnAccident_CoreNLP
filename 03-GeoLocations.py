### Finding Geo-Locations \
import numpy as np
import pandas as pd
date = '1228'
df = pd.read_csv('P:\QAC\Projects\datadive17\NotAnAccident\Fred_files\NER_query' + str(date) + '.csv')

##--------------------
## Gazetteer files
	## USPS: US Postal Service State Abb
	## GEOID: Fully concatenated geographic code
	## ANSICODE: Am Nat Stantards Institute Code
##-----------------------
	
def display_top(col):
	print col.value_counts(dropna=False).head()
	print 'Length of DF: ', len(col)

	## Counties
gaz_counties = pd.read_table(r'P:\QAC\Projects\datadive17\NotAnAccident\NER\2016_Gaz_counties_national.txt')
gaz_counties.columns = gaz_counties.columns.str.strip()
# print gaz_counties['NAME'].describe() ## Unique values 1,955 (Washington County)
# gaz_counties[['ANSICODE', 'NAME']].apply(display_top)
	## Place
gaz_place = pd.read_table(r'P:\QAC\Projects\datadive17\NotAnAccident\NER\2016_Gaz_place_national.txt')
gaz_place.columns = gaz_place.columns.str.strip()
# print gaz_place['NAME'].describe()	## Unique 24,398 (Franklin City)

# 	## County subdivisions
# gaz_cousubs = pd.read_table(r'P:\QAC\Projects\datadive17\NotAnAccident\NER\2016_Gaz_cousubs_national.txt')
# # print gaz_cousubs['NAME'].describe() ## Unique 21,842 (District 2)
# # gaz_cousubs['NAME'].value_counts(dropna=False)
# 	# Urban areas
# gaz_ua = pd.read_table(r'P:\QAC\Projects\datadive17\NotAnAccident\NER\2016_Gaz_ua_national.txt')
# # print gaz_ua['NAME'].describe() ## Unique 3601 (Fairmond, NC Urban cluster)	
cols = ['USPS', 'NAME', 'INTPTLAT', 'INTPTLONG']
gaz = pd.concat([gaz_counties[cols], gaz_place[cols]]) ## append rows


##--------------------------
## IF we get perfect location extraction
##--------------------------
man_loc = pd.read_csv('P:\QAC\Projects\datadive17\NotAnAccident\Fred_files\ManualGeoLoc1228_clean.csv')

man_loc = man_loc.replace('.', np.nan)
man_loc.columns = man_loc.columns.str.lower()
	## @param Dataframe with 'places' and 'county'
	## @return String value of more accurate location
def better_place(df):
	if pd.notnull(df['places']):
		# return 'something'
		return df['places']
	else:
		# return 'nothing'
		return df['county']

man_loc['best_loc'] = man_loc[['county', 'places']].apply(better_place, axis=1)




 	## Merge to get the Lat and Long
man_coords = pd.merge(man_loc, gaz, how='left', left_on=['usps','best_loc'], right_on=['USPS','NAME'])
