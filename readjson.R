library("rjson")
library("plyr")

json_data<- fromJSON(file = "modencodeMetaData.json")

json_data<- json_data$items

data_list<-lapply(json_data, as.data.frame, stringAsFactors=FALSE)

res<-rbind.fill(data_list)

write.csv(res,file = "abc.csv")

