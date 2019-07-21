'''Define a function that takes in two non-negative integers `a` and `b` and returns the last decimal digit of `a^b`. Note that `a` and `b` may be very large!

For example, the last decimal digit of `9^7` is `9`, since `9^7 = 4782969`.  The last decimal digit of `(2^200)^(2^300)`, which has over `10^92` decimal digits, is `6`.  Also, please take `0^0` to be `1`.

You may assume that the input will always be valid.

## Examples

```haskell
lastDigit 4 1             `shouldBe` 4
lastDigit 4 2             `shouldBe` 6
lastDigit 9 7             `shouldBe` 9
lastDigit 10 (10^10)      `shouldBe` 0
lastDigit (2^200) (2^300) `shouldBe` 6
```
```javascript
lastDigit("4", "1")            // returns 4
lastDigit("4", "2")            // returns 6
lastDigit("9", "7")            // returns 9    
lastDigit("10","10000000000")  // returns 0
```
```python
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
```
```kotlin
lastDigit(4, 1)                # returns 4
lastDigit(4, 2)                # returns 6
lastDigit(9, 7)                # returns 9
lastDigit(10, 10 ** 10)        # returns 0
lastDigit(2 ** 200, 2 ** 300)  # returns 6
```
```ruby
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
```
```cpp
last_digit("4", "1")            // returns 4
last_digit("4", "2")            // returns 6
last_digit("9", "7")            // returns 9    
last_digit("10","10000000000")  // returns 0
```
```r
last_digit("4", "1")            # returns 4
last_digit("4", "2")            # returns 6
last_digit("9", "7")            # returns 9    
last_digit("10","10000000000")  # returns 0
```
```rust
last_digit("4", "1")            // returns 4
last_digit("4", "2")            // returns 6
last_digit("9", "7")            // returns 9    
last_digit("10","10000000000")  // returns 0
```
```purescript
lastDigit "4" "1"            -- => 4
lastDigit "4" "2"            -- => 6
lastDigit "9" "7"            -- => 9
lastDigit "10" "10000000000" -- => 0
```

___

## Remarks

### JavaScript, C++, R, PureScript

Since these languages don't have native arbitrarily large integers, your arguments are going to be strings representing non-negative integers instead.'''
def last_digit(n1, n2):
    n1=n1%10
    k=2
    if (n2==0):
        return 1
    while True:
        if (n1==(n1**k)%10):
            break
        k+=1
    k-=1
    if k==1:
        return n1%10
    while True:
        if (n2==0):
            return ((n1%10)**k)%10
        if (n2<=k):
            return ((n1%10)**n2)%10
        n2=n2%k
        