setwd("C:\\Users\\haric\\OneDrive\\Documents\\GitHub\\project-deliverable-2-targaryens\\data") 

#reading dataframe containing number of reviews with respective to positive,negative,neutral
data_count <- read.table("C:\\Users\\haric\\OneDrive\\Documents\\GitHub\\project-deliverable-2-targaryens\\data\\dataset_count.txt", sep = "\t", header = TRUE)

# importing ggplot2 library for data visualization
library(ggplot2)

# Displaying a bar plot using ggplot2
# To display the number of negative, neutral and positive reviews
ggplot(data_count, aes(x = Pos.Neu.Neg, y = NumberofReviews, fill = Pos.Neu.Neg)) + 
  geom_bar(stat = "identity", width = 0.5, fill=c("darkgrey","lightblue","darkblue")) + 
  geom_text(aes(label = NumberofReviews), vjust = 0, fontface = "bold") + 
  labs(x = 'Positive/Neutral/Negative', y = 'Number of Reviews') + 
  scale_y_continuous(breaks = seq(500, 3000, by = 500)) + labs(title = "Number of Positive,Neutral, and Negative reviews")+ 
  theme(plot.title = element_text(hjust=0.5, colour ="Black", face = "bold", size="17"))+theme(plot.background = element_rect(fill = 'white', color="red")) + 
  theme(panel.background = element_rect(fill = 'white', color="red"))

# Displaying a pie plot using ggplot2
# To display the response of audience towards the show in the form of percentage
count_sum <- sum(data_count$NumberofReviews)
count_sum

percent_val <- round(100*data_count$NumberofReviews/count_sum)
ggplot(data_count, aes(x = "",y=NumberofReviews, fill= Pos.Neu.Neg)) + 
  geom_col(color = "black") + 
  geom_label(aes(label = paste0(percent_val, "%")), position = position_stack(vjust = 0.5), size=8, show.legend = FALSE) + coord_polar(theta = "y") + 
  scale_fill_brewer(palette="Blues") + 
  guides(fill = guide_legend(title = "Positive/Neutral/Negative")) + theme_minimal() +
  labs(title = "comparing percentage of Positive,Neutral, and Negative reviews")


# reading the csv file that contains the number of reviews.

# total reviews given for the show in each website
website_data <- read.csv("/Users/haric/OneDrive/Documents/GitHub/project-deliverable-2-targaryens/data/website_rev_count.csv", sep = ',')
website_data

library(webr)
library(lessR)
library(plotly)
total_count <- sum(website_data$Total_Reviews)
total_count

# Computing percentages
website_data$per_val = website_data$Total_Reviews / total_count

# Plotting Doughnut chart to indicate which website
# Website which has more number of reviews given by audience in the form of percentage
website_per <- website_data %>% group_by(Website)
fig <- website_per %>% plot_ly(labels = ~Website, values = ~per_val)
fig <- fig %>% add_pie(hole = 0.6)
fig <- fig %>% layout(showlegend = T, xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE))%>%
  layout(title="Displays the website in which audience gave more reviews")


fig

data_rating <- read.csv("/Users/haric/OneDrive/Documents/GitHub/project-deliverable-2-targaryens/data/dataset_with_Rating.csv", sep = ',')
data_rating

library(formattable)
data_rating$Percentage <- formattable::percent(data_rating$Rating) 

write.csv(data_rating, "dataset_with_Rating.csv", row.names=FALSE)
rating <- read.csv("/Users/haric/OneDrive/Documents/GitHub/project-deliverable-2-targaryens/data/dataset_with_Rating.csv", sep = ',')
rating

# Creating a barplot 
# to display the ratings given in Social media websites
ggplot(rating, aes(fill = Website_Name, y = Percentage, x = Website_Name)) + 
  geom_bar(position="stack", stat="identity") +
  ggtitle("Ratings given in Social media websites") +
  xlab("")+labs(title = "Displaying the ratings given in Social media websites")
