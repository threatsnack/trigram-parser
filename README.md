# trigram-parser
TLDR: This is a program that parses files / text for trigrams, and prints out the most common 100. You can pass as many files as you'd like as arguments, or concatenate as many files as you'd like and pipe them to the script.

## How to Use
To get started:

`pip install -r requirements.txt`

You may need to make the python script executable:

`chmod +x ./trigram.py`

# Pass Files as an Argument
For example, `./trigram.py mytext.txt`
https://github.com/threatsnack/trigram-parser/blob/main/readme-assets/onefile.gif

![Pass any file as an argument](https://github.com/threatsnack/trigram-parser/blob/main/readme-assets/onefile.gif)

You can pass more than one file if you'd like. For example:
`./trigram.py mytext.txt myothertext.txt`

![Pass multiple files as an argument](https://github.com/threatsnack/trigram-parser/blob/main/readme-assets/twofiles.mp4)

As you can see above, when you pass more than one file as an argument to the script, it will calculate the number of trigrams for each, and will include the name of the file it's parsing. This is intended behavior.

If you'd like to calculate the combined number of trigrams for more than one file, consider using a utility like cat and piping those to the script instead- see the below example.

# Pipe Files to the Script
The script will also read input from stdin. For example,
`cat myfile.txt | ./trigram.py`

![Pipe files to the script](https://github.com/threatsnack/trigram-parser/blob/main/readme-assets/stdin.gif)

You can pipe more than one file to the script as well if you'd like. When you pass the script input from stdin, the output will not include a file name. This is on purpose. For example, if you concatenate two files together, it makes sense that you do not need results divided by each individual file.

## Time Spent and Lessons Learned
On-call was kinda busy during the week, so I spent part of a weekend on this.

When I started this project, I'd never heard of an ngram, and I'd never written a tool that parsed text outside of anomaly detection scenarios. I tried to write idiomatic python instead of my usual "style", which is basically writing python like a bash script.

Don't get me wrong- initially, I still wrote this program exactly like a bash script, but once it was working I refactored it a couple of times until I was mostly sure it wouldn't offend any real developers too much. :P

I don't have the opportunity to write very much python these days outside of personal pet projects, so this was a super fun exercise.

I especially appreciate that this was take-home. I perform pretty poorly when I have to do in-person coding challenges, so this really was a breath of fresh air.

## What I'd Do Next / Things I Would Change
- I think there are improvements I could make to the scope of my exception handling.

- There are definitely additional usage guidelines I could add to argparse, to make both methods of passing text more clear to the end user.

- I could refactor this script to be a true `ngram` parser- allowing someone to calculate a bigram, a trigram, a fourgram, and so on. It doesn't need to be trigram specific, and in fact the only thing giving it the appearance of being trigram specific is the naming of the functions. Otherwise, we could just change the second argument passed to the `ngram()` function.

- I could probably find ways to make the script more performant.

- I could definitely find ways to make my code more aesthetically pleasing. I used `black` to format my code here, but I'm a big fan of PEP-8's maximum line length and `black` doesn't accomodate for that. I'm sure there are other conventions I'm missing, too.

- I could definitely find ways to make the output a lot nicer, too.
