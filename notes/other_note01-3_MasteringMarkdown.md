# Mastering Markdown

Created based on [this document](https://guides.github.com/features/mastering-markdown/).

Markdown is a lightweight and easy-to-use syntax
for styling all forms of writing on the GitHub platform.

## What is Markdown?

<!-- https://www.markdowntutorial.com/ -->

[Markdown](http://daringfireball.net/projects/markdown/) is a way to
style text on the web. You control the display of the document;
formatting words as bold or italic, adding images, and creating lists
are just a few of the things we can do with Markdown. Mostly, Markdown
is just regular text with a few non-alphabetic characters thrown in,
like `#` or `*`.

You can use Markdown most places around GitHub:

- [Gists](https://gist.github.com/)
- Comments in Issues and Pull Requests
- Files with the `.md` or `.markdown` extension

For more information, see "[Writing on
GitHub](https://help.github.com/categories/writing-on-github/)" in the
*GitHub Help*.

## Examples

### Text

```source
It's very easy to make some words **bold** and other words *italic* with Markdown.  
You can break a line with double spaces or "\" at the end of the line. 
You can even [link to Google!](http://google.com)
```

It\'s very easy to make some words **bold** and other words *italic* with Markdown.  
You can break a line with double spaces or "\" at the end of the line.\
You can even [link to Google!](http://google.com/)

### List

```source
Sometimes you want numbered lists:

1. One
2. Two
3. Three

Sometimes you want bullet points:

* Start a line with a star
* Profit!

Alternatively,

- Dashes work just as well
- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this
```

Sometimes you want numbered lists:

1. One
2. Two
3. Three

Sometimes you want bullet points:

- Start a line with a star
- Profit!

Alternatively,

- Dashes work just as well
- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this

### Links

```source
Tutorial for Python can be found [here](https://wiki.python.org/moin/BeginnersGuide).
```

Tutorial for Python can be found [here](https://wiki.python.org/moin/BeginnersGuide).

### Images

```source
If you want to embed images, this is how you do it:

![husky](./figures/husky.jpeg)
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
```

If you want to embed images, this is how you do it:

![husky](./figures/husky.jpeg)
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

### Headers & Quotes

```source
# Structured documents

Sometimes it's useful to have different levels of headings to structure your documents. Start lines with a `#` to create headings. Multiple `##` in a row denote smaller heading sizes.

### This is a third-tier heading

You can use one `#` all the way up to `######` six for different heading sizes.

If you'd like to quote someone, use the > character before the line:

> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway
```

# Structured documents

Sometimes it's useful to have different levels of headings to structure
your documents. Start lines with a `#` to create headings. Multiple `##`
in a row denote smaller heading sizes.

### This is a third-tier heading

You can use one `#` all the way up to `######` six for different heading
sizes.

If you'd like to quote someone, use the \> character before the line:

> Coffee. The finest organic suspension ever devised... I beat the Borg
> with it. - Captain Janeway

### Code

```source
There are many different ways to style code with GitHub's markdown. If you have inline code blocks, wrap them in backticks: `var example = true`.  If you've got a longer block of code, you can indent with four spaces:

    if (isAwesome){
      return true
    }

GitHub also supports something called code fencing, which allows for multiple lines without indentation:
```

if (isAwesome){
  return true
}

```
And if you'd like to use syntax highlighting, include the language:

```javascript
if (isAwesome){
  return true
}
```

```
There are many different ways to style code with GitHub's markdown. If you have inline code blocks, wrap them in backticks: `var example = true`.  If you've got a longer block of code, you can indent with four spaces:

    if (isAwesome){
      return true
    }

GitHub also supports something called code fencing, which allows for multiple lines without indentation:
```

if (isAwesome){
  return true
}

```
And if you'd like to use syntax highlighting, include the language:

```javascript
if (isAwesome){
  return true
}
```

### Extras

```source
GitHub supports many extras in Markdown that help you reference and link to people. If you ever want to direct a comment at someone, you can prefix their name with an @ symbol: Hey @kneath — love your sweater!

But I have to admit, tasks lists are my favorite:

- [x] This is a complete item
- [ ] This is an incomplete item

When you include a task list in the first comment of an Issue, you will see a helpful progress bar in your list of issues. It works in Pull Requests, too!

And, of course emoji!
```

GitHub supports many extras in Markdown that help you reference and link
to people. If you ever want to direct a comment at someone, you can
prefix their name with an @ symbol: Hey
[\@kneath](https://github.com/kneath) --- love your
sweater!

But I have to admit, tasks lists are my favorite:

- This is a complete item
- This is an incomplete item

When you include a task list in the first comment of an Issue, you will
see a helpful progress bar in your list of issues. It works in Pull
Requests, too!

And, of course emoji!

## Syntax guide

Here's an overview of Markdown syntax that you can use anywhere on
GitHub.com or in your own text files.

### Headers

```
# This is an <h1> tag
## This is an <h2> tag
###### This is an <h6> tag
```

### Emphasis

```
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_
```

### Lists

#### Unordered

```
* Item 1
* Item 2
  * Item 2a
  * Item 2b
```

#### Ordered

```
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
```

### Images

```
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
```

### Links

```
http://github.com - automatic!
[GitHub](http://github.com)
```

### Blockquotes

```
As Kanye West said:

> We're living the future so
> the present is our past.
```

### Inline code

```
I think you should use an
`<addr>` element here instead.
```

## GitHub Flavored Markdown

GitHub.com uses its own version of the Markdown syntax that provides an
additional set of useful features, many of which make it easier to work
with content on GitHub.com.

Note that some features of GitHub Flavored Markdown are only available
in the descriptions and comments of Issues and Pull Requests. These
include \@mentions as well as references to SHA-1 hashes, Issues, and
Pull Requests. Task Lists are also available in Gist comments and in
Gist Markdown files.

### Syntax highlighting

Here's an example of how you can use syntax highlighting with [GitHub
Flavored
Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/):

```
```julia
function fsum(x)
    n = length(x)
    s = 0
    for i in 1:n
        s += x[i]
    end
    return s
end
```

```
```julia
function fsum(x)
    n = length(x)
    s = 0
    for i in 1:n
        s += x[i]
    end
    return s
end
```

### Task Lists

```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
```

If you include a task list in the first comment of an Issue, you will
get a handy progress indicator in your issue list. It also works in Pull
Requests!

### Tables

You can create tables by assembling a list of words and dividing them
with hyphens `-` (for the first
row), and then separating each column with a pipe
`|`:

```
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
```

Would become:

| First Header                | Second Header                |
| --------------------------- | ---------------------------- |
| Content from cell 1         | Content from cell 2          |
| Content in the first column | Content in the second column |

### Username \@mentions

Typing an `@` symbol, followed
by a username, will notify that person to come and view the comment.
This is called an "\@mention", because you're *mentioning* the
individual. You can also \@mention teams within an organization.

### Automatic linking for URLs

Any URL (like `http://www.github.com/`) will be automatically converted into a clickable
link.

### Strikethrough

Any word wrapped with two tildes (like `~~this~~`) will appear crossed out.

### Emoji

GitHub supports
[emoji](https://help.github.com/articles/basic-writing-and-formatting-syntax/#using-emoji)!

To see a list of every image we support, check out the [Emoji Cheat
Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).
