# BF-- Utilities

This is a repo with some tools to ease the pain for those who wish to work in the programming language of BrainFuck (Whoever you are, you must be a masochist)

The Tools included:
* A python Brainfuck-- translator that translates the pseudocode of BrainFuck-- into BrainFuck
* A .xml file containing a User Defined Language for Notepad++ in order to help with syntax highlighting
* A guide for programming in the pseudocode of Brainfuck-- and Brainfuck++

## IMPORTANT! Regarding Brainfuck++ and Brainfuck-- and why I decided to branch them

When I first conceptualised what is now known as Brainfuck--, I believed that I might have thought of something original that needs sharing with the world. However, I recently learned that a documentation with all the specifications for Brainfuck++ already exists.
Brainfuck++ was first specified within [The Association for Computational Heresy's recording of the proceedings of SIGBOVIK 2022.](https://sigbovik.org/2022/proceedings.pdf)
As such, I decided to branch my repo into two. The `Main` branch will continue to contain what is now known as BF-- whereas the `BF++` branch will contain code that is oriented around Brainfuck++ as specified during the proceedings of SIGBOVIK 2022.

## Brainfuck-- translator

The Following program takes an input of a file that has the file extension of .bfmm and outputs a file with the extension of .bf which contains Brainfuck Code.

## Brainfuck-- User Defined Language

When using the text editor Notepad++, you can import the UDL by navigating to Language/User Defined Language/Define your language... and then pressing Import and selecting the File provided.
If the UDL isn't automatically loading, try restarting Notepad++ and your file should be highlighted. If not, Go into Languages and select the BF++ UDL.

## BrainFuck-- programming guide

A guide on the BrainFuck-- Programming language can be found [here](BrainFuckMinusMinus.md)

I chose the CC0 License for my project because my code is for the people, they are meant to be stolen.
