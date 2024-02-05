# One-to-Many - Blogly

#### Part Two: Adding Posts
Posts should have an:
- [X] **id**, like for **User**
- [X] **title**
- [X] **content**
- [X] **created_at** a date+time that should automatically default to the current time when the post is created
- [X] a foreign key to the **User** table

#### User Interface
- [X] Better User detail
- [X] New Post Form
- [X] Post Detail Page
- [X] Post Edit Page

#### Add Post Routes
- [X] **GET** /users/[*user_id*]/posts/new : Show form to add a post for that user.
- [X] **POST** /users/[*user_id*]/posts/new : Handle add form; add post and redirect to the user detail page.
- [X] **GET** /posts[*post_id*] : Show a post. Show buttons to edit and delete the post.
- [X] **GET** /posts/[*post_id*]/edit : Show form to edit a post, and to cancel (back to user page).
- [X] **POST** /posts/[*post_id*]/edit : Handle editing of a post. Redirect user back to the post view.
- [X] **POST** /posts/[*posts_id]/delete : Delete the post.

**Change the user page**
- [X] Change the user page to show the posts for that user

**Testing**
- [X] Update any broken tests and add more testing

**Celebrate!**
- [X] Yay! Congratulations on the first two big parts.
