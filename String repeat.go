/*Write a function called `repeatStr` which repeats the given string `string` exactly `n` times.

```c
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
```

```lua
repeatStr(6, "I") -- "IIIIII"
repeatStr(5, "Hello") -- "HelloHelloHelloHelloHello"
```

```elixir
repeat_str(6, "I") # "IIIIII"
repeat_str(5, "Hello") # "HelloHelloHelloHelloHello"
```

```scala
StringRepeat.repeatStr(6, "I") # "IIIIII"
StringRepeat.repeatStr(5, "Hello") # "HelloHelloHelloHelloHello"
```

```nim
repeatStr(6, "I") # "IIIIII"
repeatStr(5, "Hello") # "HelloHelloHelloHelloHello"
```

```julia
repeatstr(6, "I") # "IIIIII"
repeatstr(5, "Hello") # "HelloHelloHelloHelloHello"
```

```kotlin
repeatstr(6, "I") # "IIIIII"
repeatstr(5, "Hello") # "HelloHelloHelloHelloHello"
```*/
package kata

func RepeatStr(repetitions int, value string) string {
  st:=""
  for i:=0;i<repetitions;i++{
    st=st+value}
  return st
}