setwd("C:/Users/User/Desktop/azaza/sounds")
write.csv(data.frame(d = list.dirs()), 
          "C:/Users/User/Desktop/azaza/annotated.csv", 
          row.names = FALSE)
