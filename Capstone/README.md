### General Assembly Capstone Project

### Motivation
What makes a game fun to play? Can we predict how good a game will be given some basic information about the game? If we can determine what makes a game fun, it makes it possible to avoid hours spent playing subpar games. Also, it can motivate game designers to make more games with features that were found to be more fun.

### The Data
The data for this project was found on Kaggle datasets. The original source is boardgamegeek.com (BGG), which has a useful API for minning data. The data consists of the top 4,999 rated board games (rows) with 20 features for each game.

The features are:

| Feature | Type | Description |
| ------- | ---- | ----------- |
| rank | int | BGG rank (1-4999) |
| bgg_url | str | BGG URL for the game |
| game_id | int | Unique id for each game |
| names | str | Name of the game |
| min_players | int | Minimum number of players required to play |
| max_players | int | Maximum number of players |
| avg_time | int | Average length of a game (min) |
| min_time | int | Minimum time required for a game | 
| max_time | int | Maximum length of a game (min); same as avg_time |
| year | int | Release year |
| avg_rating | float | Average user rating | 
| geek_rating | float | Bayesian average rating that rank is based on |
| num_votes | int | Number of reviews |
| image_url | str | URL for an image of the game |
| age | int | Recommended minimum age of players |
| mechanic | str | Comma-separated list of game mechanics |
| owned | int | Number of BGG users that own the game |
| category | str | Comma-separated list of game categories |
| designer | str | Comma-separated list of game designers |
| weight | float | Weight of the game (lbs) |

### Goal
Predict BGG rating using game features.
