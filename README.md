# FilmArchive

- Deployed Link - 

## Contents

- [FilmArchive](#FilmArchive)
    - [Contents](#Contents)
    - [Overview](#Overview)
- [User Experience](#User-Experience-(UX))
    - [User Stories](#User-Stories)
    - [Agile and MoSCoW Prioritization](#agile-and-moscow-prioritization)
    - [Entity Relationship Diagram](#entity-relationship-digram)
- [Design](#design)
    - [Wireframes](#wireframes)
    - [Colours](#colours)
    - [Colour Accessibility](#colour-accessibility)
    - [Font](#font)
- [Features](#features)
    - [Header / Navigation](#header--navigation)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [Reviews](#reviews)
    - [Review Detail](#review-detail)
    - [Add Reviews](#add-reviews)
    - [Sign Up](#sign-up)
    - [Profile](#profile)
- [Testing](#testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Python Vaidation](#python-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Lighthouse Test](#lighthouse-test)
    - [WAVE Accessibility Test](#wave-accessibility-test)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Future Features](#future-features)
- [Frameworks and Technologies](#frameworks-and-technologies)
- [Credits](#credits)


## Overview

FilmArchive is a full-stack website designed to create a community amongst film lovers and enthusiasts. The project is centered around the review and comment functionality which was the initial idea for the project. The reviews aspect of the project allows users to create a review on any film of their choosing and share it. Users are also able to comment on any reviews they find interesting as a way to interact with others. Each user has access to a profile which they are able to add an avatar and a bio. The profile is also a location where users are able to see the reviews they have made as well as their watch later section. By default reviews are saved to the users profile allowing them to easily be managed and acts as a way to track films that have been watched. Furthermore, films can be added to a watch later list if users see any films that peak their interest and want to remember them for the next time they are looking for a film to watch.

## User Experience (UX)

### User Stories

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I can view a home page so that I can see relevant information about the website and how it works. | **MUST HAVE** |
| As a **user**, I can create an account so that I can access additional features of the website. | **MUST HAVE** |
| As a **user**, I have access to an account page so that I can view my details, reviews I have made and my watched / want to watch lists. | **MUST HAVE** |
| As a **user**, I have access to a reviews page so that I can see a list of all recent reviews other users have submitted. | **MUST HAVE** |
| As a **user**, I can create a review so I can share my thoughts on a film and interact with the community. | **MUST HAVE** |
| As a **user**, I can edit reviews I have made so that I can update any information about the film / change the review itself. | **MUST HAVE** |
| As a **user**, I can comment on other users reviews as a way to interact with the rest of the community. | **MUST HAVE** |
| As a **Site Owner**, I can create, read, update and delete reviews from the website in order to manage the content that is shown. | **MUST HAVE** |
| As a **user**,  I can add films to my watch later list so that I can keep track of films I want to see. | **SHOULD HAVE** |
| As a **user**, I can delete films from my watch later list in case I no longer want to watch them or they were added by mistake. | **SHOULD HAVE** |
| As a **user**, films I have reviewed will be added to my watched/ reviewed list so that I can keep track of films I have already reviewed. | **COULD HAVE** |
| As a **user**, I can remove comments made on my own reviews so that there are no unnecessary or unwanted comments. | **WONT HAVE** |
| As a **user**, I can edit my comment on a review.  | **COULD HAVE** |



### Agile and MoSCoW Prioritization

Throughout the process of creating the project Agile planning methods were used. Using a GitHub project board I was able to map out the website features / user stories. In addition, the tasks were placed into one of three categories : Todo, In Progess and Done which allowed me track each task. This in turn gave me a good reference point for the overall progression of the project at different stages, which I found useful. MoSCoW Prioritization was used alongside this to split up tasks / user stories into either : Must Have, Should Have, Could Have or Won't have. This allowed for a clearer plan and to understand what tasks needed to be completed in order to achieve the MVP.

Project Board - [link](https://github.com/users/m-dixon5/projects/3)

![FilmArchive Project Board](documentation/images/project-board.jpg)

### Entity Relationship Digram

Before starting the project an Entity Relationship Diagram was created in order to map out the database and to visualise how each table would interact with one another. I first created each table with all the neccessary key and field pairs using pen and paper. After I was happy that all fields and models were covered I moved on to determining the relationship each table had with another. To finalise everything I converted everything I had written down into Lucid Chart (see images below).

![Entity Relationship Diagram](documentation/images//ERD.png)

## Design

### Wireframes

From the start I tried to keep the project layout as simple as possible, putting more emphasis on creating an easier experience for the user. Figma was used to create the wireframes which allowed me to create a more detailed picture of what each page was going to look like compared to other design sites. Furthermore, due to the detail of the wireframes created the finished project managed to look very similar to the original designs / plans.

<details open>
<summary>Mobile Wireframes</summary>

![Mobile wireframes](documentation/images/Mobile-Wireframe.png)
</details>

<details open>
<summary>Tablet Wireframes</summary>

![Tablet wireframes](documentation/images/Tablet-Wireframe.png)
</details>

<details open>
<summary>Desktop Wireframes</summary>

![Desktop wireframes](documentation/images/Desktop-Wireframes.png)
</details>

### Colours

![Colour Palette](documentation/images/colour-palette.png)

Simililar to the layout and structure of the site I kept the number of colours I used for the project to a minimum. The logo was created initially and determined the colours I finally choose for the website. Shades of grey / black make up the majority of the palette and were used for different layers / feature backgrounds and a shade of white was used for the majority of the text. The final colour of red was used throughout the website to highlight or break up certain features.

### Colour Accessibility

All colour pairings were checked using Adobe Color Contrast Checker :

![Contrast check image 1](documentation/images/black-white-contrast2.png)

![Contrast check image 2](documentation/images/red-black-contrast.png)

![Contrast check image 3](documentation/images/black-white-contrast.png)


### Font

## Features

### Header / Navigation

<details open>
<summary>Header Image</summary>

![Header Image](documentation/images/navbar.png)
</details>
The navigation / header, like many other elements, has a minimal design. The background colour matches the rest of the main / body which allows the page to look cleaner and flow better. Each nav link also has css applied to it to indicate which element is currently hovered over by the user.

### Footer

<details open>
<summary>Footer Image</summary>

![Footer Image](documentation/images/footer.png)
</details>

The footer was also kept simple with a design similar to a earlier project. It includes social media icons that when clicked open in a new tab and have styles applied to indicate the user is hovering over them. The website does not have any social media accounts and the links instead take users to the signup / start pages. However, the github is linked to my own account.

### Home page

<details open>
<summary>Home Page Image</summary>

![Home Page Image](documentation/images/main-page.png)
</details>

The home page consists of a hero section, about section and four info cards. The hero section is kept concise and points out how signing up can give the user access to certain features. A sign up button is also included for new users and takes them straight to the registraton page. Info cards can also be found below the about section to give a quick overview about the features available to the user.

<details>
<summary>Info Cards Image</summary>

![Info Cards Image](documentation/images/info-cards.png)
</details>

### Reviews

<details open>
<summary>Reviews Page Image</summary>

![Reviews Page Image](documentation/images/reviews-page.png)
</details>

All user reviews are displayed in the reviews section with each review given its own card. The cards display the film image, film title, user and a short summary of the user review that is limited to 100 characters. Each card acts as a link and opens up the full review page when clicked. Cards are also responsive at all screen sizes by using bootstrap rows and columns.

### Review Detail

<details open>
<summary>Review Detail Image</summary>

![Review Detail Image](documentation/images/review-detail.png)
</details>

After clicking on a review card from the reviews page each review opens up in more detail with the full review, rating and date watched being displayed. JavaScript was included which alters the background colour of the rating depending on how high the user scored the film. For films below 4 the background colour is red, between 4 and 6 orange, between 6 and 8 light green and above 8 a darker green. The comments section was placed below the review card and the add button is available for users who have a registered account.

### Add Reviews

<details open>
<summary>Add Review Page Image</summary>

![Add Review Page Image](documentation/images/add-review.png)
</details>

The Add review form utilises crispy forms and allows uses to input all the details on the film they want to review. A RichTextField was also used for the main review input to allow users to add additional styles and manipulate the layout. Cloudinary was used also to allow users to upload their film images and store them. Lastly, the review summary input uses django max and min validators meaning the user cannot enter a value that is outside the range of 0 to 10.

### Sign Up

<details open>
<summary>Sign Up Page Image</summary>

![Sign Up Page Image](documentation/images/sign-up-page.png)
</details>

The sign up page form follows the basic design of the majority of the input forms across the website. Django AllAuth  was used to provide user authentication and the basic templates. In addition, the form provides user feedback if email and password fields are inputted incorrectly . An image of this can be seen below.

<details open>
<summary>Sign Up Error</summary>

![Sign Up Error](documentation/images/sign-up-error.png)
</details>

### Profile 

<details open>
<summary>Profile Page Image</summary>

![Profile Page Image](documentation/images/profile-image.png)
</details>

The Profile page starts out as a blank canvas and allows the user to add an avatar and a bio through a modal that appears after the edit button is clicked. Reviews that have been made by the user can be seen in the dropdown menu and link to the detailed view. The watch later feature is also located in the profile with the user being able to add a film by clicking the button which takes them to a seperate page. Users can also see how many films have either been reviewed or added to the watch later section next to their respective titles.


## Testing

### HTML Validation

To validate my HTML files I used the validator provided by W3C and inputted the code via direct input. The code was copied from the page source instead of the workspace due to django template language being present on all pages.

Most pages returned no errors or warnings apart from one or two. A common error was a button being located inside an anchor tag which was found across two pages. All fixes were simple enough and didn't cause too much hassle.

<details open>
<summary>HTML Validation Image</summary>

![HTML Validation Image](documentation/images/home-page-validation.png)
</details>

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- | 
| Home | 0 | 0 |
| Sign In | 0 | 0 |
| Sign Up | 0 | 0 |
| Profile | 0 | 0 |
| Edit Profile Modal | 0 | 0 |
| Reviews Page | 0 | 0 |
| Add Review | 0 | 0 |
| Review Detail | 0 | 0 |
| Edit Review | 0 | 0 |
| Delete Review | 0 | 0 |
| Delete Comment | 0 | 0 |
| Add to Watch Later | 0 | 0 |
| Edit Watch Later Item | 0 | 0 |
| Delete Watch Later Item | 0 | 0 |

### CSS Validation

To validate my css file I used W3C CSS Validator. Orginally there were 2 errors relating to an incorrect font-weight value and a style that could not be set to none. These were quick fixes and after running the code again all errors had cleared. However, there are still 4 warnings present that relate to styles applied to scroll bars.

<details open>
<summary>CSS Validation Image</summary>

![CSS Validation Image](documentation/images/css-validation.png)
</details>

### Python Validation

Python validation was completed using [CI Python Linter](https://pep8ci.herokuapp.com/#) which presented a couple small issues across different files. These issues mainly being empty lines at the end and a couple lines running over the character limit. Throughout the project the python black module was used on the files to try and keep everything up to date.

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
| Home | no errors | no errors | no errors | no errors | no errors |
| Profiles  | no errors | no errors | no errors | no errors | no errors |
| Reviews | no errors | no errors | no erros | no errors | no errors |
| Project App | na | na| na | no errors | na |

### JavaScript Validation

### Lighthouse Test

Testing both the reviews and home page on desktop and mobile sizes the lighthouse scores for the project were all around pretty good. All the images used for the website are WEBP or were converted to WEBP using Convertio to get the highest scores possible. A few issues that cropped up were related to the hero section and the logo not being sized correctly.

<details open>
<summary>Lighthouse Home Page - Desktop</summary>

![Lighthouse Home Page - Desktop](documentation/images/desktop-home-lighthouse.png)
</details>

<details open>
<summary>Lighthouse Reviews Page - Desktop</summary>

![Lighthouse Reviews Page - Desktop](documentation/images/desktop-reviews-lighthouse.png)
</details>

<details open>
<summary>Lighthouse Home Page - Mobile</summary>

![Lighthouse Home Page - Mobile](documentation/images/mobile-home-lighthouse.png)
</details>

<details open>
<summary>Lighthouse Reviews Page - Mobile</summary>

![Lighthouse Reviews Page - Mobile](documentation/images/mobile-reviews-lighthouse.png)
</details>

### WAVE Accessibility Test

## Deployment

## Bugs

## Future Features

- Adding a film API that allows users to search for any film on an external database. This in turn would make it much quicker for users to review a film or add one to watch later as they are not required to input the information themselves. 

- Implementing a refine search to the reviews section that would allow users to search for reviews based on different criteria and tags associated with reviews.

- Ability to search or view other users profiles to see their reviews or watch later lists.

- Add a review count on each review / post so users are able to see how many times their post has been viewed. This could also link well with the refine search where users can filter by most popular reviews.

- Be able to create a thread in the comments section of each review to further enchance interactivity between users. This would allow multiple discussions to take place under any one post / review.

## Frameworks and Technologies

## Credits
