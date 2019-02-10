# [DEPREACATED] NotAnAccident_CoreNLP 

## What is this project?

The project aims to fully automate the data collection & parsing for Everytown's [NotAnAccident Index](https://everytownresearch.org/notanaccident/). First, I use the [GDELT API](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) to get the links of stories relatings to children and guns. Next, I use [Stanford CoreNLP's Open Information Extraction](https://stanfordnlp.github.io/CoreNLP/openie.html) to summarize the stories into a subject, relation, object triplet. Lastly, I send an email with a .csv attached containing the relevant information via SMTP.





