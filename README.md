# Skreefuck - a Brainfuck interpreter with SKREEE

![skree](https://derpicdn.net/img/view/2017/10/3/1550781.gif)

Works same as brainfuck:

|command|BF equivalent|
|-------|-------------|
| `eee` | `+`         |
| `eeE` | `-`         |
| `eEe` | `<`         |
| `eEE` | `>`         |
| `Eee` | `[`         |
| `EeE` | `]`         |
| `EEe` | `.`         |
| `EEE` | `,`         |

A file needs to start with `skr`.

Hello world example:

```
skreeeeeeeeeeeeeeeeeeeeeeeeEeeeEEeeeeeeeeeeeeEeeeEEeeeeeeeEEeeeeeeeeeeEEeeeeeeeeeeEEeeeeEeeEeeEeeEeeeEEeEeEEeeeeEEeeeeEEeeEeEEeEEeeeEeeeEeEeEeEeeeEEeEeEEeEEEEeeEEeeEeeEeeEEEeeeeeeeeeeeeeeeeeeeeeeEEeEEeeeeeeeeeeEEeeEEeEEEEeeEeeeEEEeeEeEEeeeeeeeeeeEEeeeEeeEeeEeeEeeEeeEEEeeeEeeEeeEeeEeeEeeEeeEeeEEEeeEEeEEeeeEEeeEEeeeeeeEEe
```

## Usage

`./skree.py somefile` where somefile contains the skree to execute

## Conversion from brainfuck

`./bf_to_ef.py somefile` where somefile contains the brainfuck code. It prints the result to stdout
