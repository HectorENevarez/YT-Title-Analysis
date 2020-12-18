# YouTube Video Title Language Analysis
This analysis provides insight as to what kind of language in a science & technology YouTube video title yields the most viewers. This was achieved by scraping data from thousands of YouTube videos and going through exploratory data analysis on the language of a video title and its direct impact on the amount of views.

## Code and Resources Used
**Python Version:** 3.6 <br>
**Packages:** Pandas, Langdetect, NLTK, Seaborn, Matplotlib, Heapq, Itertools, Textstat, Selenium

## Web Scraping
All video scraping scripts can be accessed by navigating to the scraping_data directory:
```bash
cd ./scraping_data
```

The web scrapping scripts gather data from a list of science & technology YouTubers. The data that was collected was:
- Channel Name
- Channel Subscribers
- Video Link
- Video Views
- Video Likes
- Video Dislikes
- Video Description

## Data Cleaning
The data cleaning was included in the youtube_title_data_analysis.ipynb file's first section. The data was cleaned by:
- Removing non-english titles
- Removing any channel names in the title
- Removing symbols such as emojis and punctuation
- Removing any outliers

## Exploratory Data Analysis
The goal of the data analysis was to provide insight as to what kind of language in the video title yielded the highest amount of views. The first approach was to analyze the bigrams that had the highest amount of views. I compared the different types of bigrams that had the most views on average from the entire dataset to the bigrams of small, medium, and large YouTube channels


![ ](images/bigrams_all.png =100x20)

