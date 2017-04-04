# CheapFlights
A personal project to aggregate flight searches from multipe travel websites such as Kayak, Kiwi, FlightHub, etc.

## Motivation
I'm an avid traveller. In the Fall of 2016 I was planning an across-the-globe trip starting in Canada and spanning Europe, India, Japan, and Hong Kong; I'd depart over the Atlantic and return over the Pacific. While planning, I discovered that the results for airfare (especially multi-city airfare) varied from site to site. I searched for days, and I was able to knock off over $300 off of my initial searches by buying tickets from three different websites. Beaming with pride over my greatest accomplishment since making an edible meal, I often gloated to my friends and family how I'm the master of finding the cheapest flights for any complicated route (in fact, my smugness cost me my reputation as a meek and humble individual). However, the more I bragged out loud, the more that got me thinking. Did I really find the cheapest flight one could possibly find? How can I guarantee that it is the cheapest? What if I had searched for a few more days? 

## Goal
This project isn't necessarily intended to turn into an app or package, it's to practice Python, Hadoop, and Spark while solving a problem I love to tackle for myself and my friends - finding cheap airfare. If the solution turns into something bigger, all the better! Regardless, every project big or small needs a direction. My goals for this project include:

### Short-term:
* To create a Python script to aggregate and display search results from multiple websites. While searching for airfare in different sites, most of the time goes towards entering and re-entering the same details into different interfaces and then going through the painstaking effor to compare the various results. This is intended to speed up this process by returning results from multiple websites in one screen within minutes (and hopefully seconds!).

### Long-term:
* Different travel websites use different methods for cost and route optimization. However, if every site is truly optimized to find you the cheapest flights, how am I able to consistently find a cheaper route by using different websites? My long term goal is to set up batch jobs to aggregate and store flight searches in a NoSQL database, such as HBase, and compute the cheapest way to get from point to point by combining different results for different websites using Spark. 

## Solution

<!---
At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.) -->
