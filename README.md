# TravelTableTop

Travel Table Top is an ecommerce MVP site that sells travel games sorted by age, min play time and different genres. The dataset is taken from Board Game Geek. The site is built using Django, Python, Postgres and AWS S3 bucket for the portfolio project 5 of Code Institute's Full Stack Development Diploma.

![Different Screen Size Display](./assets_readme/amIResponsive.png)

Live Link: https://travel-table-top-6a0c25007929.herokuapp.com/

## User Experience - UX

### Strategy

I love playing board and Card games. I always try to pack small games when I go travelling to either play solo or with friends/family. On my research I could not find a website that would sell just travel size games. You need to search a lot to find decent examples. Hence, that inspired me to create a website that would sell games just for travel and cater to age groups and genres.

#### User Stories

All user stories can be found in the linked [Github Project](https://github.com/users/hennasingh/projects/8)

### Scope

The user stories were broken into epics and milestones. I had a high-level plan for the project, and I followed Boutique Ado walkthrough to add ecommerce aspect to it. 

Overall, the site aims to provide variety of travel games for your road, airplane, train trips. The platform allows both signed in and anonymous checkout and provides profile management and order history.

Home Page - Introduction to Travel games
Product Page - List of variety of games
Login/Register - To maintain profile and order history, you have to create an account on the site.

### Skeleton

The site designs were generated with help from Claude. I made changes to the design as I progressed in actual development of the site.

<details>
<summary>Travel Table Top Design</summary>

![Website Design](./assets_readme/siteSkeleton.png)

</details>

### User Interface

#### Typography

I used the same font Lato as it was used in Boutique Ado Walkthrough

#### Colors

Color scheme suggestions were taken from Coolers on uploading an image from pexels.com

<details>
<summary>Color Palette</summary>

![color palette](./assets_readme/siteColorPalette.png)

</details>

#### Database Schema

## Agile Methodology

Agile methodology was followed for building the complete site. User Stories were categorized in Epics and Milestones.

### EPICS => MILESTONES

I grouped user-stories in epics which were further grouped in Milestones. Some epics and milestones were added as I progressed with the app.

![epic Milestone](./assets_readme/epicsMilestones.png)

### MoSCoW Prioritization

I applied MoSCoW prioritization and labels to my user stories within the issues tab.

- **must-have**: guaranteed to be delivered
- **should-have**: adds significant value, but not vital
- **could-have**: small impact, but nice to have
- **wont-have**: not a priority for current version

![Moscow Chart](./assets_readme/mosCow.png)

### Github Projects

The Kanban board was created to keep track of different user stories and their progress. Columns such as backlog, in-progress, done, and fixed bugs were added to visualize the workflow.

![Github Project Board](./assets_readme/githubBoard.png)

### User Story Issues

The structure of user-story issue consisted of user story, acceptance criteria, and tasks required to complete the issue. Wherever possible, the commit messages were connected to corresponding issues.

![User Story template](./assets_readme/userStory.png)

## Site Features

## Future Implementations

1. I would like to add more varity of games and specific to travel medium :road, airplane, train.
2. I would like to add review model so that users can review their experience of playing the game.
3. I would like to add wishlist model so users can save list of games.
4. I would like to add a separate nav view for new games and special offers. 
5. I would like to add subscription fetaure where users that subscribe can both sell and buy games from the platform.
6. I would like to customize admin dashboard where admin can see a record of sales, inventory count and most bought games from
the platform

## Tools and Technologies used

- HTML used for the main site content.
- CSS used for the main site design and layout.
- JavaScript used for user interaction on the site.
- Python used as the back-end programming language.
- Git used for version control. (git add, git commit, git push)
- GitHub used for secure online code storage.
- Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
- Django used as the Python framework for the site.
- PostgreSQL used as the relational database management.
- Neon used as the Postgres database.
- Psycopg2 used as a PostgreSQL database adapter
- Heroku used for hosting the deployed back-end site.
- Stripe used for online secure payments of ecommerce products/services.
- AWS S3 used for online static file storage.
- Allauth used as the user authentication system
- Pillow used as the Python framework for the site.
- Gunicorn used for WSGI server
- Crispy Forms used for auto-formatting of front-end forms

## Ecommerce Business Model

This site sells goods to customers, therefore follows a `Business to Customer` model. It is a simplest B2C forms, as it includes
one time payment, and doesn't need anything such as monthly/annual subscriptions.

It is a basic MVP site, with a newsletter and, facebook marketing page.

Promoting on social media can build a community of users around the business, and boost site visitor numbers, especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users. For example, what items are on special offer, new items in stock, updates to business hours, notifications of events, and much more!

## Seach Engine Optimization (SEO) & Social Media Marketing

### Keywords

I identified some appropriate keywords that aligns with my site and when users search for travel games, the website
should appear in the search engine results. These included 2 kinds of keywords:

- Short-tail keywords
- Long-tail keywords#

I played around with [Word Tracker](https://www.wordtracker.com/) to check the frequency of some of my site's primary keywords and also turned the process of searching for keywords into an SEO article.


![work tracker results](./assets_readme/wordTracker.png)

### Sitemap

I'have used [XML-Sitemaps](https://www.xml-sitemaps.com/) to generate a sitemap.xml file. This was generated using my deployed site URL: https://travel-table-top-6a0c25007929.herokuapp.com/

After it finished crawling the entire site, it created a [sitemap.xml](https://github.com/hennasingh/TravelTableTop/blob/main/sitemap.xml) which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](https://github.com/hennasingh/TravelTableTop/blob/main/robots.txt) file at the root-level. Inside, I've added the default settings:

```
User-agent: *
Disallow:
Sitemap: https://travel-table-top-6a0c25007929.herokuapp.com/sitemap.xml
```

#### Further links for future implementation:

[Google search console](https://search.google.com/search-console)
[Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
[Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
[Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales. Social media platforms like Instagram, Facebook if managed properly can aid sales for the website.

I created a [mock facebook page](https://www.facebook.com/traveltabletop) for traveltable top business. (A screenshot added below in case facebook block the page)

![Facebook Mock](./assets_readme/facebookMock.png)

### Newsletter Marketing

I embedded a newsletter sign-up form provided by mailchimp in my application, to allow users to input their email address if they are interested in learning more.

![newsleeter subscription](./assets_readme/newsletterSub.png)

## Testing

For all testing, please refer to testing.md file

## Deployment


