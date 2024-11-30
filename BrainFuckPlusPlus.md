# A quick introductory guide to the pseudocode of BrainFuck++ v1

BrainFuck++ is a pseudocode programming language that was given an actual compiler/translator that converts BrainFuck++ into BrainFuck
The current version of BrainFuck++ will be referred to as v1.
BrainFuck++ is still in development as the for loop statements are a bit "BrainFucked".

The main purpose for BrainFuck++ is to prevent programmers from spending hours copy and pasting the same exact character 100 times. The limitations of the BrainFuck programming language still apply. Whether you use these tools yourself is up to your own discretion.

## All keywords used in BrainFuck++

### `dpinc(x)` and `dpdec(x)`

These commands are used to move the data pointer up or down a corresponding amount inside the brackets.
These are corresponding to `\>` and `<` in BrainFuck.

```
dpinc(5)
dpdec(3)
```
is equivalent to `\>\>\>\>\><<<` in BrainFuck.

### `inc(x)` and `dec(x)`

These commands are used to increment or decrement the value in the byte the data pointer is currently pointing to by a specified amount in the brackets.
This is corresponding to `+` and `\-` in BrainFuck.

```
inc(9)
dec(4)
```
is equivalent to `+++++++++\-\-\-\-` in BrainFuck.

### `input` and `output`

These commands are used to input and output values to and from bytes that the data pointer is currently pointing to.
The `input` command takes a integer input and stores it in that form inside the byte the pointer points to.
The `output` command takes the value stored inside the byte the datapointer points to and outputs the ASCII character equivalent to that value.
These are corresponding to `,` and `.` in BrainFuck.

```
input
output
```
is equivalent to `,.` in BrainFuck.

If a user were to input `71` when the program tries to input a value, then the program would output the ASCII character `G`.

### `loop` and `endloop`

These commands are used in for loops. Whenever `loop` is used then the program will loop through all the commands inbetween the `loop` and it's corresponding `endloop` command as long as the byte that the data pointer points to is a non-zero value.
These are corresponding to `\[` and `\]` in BrainFuck.

In other programming languages like C, this would be equivalent to
```
while (x != 0) {
	// Code here
}
```
The `loop` command does not automatically increment or decrement the value in the byte the pointer points to. You must do that on your own accord.
Due to the nature of the `loop` command, this can actually be used as an if statement to test if the current byte the datapointer points to is 0 or not and to execute at statement that runs once if such a condition is met.

```
inc(3)
loop
dpinc(1)
inc(3)
dpdec(1)
dec(1)
endloop
```
is equivalent to `+++\[\>+++<-\]` in BrainFuck.

### Comments like `//` in BrainFuck++

The `//` in a line is used to denote whether or not a line is a comment. This is styled similarly to C, C++, and C#. However, I have implemented this so horribly that multiline comments are not supported.

## Good programming Practices for BrainFuck and BrainFuck++

Read on through if you want notes to help you.

### `Init()` and `Main()` equivalents

As you may have absolutely noticed, BrainFuck is a programming language that makes your head hurt. Even when programming in the BrainFuck++ programming language, figuring out what to do is very confusing. As such, you should keep this rule in mind:

> For code that only gets ran once at the start, put it ouside of a loop.
> For code that is part of the main program loop, even if the main program only runs once, put it in a loop that terminates when the user inputs that they wish to terminate the program or another condition is met \(signalled by a loop byte\).
> For code that only runs at the end of the program to perform any final cleanups, put it after the main program loop.

By remembering these tips, you can make programming in BrainFuck and BrainFuck++ 1% easier \(a massive productivity boost\).

### BrainFuck and BrainFuck++ have less features than even Assembly

Despite the fact that inputs and outputs exist, printing whole lines of text is annoying as hell. Also, there is no multiplication, division, Bitmasks, or branch instructions. This means that BrainFuck and BrainFuck++ should be considered as a VERY primitive machine code. Any functions have to be implemented everywhere they are used. This means creating Code Snippets. Might explore this in the next BF++ version.

## Final notes

To be honest, I kind of wrote this on a whim while I was trying to setup a programming and design environment on an old HP laptop I just installed Ubuntu on.
I might need to learn a lot more about programming so that I can actually make this language make sense.
