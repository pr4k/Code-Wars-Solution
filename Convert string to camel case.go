/*Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized **only** if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 

## Examples

```php
toCamelCase("the-stealth-warrior"); // returns "theStealthWarrior"

toCamelCase("The_Stealth_Warrior"); // returns "TheStealthWarrior"
```
```objc
toCamelCase(@"the-stealth-warrior"); // => @"theStealthWarrior"

toCamelCase(@"The_Stealth_Warrior"); // => @"TheStealthWarrior"
```
```javascript
toCamelCase("the-stealth-warrior") // returns "theStealthWarrior"

toCamelCase("The_Stealth_Warrior") // returns "TheStealthWarrior"
```
```coffeescript
toCamelCase("the-stealth-warrior") # returns "theStealthWarrior"

toCamelCase("The_Stealth_Warrior") # returns "TheStealthWarrior"
```
```ruby
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
```
```python
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
```
```elixir
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
```
```haskell
toCamelCase "the-stealth-warrior" -- returns "theStealthWarrior"

toCamelCase "The_Stealth_Warrior" -- returns "TheStealthWarrior"
```
```csharp
Kata.ToCamelCase("the-stealth-warrior") // returns "theStealthWarrior"

Kata.ToCamelCase("The_Stealth_Warrior") // returns "TheStealthWarrior"
```
```cpp
to_camel_case("the-stealth-warrior") // returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") // returns "TheStealthWarrior"
```
```r
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

to_camel_case("mixed-separator_example") # returns "mixedSeparatorExample"
```
```go
ToCamelCase("the-stealth-warrior"); // returns "theStealthWarrior"

ToCamelCase("The_Stealth_Warrior"); // returns "TheStealthWarrior"
```
```julia
tocamelcase("the-stealth-warrior") # returns "theStealthWarrior"
tocamelcase("The_Stealth_Warrior") # returns "TheStealthWarrior"
```
```scala
toCamelCase("the-stealth-warrior") // returns "theStealthWarrior"

toCamelCase("The_Stealth_Warrior") // returns "TheStealthWarrior"
```*/
package kata
import "strings"
func ToCamelCase(s string) string {
	// your code
  a:=strings.Split(s,"-")
  if len(a)==1{
    a=strings.Split(s,"_")}
    str:=a[0]
  for i:=1;i<len(a);i++{
    str=str+strings.Title(a[i])
  }
  
	return str
}