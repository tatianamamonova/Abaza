library(tidyverse)
setwd("C:/Users/User/Desktop/azaza/final_edition/2018.07.14_D2_stops/")
length(list.files())
df <- readLines("C:/Users/User/Desktop/azaza/анкеты/anketa_oksana.txt", encoding = "UTF-8")
length(df)

data_frame(df)  %>% 
  mutate(df = str_replace(df, "\t", " "),
         df = str_replace(df, " $", "")) %>%
  filter(df != "") ->
  df

template <- "2018.07.14_D1_stops_"

if(length(df$df) == length(list.files())){
  file.rename(list.files(), paste0(template, df$df, ".WAV"))  
} else{
  paste0("Разное количество: в тексте (",
         length(df$df),
         "), файлов (",
         length(list.files()),
         ")")
}

data_frame(rep(c("u_1", "u_2", "u_3", "cf"), length(df$df))) %>%
  write_csv("uterances.csv", col_names = FALSE)

data_frame(rep(c("v1", "cd", "vot", "v2"), length(df$df)*4)) %>% 
  write_csv("annotation.csv", col_names = FALSE)
