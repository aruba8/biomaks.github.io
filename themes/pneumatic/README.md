# Pneumatic

Pneumatic is a minimalist, single-author [Pelican](http://getpelican.com) theme derived from a [theme](https://github.com/gjreda/gregreda.com/tree/master/theme/simply) developed by [Greg Reda](http://www.gregreda.com). It was named due to the fact that it is based on the [Skeleton](http://www.getskeleton.com) framework, and pelicans (like most birds) possess [skeletal pneumaticity](http://en.wikipedia.org/wiki/Skeletal_pneumaticity).

## Requirements

- [Assets](https://github.com/getpelican/pelican-plugins/tree/master/assets) plugin (and [webassets](https://github.com/miracle2k/webassets))
- [Neighbors](https://github.com/getpelican/pelican-plugins/tree/master/neighbors) plugin
- [Sass](http://sass-lang.com)

## Configuration

- There are intentionally no author, category, and tag page templates, so `AUTHORS_SAVE_AS`, `CATEGORY_SAVE_AS`, `CATEGORIES_SAVE_AS`, and `TAGS_SAVE_AS` should all be set to `''`.
- The files in [static/images](static/images) should be replaced appropriately.
- [`pygments.css`](static/pygments.css) can be modified to change the syntax highlighting colour scheme.
- CodeHilite line numbers should be enabled (ie. `MD_EXTENSIONS = [codehilite(linenums=True)]`).
- Some font and colour choices can be customized in [`pneumatic.scss`](static/pneumatic.scss).

Here are theme-specific settings that should be present in the Pelican configuration file:

|  Setting            | Description                                            |
|:-------------------:|--------------------------------------------------------|
| `SITENAME`          | Text displayed under avatar in sidebar                 |
| `BIO_TEXT`          | Text displayed under site name                         |
| `FOOTER_TEXT`       | Text displayed in site footer                          |
| `SITE_AUTHOR`       | Used for author `<meta>`                               |
| `TWITTER_USERNAME`  | Used for Twitter Cards `<meta>`                        |
| `GOOGLE_PLUS_URL`   | Used for Google+ `<meta>`                              |
| `INDEX_DESCRIPTION` | Used for description `<meta>` on index page            |
| `SIDEBAR_LINKS`     | List of links displayed under bio text (max 5 icons)   |
| `GOOGLE_FONTS`      | List of fonts to import from Google Fonts              |
| `SOCIAL_ICONS`      | List of tuples in the form `(link, title, icon-class)` |
| `DISQUS_SITENAME`   | Disqus shortname (optional)                            |
| `GOOGLE_ANALYTICS`  | Google Analytics tracking code (optional)              |
| `DOMAIN`            | Used for Google Analytics and Twitter Cards `<meta>`   |


## Screenshots

![Index Page](screenshots/index.png?raw=true)

![Article](screenshots/article.png?raw=true)
