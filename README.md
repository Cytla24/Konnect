# Konnect

## [PRESENTATION DECK](https://docs.google.com/presentation/d/1D0VVENqTKYcPaQi2_ys1dEvWMyaOFoqEfjRXDFIodmA/edit#slide=id.g702fa1c2f6_0_241)

### Problem

A lot of small local businesses often lack the visibility and support that they need from customers in order to grow and remain relevant in their community. Advertisements are expensive; small businesses hardly receive the coverage they need on sites such as Yelp. This project aims to serve as a microinfluencer for multiple businesses that register with us. The main problem we found is that people are often steered away from patronizing these local businesses because they can not ascertain the quality of their services

### Solution

We are utilizing trend culture, the easiest and the fastest way to gain coverage about anything in this age of social media, as our means of businesses promotion. As our company is based around trends, we encourage users and businesses to use identifiable hashtags in their tweets, posts etc. We realized that although people are unwilling to give reviews on Google or Yelp, they would readily post about their experiences on the Twitter, Reddit, etc. We use these hashtags ourself to find reviews and comments about these businesses and we utilize sentiment analysis AI, to anaylze these reactions, tags, opinions, reviews scrapped from the main platforms of the internet such as Facebook, Twitter, Reddit etc to generate ratings for the businesses.

### Detailed Technical Breakdown of Solution

- Have small businesses register with us and give us uniquely identifiable keywords that can be associated with their businesses.
- The businesses would also do their part by encouraging users to use those hashtags/keywords when tweeting about the services received
- Search multiple online forums, Twitter, Reddit, facebook for reactions, opinions, comments and reviews.
- Utilize sentimental analysis to generate a score/rating based on the language used in data collected.
- Use the generated ratings/scores to also promote businesses on a "For you" page
- Allow users to search for businesses based on tags
- Display business profile with generated rating and tweets/reviews
- Encourage people to go to these small businesses
- Web/iOS/Android app for people to register a business or search for businesses around them
- Business users can know how their business is doing based on their ratings, comments, reactions and opinions
- Business users can also use our platform to respond to these comments - Future\*
- As we are trend based, we also utilize main platforms such as twitter, facebook to promote trends asscociated with businessed in out database

### Roadmap

- Twitter bot using Tweepy API to search all tweets
- Flask DB to store tweets and info about businesses
- vaderSentiment to analyze reviews
- Generate a rating that is featured on a profile page.
- Display businesses with ratings and related reviews online.

### Moving Forward/Known Isssues

- Check for bots/spammed reviews
- Scrape Instagram for images for the businesses with location pins
- Improve sentiment analysis to accurately differentiate slangs from their literal meanings
