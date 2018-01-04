## GDELT indexes the content, provides URL to article
  ## filter stories to TV news
  ## ignore 2nd half of the code that extracts HTML body and tries to find the best paragraph


library(httr)
library(XML)
library(tm)
library(plyr)
library(dplyr)

##-------------------------
## Short Stations
##------------------------
stations = read.csv("market_station_info.csv", header=T, stringsAsFactors = F)
glimpse(stations)
 

# # stations %>% 
# #   filter(Country == "US") 
# 
# k = stations$Country == "US"
# short_stations = stations[k, ]
# 
# ## Remove stations with certain names
# k = grepl("radio|( AM )", short_stations$StationName, ignore.case=T)
# # short_stations$StationName
# # short_stations[k,"StationName"]
# short_stations = short_stations[!k, ]
# 
# k = grepl("^RAD", short_stations$UniqueIdentifier)
# # short_stations[k,"StationName"]
# short_stations = short_stations[!k, ]


short_stations <- stations
##-----------------
## Submit Query to GDELT
##------------------------

  ## Call to the API
url1 = 'https://api.gdeltproject.org/api/v2/doc/doc?query=(teen OR teenager OR child OR toddler OR boy OR girl OR "-year-old") (accidentally OR unintentionally) (shot OR killed OR wounded OR fired) (weapon OR gun OR shotgun OR rifle OR pistol) sourceCountry:US&mode=artlist&maxrecords=250&format=CSV&TIMESPAN=3d'

url = URLencode(url1)
s = GET(url)
  ## Turn content into df
df = read.csv(text = httr::content(s, as="text"), stringsAsFactors = F, header=T)
colnames(df) = c("URL", "MobileURL", "Date", "Title")

glimpse(df)



##-----------------
## Keep only stories from TV Stations
##----------------------
  ## Extract source names
  ## Regex: lookbehind
k = grepl("(?<=http://www.).*?(?=.com)", df$URL, perl=T, ignore.case=T) ## does something match?
m = regexpr("(?<=http://www.).*?(?=.com)", df$URL[k], perl=T, ignore.case=T) ## where does the match start and how long is it
t = regmatches(df$URL[k], m) ## given the start and len vectors, get the actual matches 

df2 = df[k, ]
df2$domain = toupper(t)
glimpse(df2)

r = df2$domain %in% short_stations$UniqueIdentifier
# r
df2 = df2[r, ]

# df2$domain %>% unique
tv_story = merge(x = df2, 
                 y = short_stations[ , c("UniqueIdentifier", "StationName", "Location")],
                 by.x="domain", by.y="UniqueIdentifier")
glimpse(tv_story) ## stories have a lot of repeats (posted by diff. stations)

##--------------------
## Download HTML content of page
##-------------------
  ## For first story
tv_story$place = ""
tv_story$best_para = ""

j = 1
s = GET(tv_story$URL[j]) ## pull all the content
x = htmlParse(file=s, asText=TRUE) ## text

s = xpathApply(x, path="//div", fun=xmlValue) ## (?) at this point returns a messy list that has a lot of HTML tags
s = gsub("\t", "", s)
s = gsub("\n", " ", s)
s = gsub("[ ]{2,}", " ", s) ## better but still long list

s2 = gsub("[ ]?-[ ]?", "-", tv_story$Title[j]) ## removes space in 5-year-old
t = strsplit(s2, split=" ")[[1]] ## tokenize title

  ## s: cleaned up text chunks of the story in a long sparse list
  ## t: tokens of the title
k = grepl("[{}\\]", s) | grepl("()", s, fixed=T) ## remove Javascript
s = s[!k]

##------------------------
## END
##------------------------


## Extract 'best' paragraph (most having same words as title)
## Look for geo-location within paragraph
## Create script to loop process over several days --> write csv
