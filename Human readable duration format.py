'''Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns `"now"`. Otherwise,  the duration is expressed as a combination of `years`, `days`, `hours`, `minutes` and `seconds`.

It is much easier to understand with an example:

```c
formatDuration (62)    // returns "1 minute and 2 seconds"
formatDuration (3662)  // returns "1 hour, 1 minute and 2 seconds"
```
```cpp
format_duration(62)    // returns "1 minute and 2 seconds"
format_duration(3662)  // returns "1 hour, 1 minute and 2 seconds"
```
```javascript
formatDuration(62)    // returns "1 minute and 2 seconds"
formatDuration(3662)  // returns "1 hour, 1 minute and 2 seconds"
```
```python
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```ruby
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```elixir
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```php
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```haskell
formatDuration 62     -- returns "1 minute and 2 seconds"
formatDuration 3662   -- returns "1 hour, 1 minute and 2 seconds"
```
```java
TimeFormatter.formatDuration(62)   //returns "1 minute and 2 seconds"
TimeFormatter.formatDuration(3662) //returns "1 hour, 1 minute and 2 seconds"
```
```groovy
Kata.formatDuration(62)   //returns "1 minute and 2 seconds"
Kata.formatDuration(3662) //returns "1 hour, 1 minute and 2 seconds"
```
```shell
duration 62            # echos "1 minute and 2 seconds"
duration 3662          # echos "1 hour, 1 minute and 2 seconds"
```
```julia
formatduration(62)    # returns "1 minute and 2 seconds"
formatduration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```
```racket
(format-duration 62)    ; returns "1 minute and 2 seconds"
(format-duration 3662)  ; returns "1 hour, 1 minute and 2 seconds"
```
**For the purpose of this Kata, a year is 365 days and a day is 24 hours.**

Note that spaces are important.


### Detailed rules

The resulting expression is made of components like `4 seconds`, `1 year`, etc.  In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (`", "`). Except the last component, which is separated by `" and "`, just like it would be written in English. 

A more significant units of time will occur before than a least significant one. Therefore, `1 second and 1 year` is not correct, but `1 year and 1 second` is.

Different components have different unit of times. So there is not repeated units like in `5 seconds and 1 second`.

A component will not appear at all if its value happens to be zero.  Hence, `1 minute and 0 seconds` is not valid, but it should be just `1 minute`.

 A unit of time must be used "as much as possible". It means that the function should not return `61 seconds`, but `1 minute and 1 second` instead.  Formally, the duration specified by  of a component must not be greater than any valid more significant unit of time.'''
def format_duration(seconds):
    
    #your code here
    mins=int(seconds/60)
    seconds=seconds%60
    hours=0
    days=0
    years=0
    if min>=60:
        hours=int(mins/60)
        mins=mins%60
    if hours>=24:
        days=int(hours/24)
        hours=hours%24
    if days>=365:
        years=int(days/365)
        days=days%365
    fr=[]
    if years!=0:
        if years==1:
            fr.append("1 year") 
        else:
            fr.append("{} years".format(years))
    if days!=0:
        if days==1:
            fr.append("1 day")
        else:
            fr.append("{} days".format(days))
    if hours!=0:
        if hours==1:
            fr.append("1 hour")
        else:
            fr.append("{} hours".format(hours))
    if mins!=0:
        if mins==1:
            fr.append("1 minute")
        else:
            fr.append("{} minutes".format(mins))
    if seconds!=0:
        if seconds==1:
            fr.append("1 second")
        else:
            fr.append("{} seconds".format(seconds))
    print(fr)
    if len(fr)>2:
        return ", ".join(fr[:-1])+" and "+fr[-1]
    if len(fr)==2:
        return fr[0]+" and "+fr[-1]
    if len(fr)==1:
        return fr[0]
    if len(fr)==0:
        return "now"
            6 days agoRefactorDiscuss