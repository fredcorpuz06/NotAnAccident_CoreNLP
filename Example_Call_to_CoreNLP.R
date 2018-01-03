##-------------------------
## Submit Request to Server
##-------------------------
library(httr)
library(tidyverse)
library(dplyr)
  ## note that we do not pass any additional parameters - we are fine with the default ones
url = 'http://athina.wesleyan.edu:9000/'

  ## This is where our story text would go.
story_text = "Hartford, CT (AP) Police reported a major shoot-out between two teenagers yesterday. A 15-year-old boy fatally shot his 14-year-old friend."



  ## perform a POST request.
  ## send text to CoreNLP for it to be analyzed
s = POST(url, body=URLencode(story_text), encode="form") ## turn into 'url' with %20 as spaces
status_code(s)
s$url
s$content
  ## Unpacking POST and URLencode
# y <- URLencode("a url with spaces and / and @")
# URLdecode(y)
# 
# 
# z <- "ab%20cd"
# URLdecode(z)
# c(URLencode(z), URLencode(z, repeated = TRUE)) # first is usually wanted

b2 <- "http://httpbin.org/post"
p1 = POST(b2, body = "A simple text string")
p$url
p$content
p2 = POST(b2, body = list(x = "A simple text string"))
p3 = POST(b2, body = list(y = upload_file(system.file("CITATION"))))
p4 = POST(b2, body = list(x = "A simple text string"), encode = "json")



  ## convert JSON-text into a list
w = content(s, as="parse")
w = content(s)
##---------------------------------
## Analyze return values
##--------------------------------
  ## NER: Name Entity Recognition
w$sentences[[1]]$entitymentions
w$sentences[[1]]$entitymentions[[1]]$text
w$sentences[[1]]$entitymentions[[1]]$ner
w$sentences[[1]]$entitymentions[[2]]$text
w$sentences[[1]]$entitymentions[[2]]$ner


len = length(w$sentences[[1]]$entitymentions)
entity_mentions = vector(mode = 'list',
                         length = len)

# entity_mentions[[1]] <- c(w$sentences[[1]]$entitymentions[[1]]$ner, w$sentences[[1]]$entitymentions[[1]]$text)
for(i in 1:length(w$sentences[[1]]$entitymentions)){
  entity_mentions[[i]] <- c(w$sentences[[1]]$entitymentions[[i]]$ner,
                            w$sentences[[1]]$entitymentions[[i]]$text)
}

w$sentences[[2]]$entitymentions


  
  ## IE: Open Information Extraction
w$sentences[[1]]$openie %>% length
w$sentences[[2]]$openie %>% length

w$sentences[[2]]$openie[[1]]$subject
w$sentences[[2]]$openie[[1]]$relation
w$sentences[[2]]$openie[[1]]$object

  ## Report

for (p in w$sentences[[2]]$openie) { ## p is a unnamed list within 'openie'
  cat(p$subject, p$relation, p$object, "\n")
}


results<-vector(mode = "list", length = 4) 
results2 <- vector('numeric', 3)

strsplit(LETTERS[1:10], "")
x <- c(as = "asfef", qu = "qwerty", "yuiop[", "b", "stuff.blah.yech")
# split x on the letter e
strsplit(x, "e")
x = list(1, 2, 3, 4)
x
x[1] %>% class
x[[1]] %>% class
x2 = list(1:4)
x2
