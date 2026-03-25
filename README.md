# libraryboxd

An internal web application for managing and tracking book diaries, reviews, and maintaining my home library. Inspired by Letterboxd, but for books!

## Table of Contents
* [Overview](#overview)
* [Features](#features)
* [Technologies](#technologies)
* [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
* [Usage](#usage)
    - [Full Walkthrough](#full-walkthrough)
* [Main Goals](#main-goals)
* [Privacy & Security](#privacy-and-security)
* [Admin Operations](#admin-operations)
* [Future Roadmap](#future-roadmap)
* [Contributing](#contributing)
* [What I learned](#what-i-learned)
* [Credits / License](#credits--licence)

## Overview

This project serves fewer than 50 users and provides a private, in-house platform (hosted on Ubuntu 22.04) for tracking individual reading histories and sharing book reviews. Users can maintain personal reading diaries, review and rate books, and view a catalog curated by library administrators.

## Features

*User Registration & Authentication* - Secure Signup/Login for all users.

*Privacy-Aware Profiles* - Users can be private (history/reviews visible only to themselves and admins) or public (visible to all other users).

*Reading Diary* - Log books read. Undated entries are listed alphabetically; dated entries are shown in reverse chronological order.

*Book Catalog* - Browse all available books within the library.

*Book Detail Pages* - Aggregate visible reviews and ratings from users, respecting privacy settings.

*Admin Catalog Management* - Book catalog maintained via spreadsheet import and manual entry.

    *Note: Social features like likes, comments, and friendship models are planned for future releases.*

## Technologies

* *Core Stack*

    - **Programming Language**: Python
    - **Web Framework**: Django
    - **Database**: SQL
    - **Frontend**: HTML5, CSS3, Javascript
*  *Server and Deployment*
    - **OS / Platform**: Ubuntu LTS 22.04
    - **Application Server**: Gunicorn
    - **Web Server**: Nginx
    - **Process Management**: systemd
* *Development and Tooling*
    - **Environment Managment**: 
        - `venv`
        - `pip`
    - **Version Control**: Git
* *Administration / Data Import*
    - **Admin Interface**: Django Admin
    - **Data Import**: 
        - `CSV-Import`
        - `csv Python Libraries`
    - **API**: Open Library

## Getting Started

### Prerequisites

- Ubuntu 22.04 server
- Python 3.10+ / Django / pip
- PostgreSQL

        Since this is a private project, Users will need to be whitelisted before being able to connect to the database. Please contact me at [EMAIL] for further instructions.

### Installation

1. Clone the repository:


2. Install dependencies:


3. Configure environmental variables:


4. Apply database migrations:


5. Run the application:

## Usage
- **Create an account**:\
Registration is required.
- **View the catalog**: \
Browse all available books in your library.
- **Log and review books**: \
Add books to your diary, rate, and write a review.
- **Privacy**: \
Choose whether your activity is personal or public.

### Full Walkthrough


## Main Goals
- Self hosting of library database.
- Users are able to:
    - update reading diaries 
    - leave book reviews
    - like other user reivews
    - view other user's reading diaries.

## Privacy and Security

- All profiles are either personal (viewable only by self/admin) or public (viewable by all other users).

- User data is internal and never exposed externally.

- Admins have privileged access for catalog management.

## Admin Operations


- Import book catalog via spreadsheet (.csv, .xls) or manual entry.
- Configure user privacy and manage accounts.
- *(Optional\*)* - integration with free, non-commercial book APIs for metadata (future).

## Future Roadmap

## Contributing

## What I Learned

-- Written post completion --

## Credits / Licence

<!--
## Formatting
- **Bold**
- *Italic*
- `Inline code`

Code block:
```bash
echo "Hello, librarybox"
```

## Lists
1. First item
2. Second item
	- Subitem

## Link
[Example site](https://example.com)

## Image
![logo](assets/logo.png)

## Table
| Name | Description |
| --- | --- |
| librarybox | Demo project |

> Keep documentation concise.
-->
